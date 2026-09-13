import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

old_sidebar = """<div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] transition-all duration-700 h-full overflow-hidden backdrop-blur-[12px]"
          style={{ background: "rgba(255, 255, 255, 0.03)", backdropFilter: "blur(12px)", WebkitBackdropFilter: "blur(12px)", border: "1px solid rgba(255, 255, 255, 0.1)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)" }}
        >"""
new_sidebar = """<div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.08)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.15)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""

old_main = """<div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] transition-all duration-700 h-full overflow-hidden backdrop-blur-[12px]"
          style={{ background: "rgba(255, 255, 255, 0.03)", backdropFilter: "blur(12px)", WebkitBackdropFilter: "blur(12px)", border: "1px solid rgba(255, 255, 255, 0.1)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)" }}
        >"""
new_main = """<div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.08)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.15)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""

content = content.replace(old_sidebar, new_sidebar)
content = content.replace(old_main, new_main)

with open(file_path, "w") as f:
    f.write(content)
print("Updated Hero blur opacity")
