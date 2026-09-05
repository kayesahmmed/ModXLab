import re

def process_file(path, replacements):
    with open(path, "r") as f:
        content = f.read()
    for o, n in replacements:
        if o not in content:
            print(f"Warning: could not find {o[:50]}... in {path}")
        content = content.replace(o, n)
    with open(path, "w") as f:
        f.write(content)

# ================= HeroSection.tsx =================
hero = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"

h_search_old = """              <div
                className={`transition-all duration-350 ease-[cubic-bezier(0.16,1,0.3,1)] h-14 flex items-center overflow-hidden rounded-2xl border ${
                  searchOpen ? "w-[260px] sm:w-[320px] opacity-100 border-white/20 pointer-events-auto" : "w-0 opacity-0 border-transparent pointer-events-none"
                }`}
                style={{
                  background: "rgba(255, 255, 255, 0.18)",
                  backdropFilter: "blur(16px)",
                  WebkitBackdropFilter: "blur(16px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                  boxShadow: "0 8px 32px 0 rgba(0,0,0,0.15)"
                }}
              >
                <div className="relative w-full h-full flex items-center">"""
h_search_new = """              <div
                className={`transition-all duration-350 ease-[cubic-bezier(0.16,1,0.3,1)] h-14 flex items-center rounded-2xl relative ${
                  searchOpen ? "w-[260px] sm:w-[320px] opacity-100 pointer-events-auto" : "w-0 opacity-0 pointer-events-none"
                }`}
              >
                <div className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 border ${searchOpen ? "border-white/20" : "border-transparent"}`} style={{
                  background: "rgba(255, 255, 255, 0.18)",
                  backdropFilter: "blur(16px)",
                  WebkitBackdropFilter: "blur(16px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                  boxShadow: "0 8px 32px 0 rgba(0,0,0,0.15)"
                }} />
                <div className="relative w-full h-full flex items-center z-10 overflow-hidden rounded-2xl">"""

h_search_end_old = """                    </div>
                  )}
                </motion.div>
              )}
              </AnimatePresence>
            </div>
          </motion.div>
        </motion.div>"""
h_search_end_new = """                    </div>
                  )}
                  </div>
                </motion.div>
              )}
              </AnimatePresence>
            </div>
          </motion.div>
        </motion.div>"""

h_drop_old = """                    style={{
                      background: "rgba(15, 23, 42, 0.95)",
                      backdropFilter: "blur(40px)",
                      WebkitBackdropFilter: "blur(40px)",
                      WebkitTransform: "translate3d(0, 0, 0)",
                      transform: "translate3d(0, 0, 0)",
                      WebkitBackfaceVisibility: "hidden",
                      backfaceVisibility: "hidden",
                      border: "1px solid rgba(255, 255, 255, 0.25)",
                      boxShadow: "0 12px 40px 0 rgba(0, 0, 0, 0.3)",
                      color: "white"
                    }}
                  >
                  {filteredResults.length > 0 ? ("""
h_drop_new = """                  >
                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0" style={{
                      background: "rgba(15, 23, 42, 0.95)",
                      backdropFilter: "blur(40px)",
                      WebkitBackdropFilter: "blur(40px)",
                      WebkitTransform: "translate3d(0, 0, 0)",
                      transform: "translate3d(0, 0, 0)",
                      WebkitBackfaceVisibility: "hidden",
                      backfaceVisibility: "hidden",
                      border: "1px solid rgba(255, 255, 255, 0.25)",
                      boxShadow: "0 12px 40px 0 rgba(0, 0, 0, 0.3)",
                    }} />
                    <div className="relative z-10 w-full h-full text-white">
                  {filteredResults.length > 0 ? ("""

h_drop_end_old = """                    </div>
                  )}
                  </div>
                </motion.div>"""
h_drop_end_new = """                    </div>
                  )}
                  </div>
                  </div>
                </motion.div>"""

process_file(hero, [
    (h_search_old, h_search_new),
    (h_search_end_old, h_search_end_new),
    (h_drop_old, h_drop_new),
    (h_drop_end_old, h_drop_end_new)
])


# ================= FAQSection.tsx =================
faq = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"

