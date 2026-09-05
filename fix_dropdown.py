import re

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

# find the dropdown wrapper
old_dropdown = """              {/* Suggestions / Results Dropdown */}
                {searchOpen && showSuggestions && searchVal.trim().length > 0 && (
                  <motion.div"""

new_dropdown = """              {/* Suggestions / Results Dropdown */}
              <AnimatePresence>
                {searchOpen && showSuggestions && searchVal.trim().length > 0 && (
                  <motion.div
                    key="search-dropdown"
                    initial={{ opacity: 0, y: -10, scale: 0.98 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -5, scale: 0.98 }}
                    transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
                    className="absolute top-[68px] right-0 w-80 sm:w-96 md:w-[420px] rounded-2xl p-2 z-[9999]"
"""

# Now we need to replace the exact text
old_regex = r"\{\/\* Suggestions \/ Results Dropdown \*\/}.*?className=\"absolute top-\[68px\] right-0 w-80 sm:w-96 md:w-\[420px\] rounded-2xl p-2 z-\[9999\]\""
content = re.sub(old_regex, new_dropdown.strip(), content, flags=re.DOTALL)

# Add closing AnimatePresence
old_close = """                    <div className="p-4 text-center flex items-center justify-center gap-2 text-xs font-semibold text-white/90">
                      <span>🔍</span>
                      <span>No items match "{searchVal}"</span>
                    </div>
                  )}
                </motion.div>
              )}
            </div>"""

new_close = """                    <div className="p-4 text-center flex items-center justify-center gap-2 text-xs font-semibold text-white/90">
                      <span>🔍</span>
                      <span>No items match "{searchVal}"</span>
                    </div>
                  )}
                </motion.div>
              )}
              </AnimatePresence>
            </div>"""

if old_close in content:
    content = content.replace(old_close, new_close)

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)
