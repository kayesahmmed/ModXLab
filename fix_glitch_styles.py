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

# FAQ SECTION
faq_path = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"

old_faq_1 = """                className="rounded-[24px] relative group overflow-hidden transition-all duration-300"
                style={{ 
                  willChange: 'transform, opacity', 
                  WebkitBackfaceVisibility: 'hidden', 
                  backfaceVisibility: 'hidden',
                  background: "rgba(255, 255, 255, 0.12)",
                  backdropFilter: "blur(12px)",
                  WebkitBackdropFilter: "blur(12px)",
                  border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.2)",
                  boxShadow: isOpen ? "0 8px 32px 0 rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                  transform: "translateZ(0)"
                }}"""

new_faq_1 = """                className="rounded-[24px] relative group overflow-hidden transition-all duration-300"
                style={{ 
                  background: "rgba(255, 255, 255, 0.05)",
                  backdropFilter: "blur(16px)",
                  WebkitBackdropFilter: "blur(16px)",
                  border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.15)",
                  boxShadow: isOpen ? "0 8px 32px 0 rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                }}"""
update_file(faq_path, old_faq_1, new_faq_1)

old_faq_2 = """                        className="rounded-[18px] relative transition-all duration-300 overflow-hidden"
                        style={{ 
                          willChange: 'transform, opacity', 
                          WebkitBackfaceVisibility: 'hidden', 
                          backfaceVisibility: 'hidden',
                          background: "rgba(255, 255, 255, 0.12)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.2)",
                          boxShadow: isOpen ? "0 4px 20px -5px rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                          transform: "translateZ(0)"
                        }}"""

new_faq_2 = """                        className="rounded-[18px] relative transition-all duration-300 overflow-hidden"
                        style={{ 
                          background: "rgba(255, 255, 255, 0.05)",
                          backdropFilter: "blur(16px)",
                          WebkitBackdropFilter: "blur(16px)",
                          border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.15)",
                          boxShadow: isOpen ? "0 4px 20px -5px rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                        }}"""
update_file(faq_path, old_faq_2, new_faq_2)


# DOWNLOAD SECTION
download_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"

old_dl_1 = """                        className="flex flex-col justify-between gap-4 p-5 sm:p-6 rounded-[18px] transition-all duration-300 overflow-hidden group" 
                        style={{ 
                          background: "rgba(255, 255, 255, 0.12)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          border: "1px solid rgba(255, 255, 255, 0.2)",
                          boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                          transform: "translateZ(0)"
                        }}"""

new_dl_1 = """                        className="flex flex-col justify-between gap-4 p-5 sm:p-6 rounded-[18px] transition-all duration-300 overflow-hidden group" 
                        style={{ 
                          background: "rgba(255, 255, 255, 0.05)",
                          backdropFilter: "blur(20px)",
                          WebkitBackdropFilter: "blur(20px)",
                          border: "1px solid rgba(255, 255, 255, 0.15)",
                          boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.25)"
                        }}"""
update_file(download_path, old_dl_1, new_dl_1)

old_dl_2 = """                            className="mt-3 p-5 sm:p-6 rounded-[24px] flex flex-col gap-4 relative overflow-hidden transition-all duration-300"
                            style={{
                              background: "rgba(255, 255, 255, 0.12)",
                              backdropFilter: "blur(12px)",
                              WebkitBackdropFilter: "blur(12px)",
                              border: "1px solid rgba(255, 255, 255, 0.2)",
                              boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                              transform: "translateZ(0)"
                            }}"""

new_dl_2 = """                            className="mt-3 p-5 sm:p-6 rounded-[24px] flex flex-col gap-4 relative overflow-hidden transition-all duration-300"
                            style={{
                              background: "rgba(255, 255, 255, 0.05)",
                              backdropFilter: "blur(24px)",
                              WebkitBackdropFilter: "blur(24px)",
                              border: "1px solid rgba(255, 255, 255, 0.15)",
                              boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.25)"
                            }}"""
update_file(download_path, old_dl_2, new_dl_2)

old_dl_3 = """                                    className="p-4 sm:p-5 rounded-[18px] flex flex-col gap-2.5 relative overflow-hidden transition-all duration-300 hover:translate-y-[-2px]"
                                    style={{
                                      background: "rgba(255, 255, 255, 0.12)",
                                      backdropFilter: "blur(12px)",
                                      WebkitBackdropFilter: "blur(12px)",
                                      border: "1px solid rgba(255, 255, 255, 0.2)",
                                      boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                                      transform: "translateZ(0)"
                                    }}"""

new_dl_3 = """                                    className="p-4 sm:p-5 rounded-[18px] flex flex-col gap-2.5 relative overflow-hidden transition-all duration-300 hover:translate-y-[-2px]"
                                    style={{
                                      background: "rgba(255, 255, 255, 0.03)",
                                      backdropFilter: "blur(12px)",
                                      WebkitBackdropFilter: "blur(12px)",
                                      border: "1px solid rgba(255, 255, 255, 0.1)",
                                      boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                                    }}"""
update_file(download_path, old_dl_3, new_dl_3)

