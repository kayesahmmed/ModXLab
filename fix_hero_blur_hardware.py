import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

old_sidebar = """<div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.08)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.15)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""
new_sidebar = """<motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.08)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.15)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)", transform: "translateZ(0)", willChange: "transform, opacity" }}
        >"""

old_main = """<div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.08)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.15)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)" }}
        >"""
new_main = """<motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] transition-all duration-700 h-full overflow-hidden"
          style={{ background: "rgba(255, 255, 255, 0.08)", backdropFilter: "blur(16px)", WebkitBackdropFilter: "blur(16px)", border: "1px solid rgba(255, 255, 255, 0.15)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.2)", transform: "translateZ(0)", willChange: "transform, opacity" }}
        >"""

content = content.replace(old_sidebar, new_sidebar)
content = content.replace(old_main, new_main)

content = content.replace("</button>\n          </div>\n        </div>\n\n        {/* Right Column", "</button>\n          </div>\n        </motion.div>\n\n        {/* Right Column")
content = content.replace("                <span>ModX Lab Hub</span>", "                <span>ModX Lab Hub</span>") # Just an anchor

# We need to find the end of the main div
# Main div starts around line 593, ends around line 1172 (before </div></div> </div>)
# A safer way to replace the closing tags is by regex or just replacing the last </div> before the <AnimatePresence> or whatever is after.
