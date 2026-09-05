import re

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

# 1. Fix the Search Input Container
# Find the exact block using regex
input_regex = r'<div\s+className={`transition-all duration-350 ease-\[cubic-bezier\(0\.16,1,0\.3,1\)\] h-14 flex items-center overflow-hidden rounded-2xl border \$\{\s*searchOpen \? "w-\[260px\] sm:w-\[320px\] opacity-100 border-white/20 pointer-events-auto" : "w-0 opacity-0 border-transparent pointer-events-none"\s*\}`}\s*style=\{\{.*?(boxShadow: "0 8px 32px 0 rgba\(0,0,0,0\.15\)".*?)\}\}\s*>\s*<div className="relative w-full h-full flex items-center">'

new_input = """<div
                className={`transition-all duration-350 ease-[cubic-bezier(0.16,1,0.3,1)] h-14 flex items-center rounded-2xl relative ${
                  searchOpen ? "w-[260px] sm:w-[320px] opacity-100 pointer-events-auto" : "w-0 opacity-0 pointer-events-none"
                }`}
              >
                <div className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 border ${searchOpen ? "border-white/20" : "border-transparent"}`} style={{
                  background: "rgba(255, 255, 255, 0.18)",
                  backdropFilter: "blur(16px)",
                  WebkitBackdropFilter: "blur(16px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                  boxShadow: "0 8px 32px 0 rgba(0,0,0,0.15)"
                }} />
                <div className="relative w-full h-full flex items-center z-10 overflow-hidden rounded-2xl">"""

content = re.sub(input_regex, new_input, content, flags=re.DOTALL)

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)
