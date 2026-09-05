with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

bad = """            </motion.button>

            {/* Ultra-Premium Glassmorphic Search Bar */}"""

good = """            </motion.button>
          </motion.div>

            {/* Ultra-Premium Glassmorphic Search Bar */}"""

content = content.replace(bad, good)
with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)
