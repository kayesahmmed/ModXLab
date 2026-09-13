import re

file_path = "./artifacts/cinematic-scroll-site/index.html"
with open(file_path, "r") as f:
    content = f.read()

# Add SEO Keywords for "ModX", "ModX Lab", "modx"
keywords_tag = '<meta name="keywords" content="ModX, ModX Lab, modx, modx lab, Free Fire Mod Panel, ModX Lab Official, Shizuku, Anti-Ban Panel, ModX APK Download" />'

# Insert it right after description
if 'name="keywords"' not in content:
    content = content.replace('content="The official website of the ModX Lab YouTube Channel. Access our exclusive video tutorial resources, premium apps, and files. Join our community to ask questions, explore features, and share your valuable reviews!"\n    />', 
                              'content="The official website of the ModX Lab YouTube Channel. Access our exclusive video tutorial resources, premium apps, and files. Join our community to ask questions, explore features, and share your valuable reviews!"\n    />\n    ' + keywords_tag)

with open(file_path, "w") as f:
    f.write(content)
print("Updated index.html SEO tags")
