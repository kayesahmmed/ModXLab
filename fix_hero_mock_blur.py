import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Left Column (Sidebar)
old_sidebar = """<div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.05)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.1)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)" }}
        >"""
new_sidebar = """<div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: isDark ? "rgba(10, 15, 30, 0.4)" : "rgba(255, 255, 255, 0.2)", backdropFilter: "blur(24px)", WebkitBackdropFilter: "blur(24px)", border: isDark ? "1px solid rgba(255, 255, 255, 0.1)" : "1px solid rgba(255, 255, 255, 0.4)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""

# Right Column (Hub)
old_main = """<div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.05)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.1)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)" }}
        >"""
new_main = """<div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: isDark ? "rgba(10, 15, 30, 0.4)" : "rgba(255, 255, 255, 0.2)", backdropFilter: "blur(24px)", WebkitBackdropFilter: "blur(24px)", border: isDark ? "1px solid rgba(255, 255, 255, 0.1)" : "1px solid rgba(255, 255, 255, 0.4)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""

content = content.replace(old_sidebar, new_sidebar)
content = content.replace(old_main, new_main)

with open(file_path, "w") as f:
    f.write(content)
print("Updated Hero blur to be darker and more blurred")
