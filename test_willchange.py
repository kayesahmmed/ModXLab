import re

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

content = content.replace('willChange: "transform, opacity"', '')
content = content.replace('willChange: "transform"', '')

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "r") as f:
    content = f.read()

content = content.replace('willChange: "transform, opacity"', '')
content = content.replace('willChange: "transform"', '')

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "w") as f:
    f.write(content)

