import re

file_path = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Find the viewport={{ once: true, amount: 0.2 }}
# It might be making the item only show up when 20% in view, which feels "late".
content = content.replace('viewport={{ once: true, amount: 0.2 }}', 'viewport={{ once: true, amount: 0.1 }}')

with open(file_path, "w") as f:
    f.write(content)
print("Updated FAQSection")
