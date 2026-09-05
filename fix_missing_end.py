with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

bad = """              </AnimatePresence>
            </div>
          </motion.div>

        {/* Hero Mock Panel - Placed cleanly underneath with GPU acceleration */}"""

good = """              </AnimatePresence>
            </div>
          </motion.div>
        </motion.div>

        {/* Hero Mock Panel - Placed cleanly underneath with GPU acceleration */}"""

content = content.replace(bad, good)
with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)
