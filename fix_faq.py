import re

file_path = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# 1. Restore the blur timing (amount: 0.2)
content = content.replace('viewport={{ once: true, amount: 0.1 }}', 'viewport={{ once: true, amount: 0.2 }}')

# 2. Increase the default white stroke visibility for FAQ boxes
content = content.replace('"1px solid rgba(255, 255, 255, 0.15)"', '"1px solid rgba(255, 255, 255, 0.3)"')

with open(file_path, "w") as f:
    f.write(content)
print("Updated FAQSection")
