with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

content = content.replace("              )}", "              )}\n              </AnimatePresence>")

# Now wait! The replacement string "              )}" might appear multiple times.
# Let's just fix it at the specific line.
