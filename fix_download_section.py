import re

file_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Fix the main Download box styling
old_dl_style = """                  className="w-full max-w-7xl mx-auto px-5 sm:px-8 lg:px-10 py-8 sm:py-10 flex flex-col gap-6 relative overflow-hidden rounded-3xl border shadow-2xl mb-8 backdrop-blur-2xl"
              style={{
                background: isDark ? "rgba(255, 255, 255, 0.08)" : "rgba(255, 255, 255, 0.85)",
                borderColor: "rgba(255, 255, 255, 0.2)",
                boxShadow: isDark
                  ? "0 20px 50px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 0 30px rgba(255, 255, 255, 0.05)"
                  : "0 20px 50px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.8)"
              }}"""

new_dl_style = """                  className="w-full max-w-7xl mx-auto px-5 sm:px-8 lg:px-10 py-8 sm:py-10 flex flex-col gap-6 relative overflow-hidden rounded-3xl mb-8"
              style={{
                background: "rgba(255, 255, 255, 0.12)",
                backdropFilter: "blur(12px)",
                WebkitBackdropFilter: "blur(12px)",
                border: "1px solid rgba(255, 255, 255, 0.2)",
                boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
              }}"""
content = content.replace(old_dl_style, new_dl_style)

# Fix How to Use button click color change
old_btn_style = """                      style={{
                        borderColor: isHowToUseOpen ? "rgba(255,255,255,0.3)" : "rgba(255,255,255,0.18)",
                        background: isHowToUseOpen ? "rgba(255,255,255,0.08)" : "rgba(255,255,255,0.03)"
                      }}"""

new_btn_style = """                      style={{
                        borderColor: "rgba(255,255,255,0.18)",
                        background: "rgba(255,255,255,0.05)",
                        backdropFilter: "blur(12px)",
                        WebkitBackdropFilter: "blur(12px)",
                      }}"""
content = content.replace(old_btn_style, new_btn_style)

with open(file_path, "w") as f:
    f.write(content)
print("Updated DownloadSection")
