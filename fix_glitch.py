import re
import os

files_to_fix = [
    "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx",
    "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"
]

def add_gpu_acceleration(content):
    # Find all style={{ ... backdropFilter: "..." ... }} blocks
    # and inject transform properties to force GPU composite layer
    
    # We will just do a regex replace to add the properties after WebkitBackdropFilter
    pattern = r'(WebkitBackdropFilter:\s*"[^"]*",?)'
    replacement = r'\1\n                  WebkitTransform: "translate3d(0, 0, 0)",\n                  transform: "translate3d(0, 0, 0)",\n                  WebkitBackfaceVisibility: "hidden",\n                  backfaceVisibility: "hidden",'
    
    new_content = re.sub(pattern, replacement, content)
    
    # Also fix willChange string in HeroSection if present
    new_content = new_content.replace('willChange: "transform, opacity"', 'willChange: "transform, opacity",\n                    WebkitTransform: "translate3d(0,0,0)",\n                    transform: "translate3d(0,0,0)",\n                    backfaceVisibility: "hidden",\n                    WebkitBackfaceVisibility: "hidden"')
    
    return new_content

for file_path in files_to_fix:
    with open(file_path, "r") as f:
        content = f.read()
    
    content = add_gpu_acceleration(content)
    
    # In FAQSection, the AnimatePresence for the answer opening could be the culprit too.
    # When AnimatePresence animates height, it repaints. 
    # Let's make sure the dropdowns and answers have overflow: hidden which they do.
    
    with open(file_path, "w") as f:
        f.write(content)

