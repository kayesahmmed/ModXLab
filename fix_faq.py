import re

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "r") as f:
    content = f.read()

# 1. Form
old_form = """              <form onSubmit={handleAsk} className="p-6 rounded-[24px]" style={{ 
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
              
new_form = """              <form onSubmit={handleAsk} className="p-6 rounded-[24px] relative" style={{ 
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
content = content.replace(old_form, new_form)
# I also need to close the extra div for the form.
# The end of the form is:
#                 {errorMsg && <div className="mt-2 text-red-500 text-sm font-semibold">{errorMsg}</div>}
#               </form>
end_form = """                {errorMsg && <div className="mt-2 text-red-500 text-sm font-semibold">{errorMsg}</div>}
              </form>"""
new_end_form = """                {errorMsg && <div className="mt-2 text-red-500 text-sm font-semibold">{errorMsg}</div>}
                </div>
              </form>"""
content = content.replace(end_form, new_end_form)

# 2. FAQ motion.div
old_faq_item = """                className="rounded-[24px] overflow-hidden transition-all duration-150 relative group"
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
new_faq_item = """                className="rounded-[24px] transition-all duration-150 relative group"
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
content = content.replace(old_faq_item, new_faq_item)

# Closing for FAQ item
end_faq = """                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.div>"""
new_end_faq = """                    </motion.div>
                  )}
                </AnimatePresence>
                </div>
              </motion.div>"""
content = content.replace(end_faq, new_end_faq)

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "w") as f:
    f.write(content)

