import re

file_path = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Replace whileInView with animate so they render immediately on load
content = content.replace('whileInView={{ opacity: 1, y: 0 }}', 'animate={{ opacity: 1, y: 0 }}')
content = content.replace('viewport={{ once: true, amount: 0.2 }}', '')

with open(file_path, "w") as f:
    f.write(content)
print("Fixed FAQ animation")
