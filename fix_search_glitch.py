import re

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

# 3. Add <AnimatePresence> wrapper correctly
old_block = """              {/* Suggestions / Results Dropdown */}
              {searchOpen && showSuggestions && searchVal.trim().length > 0 && ("""

new_block = """              {/* Suggestions / Results Dropdown */}
              <AnimatePresence>
              {searchOpen && showSuggestions && searchVal.trim().length > 0 && ("""
content = content.replace(old_block, new_block)

old_end = """                    <div className="p-4 text-center flex items-center justify-center gap-2 text-xs font-semibold text-white/90">
                      <span>🔍</span>
                      <span>No items match "{searchVal}"</span>
                    </div>
                  )}
                </motion.div>
              )}
            </div>"""

new_end = """                    <div className="p-4 text-center flex items-center justify-center gap-2 text-xs font-semibold text-white/90">
                      <span>🔍</span>
                      <span>No items match "{searchVal}"</span>
                    </div>
                  )}
                </motion.div>
              )}
              </AnimatePresence>
            </div>"""
content = content.replace(old_end, new_end)

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)

