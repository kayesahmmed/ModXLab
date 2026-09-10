import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

target = """          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="w-full flex flex-wrap items-center justify-center gap-3 sm:gap-6 mt-8 sm:mt-12 relative z-20"
          >
            <div className="flex flex-col items-center gap-1.5 px-6 py-4 rounded-3xl bg-white/5 backdrop-blur-xl border border-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.15)] transition-all hover:scale-105 hover:bg-white/10 hover:border-white/20">
              <span className="font-['Orbitron',sans-serif] font-black text-2xl sm:text-3xl text-transparent bg-clip-text bg-gradient-to-r from-[#2790FF] to-[#00E5D1]">
                25K+
              </span>
              <span className="text-[10px] sm:text-xs font-bold text-white/70 uppercase tracking-widest">Total Downloads</span>
            </div>
            
            <div className="flex flex-col items-center gap-1.5 px-6 py-4 rounded-3xl bg-white/5 backdrop-blur-xl border border-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.15)] transition-all hover:scale-105 hover:bg-white/10 hover:border-white/20">
              <span className="font-['Orbitron',sans-serif] font-black text-2xl sm:text-3xl text-transparent bg-clip-text bg-gradient-to-r from-[#16CF83] to-[#2790FF]">
                99.9%
              </span>
              <span className="text-[10px] sm:text-xs font-bold text-white/70 uppercase tracking-widest">Anti-Ban Safe</span>
            </div>

            <div className="flex flex-col items-center gap-1.5 px-6 py-4 rounded-3xl bg-white/5 backdrop-blur-xl border border-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.15)] transition-all hover:scale-105 hover:bg-white/10 hover:border-white/20">
              <span className="font-['Orbitron',sans-serif] font-black text-2xl sm:text-3xl text-transparent bg-clip-text bg-gradient-to-r from-[#7B2CBF] to-[#00E5D1]">
                <div className="flex items-center gap-2">
                  <span className="relative flex h-3 w-3">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#16CF83] opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-3 w-3 bg-[#16CF83]"></span>
                  </span>
                  3.2K
                </div>
              </span>
              <span className="text-[10px] sm:text-xs font-bold text-white/70 uppercase tracking-widest">Active Users</span>
            </div>
          </motion.div>"""

if target in content:
    content = content.replace(target, "")
    with open(file_path, "w") as f:
        f.write(content)
    print("Removed stats from HeroSection")
else:
    print("Stats not found in HeroSection")