# FAQ FORM
f_form_old = """              <form onSubmit={handleAsk} className="p-6 rounded-[24px] overflow-hidden" style={{ 
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
f_form_new = """              <form onSubmit={handleAsk} className="relative rounded-[24px]">
                <div className="absolute inset-0 rounded-[24px] pointer-events-none z-0" style={{ 
                  background: "rgba(255, 255, 255, 0.12)", 
                  backdropFilter: "blur(12px)", 
                  WebkitBackdropFilter: "blur(12px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                  border: `1px solid rgba(255, 255, 255, 0.2)`,
                  boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                }} />
                <div className="relative z-10 p-6 rounded-[24px] overflow-hidden w-full h-full">"""
f_form_end_old = """                {errorMsg && <div className="mt-2 text-red-500 text-sm font-semibold">{errorMsg}</div>}
              </form>"""
f_form_end_new = """                {errorMsg && <div className="mt-2 text-red-500 text-sm font-semibold">{errorMsg}</div>}
                </div>
              </form>"""

# FAQ ITEM
f_item_old = """                className="rounded-[24px] overflow-hidden transition-all duration-150 relative group"
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
f_item_new = """                className="rounded-[24px] relative group"
              >
                <div className="absolute inset-0 rounded-[24px] pointer-events-none z-0 transition-all duration-150" style={{ 
                  background: "rgba(255, 255, 255, 0.12)", 
                  backdropFilter: "blur(12px)",
                  WebkitBackdropFilter: "blur(12px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                  border: isOpen ? `1px solid rgba(22, 207, 131, 0.4)` : `1px solid rgba(255, 255, 255, 0.2)`,
                  boxShadow: isOpen ? `0 8px 32px 0 rgba(22, 207, 131, 0.25)` : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                }} />
                <div className="relative z-10 w-full rounded-[24px] overflow-hidden">"""
f_item_end_old = """                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.div>"""
f_item_end_new = """                    </motion.div>
                  )}
                </AnimatePresence>
                </div>
              </motion.div>"""

# FAQ MODAL WRAPPER
f_modal_old = """              className="w-full max-w-3xl max-h-[85vh] rounded-3xl p-6 sm:p-8 flex flex-col gap-5 border shadow-2xl overflow-hidden relative"
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
f_modal_new = """              className="w-full max-w-3xl max-h-[85vh] rounded-3xl relative shadow-2xl"
            >
              <div className="absolute inset-0 rounded-3xl pointer-events-none z-0" style={{
                background: "rgba(30, 30, 40, 0.6)",
                backdropFilter: "blur(24px)",
                WebkitBackdropFilter: "blur(24px)",
                WebkitTransform: "translate3d(0, 0, 0)",
                transform: "translate3d(0, 0, 0)",
                WebkitBackfaceVisibility: "hidden",
                backfaceVisibility: "hidden",
                border: "1px solid rgba(255, 255, 255, 0.15)",
                boxShadow: "0 20px 50px -10px rgba(0, 0, 0, 0.85)"
              }} />
              <div className="relative z-10 p-6 sm:p-8 flex flex-col gap-5 rounded-3xl overflow-hidden w-full max-h-full">"""
f_modal_end_old = """              </div>
            </motion.div>
          </motion.div>
        )}"""
f_modal_end_new = """              </div>
              </div>
            </motion.div>
          </motion.div>
        )}"""

# FAQ MODAL ITEM
f_mod_item_old = """                      <div
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
f_mod_item_new = """                      <div
                        key={faq.id}
                        className="rounded-2xl relative transition-all duration-150"
                      >
                        <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-150" style={{
                          background: "rgba(255, 255, 255, 0.05)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          WebkitTransform: "translate3d(0, 0, 0)",
                          transform: "translate3d(0, 0, 0)",
                          WebkitBackfaceVisibility: "hidden",
                          backfaceVisibility: "hidden",
                          border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.1)",
                          boxShadow: isOpen ? "0 4px 20px -5px rgba(22, 207, 131, 0.25)" : "none"
                        }} />
                        <div className="relative z-10 rounded-2xl overflow-hidden w-full">"""
f_mod_item_end_old = """                            </motion.div>
                          )}
                        </AnimatePresence>
                      </div>"""
f_mod_item_end_new = """                            </motion.div>
                          )}
                        </AnimatePresence>
                        </div>
                      </div>"""

process_file(faq, [
    (f_form_old, f_form_new),
    (f_form_end_old, f_form_end_new),
    (f_item_old, f_item_new),
    (f_item_end_old, f_item_end_new),
    (f_modal_old, f_modal_new),
    (f_modal_end_old, f_modal_end_new),
    (f_mod_item_old, f_mod_item_new),
    (f_mod_item_end_old, f_mod_item_end_new),
])

