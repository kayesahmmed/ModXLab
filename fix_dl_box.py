import re

def update_file(path, old, new):
    with open(path, "r") as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(path, "w") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Failed to find target in {path}")

# DOWNLOAD SECTION
download_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"

# 1. Main download file box
old_dl_1 = """                        className="flex flex-col justify-between gap-4 p-5 sm:p-6 rounded-[18px] transition-all duration-300 overflow-hidden group" 
                        style={{ 
                          background: "rgba(255, 255, 255, 0.05)",
                          backdropFilter: "blur(20px)",
                          WebkitBackdropFilter: "blur(20px)",
                          border: "1px solid rgba(255, 255, 255, 0.15)",
                          boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.25)"
                        }}"""

new_dl_1 = """                        className="flex flex-col justify-between gap-4 p-5 sm:p-6 rounded-[18px] transition-all duration-300 overflow-hidden group" 
                        style={{ 
                          background: "rgba(255, 255, 255, 0.12)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          border: "1px solid rgba(255, 255, 255, 0.2)",
                          boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                        }}"""
update_file(download_path, old_dl_1, new_dl_1)

# 2. How to Use expanded wrapper
old_dl_2 = """                            className="mt-3 p-5 sm:p-6 rounded-[24px] flex flex-col gap-4 relative overflow-hidden transition-all duration-300"
                            style={{
                              background: "rgba(255, 255, 255, 0.05)",
                              backdropFilter: "blur(24px)",
                              WebkitBackdropFilter: "blur(24px)",
                              border: "1px solid rgba(255, 255, 255, 0.15)",
                              boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.25)"
                            }}"""

new_dl_2 = """                            className="mt-3 p-5 sm:p-6 rounded-[24px] flex flex-col gap-4 relative overflow-hidden transition-all duration-300"
                            style={{
                              background: "rgba(255, 255, 255, 0.12)",
                              backdropFilter: "blur(12px)",
                              WebkitBackdropFilter: "blur(12px)",
                              border: "1px solid rgba(255, 255, 255, 0.2)",
                              boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                            }}"""
update_file(download_path, old_dl_2, new_dl_2)


# 3. How to Use Arrow Color Change Fix
old_arrow = """                        <motion.div 
                          animate={{
                            rotate: isHowToUseOpen ? 180 : 0,
                            backgroundColor: isHowToUseOpen ? "#ffffff" : "rgba(255,255,255,0.15)",
                            color: isHowToUseOpen ? "#0f0c20" : "#ffffff",
                            boxShadow: isHowToUseOpen ? "0 0 15px rgba(255,255,255,0.4)" : "0 0 0px transparent"
                          }}"""

new_arrow = """                        <motion.div 
                          animate={{
                            rotate: isHowToUseOpen ? 180 : 0,
                            backgroundColor: "rgba(255,255,255,0.15)",
                            color: "#ffffff",
                            boxShadow: "0 0 0px transparent"
                          }}"""
update_file(download_path, old_arrow, new_arrow)

