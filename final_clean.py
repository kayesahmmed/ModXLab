import re

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

bad_block = """                    WebkitTransform: "translate3d(0,0,0)",
                    transform: "translate3d(0,0,0)",
                    backfaceVisibility: "hidden",
                    WebkitBackfaceVisibility: "hidden"
                  }"""

content = content.replace(bad_block, "                  }")

bad_block2 = """                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                    border: "1px solid rgba(255, 255, 255, 0.25)",
                    boxShadow: "0 12px 40px 0 rgba(0, 0, 0, 0.3)",
                    color: "white",
                    willChange: "transform, opacity",
                    WebkitTransform: "translate3d(0,0,0)",
                    transform: "translate3d(0,0,0)",
                    backfaceVisibility: "hidden",
                    WebkitBackfaceVisibility: "hidden"
                  }}"""

replacement2 = """                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                    border: "1px solid rgba(255, 255, 255, 0.25)",
                    boxShadow: "0 12px 40px 0 rgba(0, 0, 0, 0.3)",
                    color: "white",
                    willChange: "transform, opacity"
                  }}"""
                  
content = content.replace(bad_block2, replacement2)

# Just run a global regex to remove the duplicate block after willChange if it exists
content = re.sub(r'willChange:\s*"transform, opacity",\s*WebkitTransform:\s*"translate3d\(0,0,0\)",\s*transform:\s*"translate3d\(0,0,0\)",\s*backfaceVisibility:\s*"hidden",\s*WebkitBackfaceVisibility:\s*"hidden"', 'willChange: "transform, opacity"', content)

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)
