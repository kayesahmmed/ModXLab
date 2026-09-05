import re

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

# Fix duplicates in HeroSection.tsx
content = re.sub(r'transform:\s*"translateZ\(0\)"\n', '', content)

# My previous script replaced willChange with:
# willChange: "transform, opacity",
# WebkitTransform: "translate3d(0,0,0)",
# transform: "translate3d(0,0,0)",
# backfaceVisibility: "hidden",
# WebkitBackfaceVisibility: "hidden"

# And my previous script also replaced WebkitBackdropFilter with:
# WebkitBackdropFilter: "blur(40px)",
# WebkitTransform: "translate3d(0, 0, 0)",
# transform: "translate3d(0, 0, 0)",
# WebkitBackfaceVisibility: "hidden",
# backfaceVisibility: "hidden",

# So I got duplicates for transform, WebkitTransform, backfaceVisibility, WebkitBackfaceVisibility!
# Let's clean that up.
block_to_remove = """                    WebkitTransform: "translate3d(0,0,0)",
                    transform: "translate3d(0,0,0)",
                    backfaceVisibility: "hidden",
                    WebkitBackfaceVisibility: "hidden" """

content = content.replace(',\n' + block_to_remove, '')
content = content.replace(block_to_remove, '')

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)

