import re

file_path = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"

with open(file_path, "r") as f:
    content = f.read()

# Replace the mb-6 with mb-14
old_buttons = """        <div className="flex flex-col items-center gap-4 mb-6">"""
new_buttons = """        <div className="flex flex-col items-center gap-4 mb-14">"""
content = content.replace(old_buttons, new_buttons)

with open(file_path, "w") as f:
    f.write(content)

