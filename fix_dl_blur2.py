import re

file_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Fix Parent motion.div (the container)
old_parent_style = """              style={{
                background: "rgba(255, 255, 255, 0.12)",
                backdropFilter: "blur(12px)",
                WebkitBackdropFilter: "blur(12px)",
                border: "1px solid rgba(255, 255, 255, 0.2)",
                boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                
              }}"""
new_parent_style = """              style={{
                background: "rgba(255, 255, 255, 0.03)",
                backdropFilter: "blur(16px)",
                WebkitBackdropFilter: "blur(16px)",
                border: "1px solid rgba(255, 255, 255, 0.1)",
                boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
              }}"""
content = content.replace(old_parent_style, new_parent_style)

# Fix Inner file card
old_inner_style = """                        style={{ 
                          background: "rgba(255, 255, 255, 0.12)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          border: "1px solid rgba(255, 255, 255, 0.2)",
                          boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                        }}"""
new_inner_style = """                        style={{ 
                          background: "rgba(255, 255, 255, 0.08)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          border: "1px solid rgba(255, 255, 255, 0.15)",
                          boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                        }}"""
content = content.replace(old_inner_style, new_inner_style)

with open(file_path, "w") as f:
    f.write(content)
print("Fixed DownloadSection double blur")
