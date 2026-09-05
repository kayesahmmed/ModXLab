import re

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "r") as f:
    content = f.read()

# I see the issue!
# I had: `className="p-6 rounded-[24px] relative"` in the form, and `className="rounded-[24px] overflow-hidden transition-all duration-150 relative group"` for the motion.div FAQ item.
# BUT I also added `overflow-hidden rounded-[24px]` to the inner z-10 div.
# And for the modal item: `className="rounded-2xl overflow-hidden transition-all duration-150 relative border"`

# The blur is applied to an absolute inset-0 child. If that absolute inset-0 child bleeds outside the border-radius of the parent, it will look like the stroke is messed up or missing at the corners.
# Wait, if the parent has border, the `inset: 0` child will overlap the border area (since inset: 0 stretches to the padding-box).
# If the absolute child overlaps the border, the border might be invisible or look weird, especially since the child has a background color and blur.
# The correct way to prevent an absolute inset-0 child from overlapping the border is to use `inset: 0` and make sure it has `z-index: 0`, and since it's inside a parent with a border, it shouldn't overlap if box-sizing is border-box.
# But wait, backdrop-filter can sometimes bleed.
# Let's just move the border TO the absolute child, OR move it back to how it was originally!
# Why did I split it into a separate absolute div in the first place? To apply transform3d to the blur layer ONLY, because applying transform3d to the parent `<motion.div>` was causing layout issues with height animation?
# No! Adding transform3d to the motion.div directly was perfectly fine!
# Ah, if I just put the `translate3d(0,0,0)` directly in the motion.div style, does it cause issues?
# Let's revert FAQSection to a cleaner state but with the translate3d properties attached directly to the main element, and remove the inner absolute divs for the blur.

def restore_blur_directly(content, search_class, blur_val):
    # This might be too complex to regex blindly. Let's do it manually for the 3 instances.
    pass

# Instance 1: Form
form_old = """              <form onSubmit={handleAsk} className="p-6 rounded-[24px] relative" style={{ 
                border: `1px solid rgba(255, 255, 255, 0.2)`,
                boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
              }}>
                <div className="absolute inset-0 rounded-[24px] pointer-events-none z-0" style={{
                  background: "rgba(255, 255, 255, 0.12)", 
                  backdropFilter: "blur(12px)", 
                  WebkitBackdropFilter: "blur(12px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                }} />
                <div className="relative z-10">"""
form_new = """              <form onSubmit={handleAsk} className="p-6 rounded-[24px] overflow-hidden" style={{ 
                background: "rgba(255, 255, 255, 0.12)", 
                backdropFilter: "blur(12px)", 
                WebkitBackdropFilter: "blur(12px)",
                WebkitTransform: "translate3d(0, 0, 0)",
                transform: "translate3d(0, 0, 0)",
                WebkitBackfaceVisibility: "hidden",
                backfaceVisibility: "hidden",
                border: `1px solid rgba(255, 255, 255, 0.2)`,
                boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
              }}>"""
content = content.replace(form_old, form_new)

form_end_old = """                {errorMsg && <div className="mt-2 text-red-500 text-sm font-semibold">{errorMsg}</div>}
                </div>
              </form>"""
form_end_new = """                {errorMsg && <div className="mt-2 text-red-500 text-sm font-semibold">{errorMsg}</div>}
              </form>"""
content = content.replace(form_end_old, form_end_new)


# Instance 2: FAQ Item
faq_item_old = """                className="rounded-[24px] overflow-hidden transition-all duration-150 relative group"
                style={{ 
                  border: isOpen ? `1px solid rgba(22, 207, 131, 0.4)` : `1px solid rgba(255, 255, 255, 0.2)`,
                  boxShadow: isOpen ? `0 8px 32px 0 rgba(22, 207, 131, 0.25)` : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                }}
              >
                <div className="absolute inset-0 rounded-[24px] pointer-events-none z-0" style={{
                  background: "rgba(255, 255, 255, 0.12)", 
                  backdropFilter: "blur(12px)",
                  WebkitBackdropFilter: "blur(12px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                }} />
                <div className="relative z-10 w-full overflow-hidden rounded-[24px]">"""

faq_item_new = """                className="rounded-[24px] overflow-hidden transition-all duration-150 relative group"
                style={{ 
                  background: "rgba(255, 255, 255, 0.12)", 
                  backdropFilter: "blur(12px)",
                  WebkitBackdropFilter: "blur(12px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                  border: isOpen ? `1px solid rgba(22, 207, 131, 0.4)` : `1px solid rgba(255, 255, 255, 0.2)`,
                  boxShadow: isOpen ? `0 8px 32px 0 rgba(22, 207, 131, 0.25)` : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                }}
              >"""
