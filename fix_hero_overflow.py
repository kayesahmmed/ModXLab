import re

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

# I also need to restore HeroSection's search bar to native blur because otherwise it will look weird as well.
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
                  WebkitTransform: "translate3d(0,0,0)",
                  transform: "translate3d(0,0,0)",
                  backfaceVisibility: "hidden",
                  WebkitBackfaceVisibility: "hidden",
                  boxShadow: "0 8px 32px 0 rgba(0,0,0,0.15)"
                }}
              >
                <div className="relative w-full h-full flex items-center">"""
content = content.replace(search_bar_old, search_bar_new)

search_bar_end_old = """                  )}
                  </div>
                </motion.div>
              )}
              </AnimatePresence>
            </div>
          </motion.div>
        </motion.div>"""

search_bar_end_new = """                  )}
                </motion.div>
              )}
              </AnimatePresence>
            </div>
          </motion.div>
        </motion.div>"""
# Wait, actually I just need to remove the extra closing `</div>` around the dropdown?
# Wait, the extra `</div>` was for `overflow-hidden rounded-2xl` right?
# Let's check my `fix_glass.py` script:
# I had:
#                 <div className="relative w-full h-full flex items-center z-10 overflow-hidden rounded-2xl">
# The end was:
#     end_dropdown_regex = r'(                  \)\}\n                <\/motion\.div>)'
#     content = re.sub(end_dropdown_regex, r'                  )}\n                    </div>\n                </motion.div>', content)

# But wait, the dropdown `motion.div` itself was ALSO replaced with an absolute layer!
# Let's restore the dropdown motion.div as well.

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
# wait, I need to put the styles back onto the motion.div.
# Actually, I can just use a generic search and replace for the dropdown styles.
pass

