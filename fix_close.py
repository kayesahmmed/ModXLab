with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

bad = """                  )}
              
                </motion.div>
              )}"""

good = """                  )}
                  </div>
                </motion.div>
              )}"""

content = content.replace(bad, good)

# In my script I had:
#     end_dropdown_regex = r'(                  \)\}\n                <\/motion\.div>)'
#     content = re.sub(end_dropdown_regex, r'                  )}\n                    </div>\n                </motion.div>', content)
# But it failed because of the extra spaces or empty lines.

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)