content = content.replace(faq_item_old, faq_item_new)

faq_end_old = """                    </motion.div>
                  )}
                </AnimatePresence>
                </div>
              </motion.div>"""
faq_end_new = """                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.div>"""
content = content.replace(faq_end_old, faq_end_new)


# Instance 3: Modal Wrapper
modal_old = """              className="w-full max-w-3xl max-h-[85vh] rounded-3xl p-6 sm:p-8 flex flex-col gap-5 border shadow-2xl relative"
              style={{
                border: "1px solid rgba(255, 255, 255, 0.15)",
                boxShadow: "0 20px 50px -10px rgba(0, 0, 0, 0.85)"
              }}
            >
              <div className="absolute inset-0 rounded-3xl pointer-events-none z-0" style={{
                background: "rgba(30, 30, 40, 0.6)",
                backdropFilter: "blur(24px)",
                WebkitBackdropFilter: "blur(24px)",
                WebkitTransform: "translate3d(0, 0, 0)",
                transform: "translate3d(0, 0, 0)",
                WebkitBackfaceVisibility: "hidden",
                backfaceVisibility: "hidden",
              }} />
              <div className="relative z-10 flex flex-col gap-5 max-h-full overflow-hidden">"""

modal_new = """              className="w-full max-w-3xl max-h-[85vh] rounded-3xl p-6 sm:p-8 flex flex-col gap-5 border shadow-2xl overflow-hidden relative"
              style={{
                background: "rgba(30, 30, 40, 0.6)",
                backdropFilter: "blur(24px)",
                WebkitBackdropFilter: "blur(24px)",
                WebkitTransform: "translate3d(0, 0, 0)",
                transform: "translate3d(0, 0, 0)",
                WebkitBackfaceVisibility: "hidden",
                backfaceVisibility: "hidden",
                border: "1px solid rgba(255, 255, 255, 0.15)",
                boxShadow: "0 20px 50px -10px rgba(0, 0, 0, 0.85)"
              }}
            >"""
content = content.replace(modal_old, modal_new)

modal_end_old = """              </div>
              </div>
            </motion.div>
          </motion.div>
        )}"""
modal_end_new = """              </div>
            </motion.div>
          </motion.div>
        )}"""
content = content.replace(modal_end_old, modal_end_new)

# Instance 4: Modal Item
modal_item_old = """                      <div
                        key={faq.id}
                        className="rounded-2xl overflow-hidden transition-all duration-150 relative border"
                        style={{
                          borderColor: isOpen ? "rgba(22, 207, 131, 0.4)" : "rgba(255, 255, 255, 0.1)",
                          boxShadow: isOpen ? "0 4px 20px -5px rgba(22, 207, 131, 0.25)" : "none"
                        }}
                      >
                        <div className="absolute inset-0 rounded-2xl pointer-events-none z-0" style={{
                          background: "rgba(255, 255, 255, 0.05)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          WebkitTransform: "translate3d(0, 0, 0)",
                          transform: "translate3d(0, 0, 0)",
                          WebkitBackfaceVisibility: "hidden",
                          backfaceVisibility: "hidden",
                        }} />
                        <div className="relative z-10 overflow-hidden rounded-2xl">"""

modal_item_new = """                      <div
                        key={faq.id}
                        className="rounded-2xl overflow-hidden transition-all duration-150 relative border"
                        style={{
                          background: "rgba(255, 255, 255, 0.05)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          WebkitTransform: "translate3d(0, 0, 0)",
                          transform: "translate3d(0, 0, 0)",
                          WebkitBackfaceVisibility: "hidden",
                          backfaceVisibility: "hidden",
                          borderColor: isOpen ? "rgba(22, 207, 131, 0.4)" : "rgba(255, 255, 255, 0.1)",
                          boxShadow: isOpen ? "0 4px 20px -5px rgba(22, 207, 131, 0.25)" : "none"
                        }}
                      >"""
content = content.replace(modal_item_old, modal_item_new)

modal_item_end_old = """                            </motion.div>
                          )}
                        </AnimatePresence>
                        </div>
                      </div>"""
modal_item_end_new = """                            </motion.div>
                          )}
                        </AnimatePresence>
                      </div>"""
content = content.replace(modal_item_end_old, modal_item_end_new)

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "w") as f:
    f.write(content)
