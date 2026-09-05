import re

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

# 1. Input Container
search_bar_old = """              <div
                className={`transition-all duration-350 ease-[cubic-bezier(0.16,1,0.3,1)] h-14 flex items-center rounded-2xl border relative ${
                  searchOpen ? "w-[260px] sm:w-[320px] opacity-100 border-white/20 pointer-events-auto" : "w-0 opacity-0 border-transparent pointer-events-none"
                }`}
                style={{
                  boxShadow: "0 8px 32px 0 rgba(0,0,0,0.15)"
                }}
              >
                <div 
                  className="absolute inset-0 rounded-2xl pointer-events-none" 
                  style={{
                    background: "rgba(255, 255, 255, 0.18)",
                    backdropFilter: "blur(16px)",
                    WebkitBackdropFilter: "blur(16px)",
                    WebkitTransform: "translate3d(0,0,0)",
                    transform: "translate3d(0,0,0)",
                    backfaceVisibility: "hidden",
                    WebkitBackfaceVisibility: "hidden"
                  }} 
                />
                <div className="relative w-full h-full flex items-center z-10 overflow-hidden rounded-2xl">"""

search_bar_new = """              <div
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
content = content.replace(search_bar_old, search_bar_new)

# Find the end of the input section which we added an extra `</div>` for
# Currently it is:
#                     <div className="p-4 text-center flex items-center justify-center gap-2 text-xs font-semibold text-white/90">
#                       <span>🔍</span>
#                       <span>No items match "{searchVal}"</span>
#                     </div>
#                   )}
#                   </div>
#                 </motion.div>
#               )}
#               </AnimatePresence>
#             </div>
end_input_old = """                    </div>
                  )}
                  </div>
                </motion.div>
              )}
              </AnimatePresence>
            </div>
          </motion.div>
        </motion.div>"""
end_input_new = """                    </div>
                  )}
                </motion.div>
              )}
              </AnimatePresence>
            </div>
          </motion.div>
        </motion.div>"""
content = content.replace(end_input_old, end_input_new)

# Dropdown Layer
dropdown_old = """                  >
                    <div 
                      className="absolute inset-0 rounded-2xl pointer-events-none" 
                      style={{
                        background: "rgba(15, 23, 42, 0.95)",
                        backdropFilter: "blur(40px)",
                        WebkitBackdropFilter: "blur(40px)",
                        WebkitTransform: "translate3d(0,0,0)",
                        transform: "translate3d(0,0,0)",
                        backfaceVisibility: "hidden",
                        WebkitBackfaceVisibility: "hidden"
                      }} 
                    />
                    <div className="relative w-full h-full p-2 z-10">"""

dropdown_new = """                  >"""

# We need to add the backdropFilter back to the dropdown's style.
dropdown_style_old = """                    style={{
                      border: "1px solid rgba(255, 255, 255, 0.25)",
                      boxShadow: "0 12px 40px 0 rgba(0, 0, 0, 0.3)",
                      color: "white"
                    }}"""
dropdown_style_new = """                    style={{
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
                    }}"""
content = content.replace(dropdown_style_old, dropdown_style_new)
content = content.replace(dropdown_old, dropdown_new)


with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)

