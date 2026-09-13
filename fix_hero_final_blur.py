import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Left Column (Sidebar)
old_sidebar = """<motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.08)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.15)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)", transform: "translateZ(0)", willChange: "transform, opacity" }}
        >"""
new_sidebar = """<motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: isDark ? "rgba(20, 20, 25, 0.3)" : "rgba(255, 255, 255, 0.15)", backdropFilter: "blur(24px)", WebkitBackdropFilter: "blur(24px)", border: isDark ? "1px solid rgba(255, 255, 255, 0.1)" : "1px solid rgba(255, 255, 255, 0.4)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""

# Right Column (Hub)
old_main = """<motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.08)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.15)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)", transform: "translateZ(0)", willChange: "transform, opacity" }}
        >"""
new_main = """<motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: isDark ? "rgba(20, 20, 25, 0.3)" : "rgba(255, 255, 255, 0.15)", backdropFilter: "blur(24px)", WebkitBackdropFilter: "blur(24px)", border: isDark ? "1px solid rgba(255, 255, 255, 0.1)" : "1px solid rgba(255, 255, 255, 0.4)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""

content = content.replace(old_sidebar, new_sidebar)
content = content.replace(old_main, new_main)

# Remove bg-transparent from the wrapper grid
content = content.replace("bg-transparent", "")

with open(file_path, "w") as f:
    f.write(content)
print("Updated Hero blur styles")
