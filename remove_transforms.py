import re

files = [
    "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx",
    "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"
]

for file in files:
    with open(file, "r") as f:
        content = f.read()

    # regex to remove the problematic lines
    content = re.sub(r'\s*WebkitTransform:\s*"translate3d\(0,\s*0,\s*0\)",', '', content)
    content = re.sub(r'\s*transform:\s*"translate3d\(0,\s*0,\s*0\)",', '', content)
    content = re.sub(r'\s*WebkitBackfaceVisibility:\s*"hidden",', '', content)
    content = re.sub(r'\s*backfaceVisibility:\s*"hidden",', '', content)

    # I'll also remove the inline transition if it's there on the backdrop
    # Let's write it back
    with open(file, "w") as f:
        f.write(content)

