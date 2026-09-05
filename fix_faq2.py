import re

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "r") as f:
    content = f.read()

# 3. All FAQs Modal Wrapper
old_modal = """              className="w-full max-w-3xl max-h-[85vh] rounded-3xl p-6 sm:p-8 flex flex-col gap-5 border shadow-2xl overflow-hidden relative"
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
new_modal = """              className="w-full max-w-3xl max-h-[85vh] rounded-3xl p-6 sm:p-8 flex flex-col gap-5 border shadow-2xl relative"
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
content = content.replace(old_modal, new_modal)

# Close Modal Wrapper
end_modal = """              </div>
            </motion.div>
          </motion.div>
        )}"""
new_end_modal = """              </div>
              </div>
            </motion.div>
          </motion.div>
        )}"""
content = content.replace(end_modal, new_end_modal)

# 4. Modal Item
old_modal_item = """                      <div
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
new_modal_item = """                      <div
                        key={faq.id}
                        className="rounded-2xl transition-all duration-150 relative border"
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
content = content.replace(old_modal_item, new_modal_item)

# Close Modal Item
end_modal_item = """                            </motion.div>
                          )}
                        </AnimatePresence>
                      </div>"""
new_end_modal_item = """                            </motion.div>
                          )}
                        </AnimatePresence>
                        </div>
                      </div>"""
content = content.replace(end_modal_item, new_end_modal_item)

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "w") as f:
    f.write(content)

