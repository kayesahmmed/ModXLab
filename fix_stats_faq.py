import re

# 1. Fix MarqueeSection Stats blur (remove willChange)
stats_file = "./artifacts/cinematic-scroll-site/src/components/MarqueeSection.tsx"
with open(stats_file, "r") as f:
    stats_content = f.read()

stats_content = stats_content.replace('willChange: "transform, opacity"', '')
with open(stats_file, "w") as f:
    f.write(stats_content)
print("Fixed StatsSection blur")

# 2. Fix FAQ Section stroke color
faq_file = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"
with open(faq_file, "r") as f:
    faq_content = f.read()

faq_content = faq_content.replace('"1px solid rgba(255, 255, 255, 0.3)"', '"1px solid rgba(255, 255, 255, 0.15)"')
with open(faq_file, "w") as f:
    f.write(faq_content)
print("Fixed FAQ stroke color")
