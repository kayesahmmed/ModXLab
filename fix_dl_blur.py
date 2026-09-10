import re

dl_file = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"
with open(dl_file, "r") as f:
    content = f.read()

# Remove willChange from parent
content = content.replace('style={{ willChange: "transform, opacity", z: 0 }}', 'style={{ z: 0 }}')

# Remove whileHover from the card to prevent dynamic stacking context bugs in Chrome
content = content.replace('whileHover={{ y: -4, scale: 1.01 }}', '')

with open(dl_file, "w") as f:
    f.write(content)
print("Fixed DownloadSection blur")
