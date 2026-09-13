import re

file_path = "./artifacts/cinematic-scroll-site/index.html"
with open(file_path, "r") as f:
    content = f.read()

# Add Google Site Verification Meta Tag
verification_tag = '<meta name="google-site-verification" content="o0Bb4O8JI44uuyEF77WeMRuVlwHTFYMbPZwUw6pmjis" />'

# Insert it right after the charset meta tag
if 'name="google-site-verification"' not in content:
    content = content.replace('<meta charset="UTF-8" />', 
                              '<meta charset="UTF-8" />\n    ' + verification_tag)

with open(file_path, "w") as f:
    f.write(content)
print("Updated index.html with verification tag")
