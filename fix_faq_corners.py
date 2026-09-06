import re

def replace_in_file(path, old, new):
    with open(path, "r") as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(path, "w") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Failed to find target in {path}")

faq_path = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"

old_main = """                <div 
                  className="absolute inset-0 z-0 transition-all duration-300 pointer-events-none"
                  style={{"""

new_main = """                <div 
                  className="absolute inset-0 z-0 transition-all duration-300 pointer-events-none rounded-[24px]"
                  style={{"""
replace_in_file(faq_path, old_main, new_main)

old_search = """                        <div 
                          className="absolute inset-0 z-0 transition-all duration-300 pointer-events-none"
                          style={{"""

new_search = """                        <div 
                          className="absolute inset-0 z-0 transition-all duration-300 pointer-events-none rounded-[18px]"
                          style={{"""
replace_in_file(faq_path, old_search, new_search)

