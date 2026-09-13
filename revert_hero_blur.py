import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Re-add rotateXPanel
content = content.replace(
    "const opacityPanel = useTransform(scrollYProgress, [0, 0.85, 1], [1, 1, 0.6]);",
    "const opacityPanel = useTransform(scrollYProgress, [0, 0.85, 1], [1, 1, 0.6]);\n  const rotateXPanel = useTransform(scrollYProgress, [0, 1], [0, 6]);"
)

# Re-add 3D transform on the parent motion.div
old_parent = """        <motion.div
          initial={{ opacity: 0, scale: 0.96, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          
          transition={{ duration: 0.6, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
          className="w-full max-w-[960px] z-10 relative mt-16 sm:mt-24 lg:mt-28"
        >"""
new_parent = """        <motion.div
          initial={{ opacity: 0, scale: 0.96, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          style={{ y: yPanel, scale: scalePanel, opacity: opacityPanel, rotateX: rotateXPanel, transformPerspective: 1200, z: 0 }}
          transition={{ duration: 0.6, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
          className="w-full max-w-[960px] z-10 relative mt-16 sm:mt-24 lg:mt-28"
        >"""
content = content.replace(old_parent, new_parent)

# Restore the exact glass style from StatsSection to the HeroMockPanel columns
old_sidebar = """<div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: isDark ? "rgba(10, 15, 30, 0.4)" : "rgba(255, 255, 255, 0.2)", backdropFilter: "blur(24px)", WebkitBackdropFilter: "blur(24px)", border: isDark ? "1px solid rgba(255, 255, 255, 0.1)" : "1px solid rgba(255, 255, 255, 0.4)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""
new_sidebar = """<div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] h-full overflow-hidden backdrop-blur-md"
          style={{ background: "rgba(255, 255, 255, 0.12)", backdropFilter: "blur(12px)", WebkitBackdropFilter: "blur(12px)", border: "1px solid rgba(255, 255, 255, 0.2)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)" }}
        >"""

old_main = """<div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: isDark ? "rgba(10, 15, 30, 0.4)" : "rgba(255, 255, 255, 0.2)", backdropFilter: "blur(24px)", WebkitBackdropFilter: "blur(24px)", border: isDark ? "1px solid rgba(255, 255, 255, 0.1)" : "1px solid rgba(255, 255, 255, 0.4)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""
new_main = """<div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] h-full overflow-hidden backdrop-blur-md"
          style={{ background: "rgba(255, 255, 255, 0.12)", backdropFilter: "blur(12px)", WebkitBackdropFilter: "blur(12px)", border: "1px solid rgba(255, 255, 255, 0.2)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)" }}
        >"""

content = content.replace(old_sidebar, new_sidebar)
content = content.replace(old_main, new_main)

# Also fix the weird pseudo-element bug in Chrome where child backdrops fail inside 3D parents
# by wrapping the inner contents in a container or adding a pseudoelement for the blur
# BUT since StatsSection uses identical CSS, we just copied StatsSection's exact styles.

with open(file_path, "w") as f:
    f.write(content)
print("Reverted to white blur and added back 3D transform")
