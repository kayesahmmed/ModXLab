import re

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

# I see my previous Python regex was too loose and duplicated transform/backfaceVisibility keys inside style objects.
# I will use a robust replacement strategy.
# Let's fix line 1228-1231 in HeroSection.tsx
duplicate_block = """
                    WebkitTransform: "translate3d(0,0,0)",
                    transform: "translate3d(0,0,0)",
                    backfaceVisibility: "hidden",
                    WebkitBackfaceVisibility: "hidden" """

# Also remove trailing commas followed by this block
content = content.replace(',\n' + duplicate_block, '')
content = content.replace(duplicate_block, '')
content = content.replace(',                    WebkitTransform: "translate3d(0,0,0)",\n                    transform: "translate3d(0,0,0)",\n                    backfaceVisibility: "hidden",\n                    WebkitBackfaceVisibility: "hidden"', '')

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)

