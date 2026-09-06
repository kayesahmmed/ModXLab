import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"

with open(file_path, "r") as f:
    content = f.read()

old_search_btn = """              <motion.button
                whileHover={{ scale: 1.06 }}
                whileTap={{ scale: 0.94 }}
                onClick={handleSearchAction}
                className={`shrink-0 w-14 h-14 flex items-center justify-center rounded-2xl transition-all duration-300 cursor-pointer relative border shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] text-white group ${searchOpen ? 'border-[#2790FF]/50 bg-[#2790FF]/30' : 'border-[#2790FF]/30 hover:border-[#2790FF]/50 hover:bg-[#2790FF]/20'}`}
                style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}
                title="Search ModX Lab"
                aria-label="Search"
              >
                <svg className="w-6 h-6 transition-transform duration-300" fill="none" viewBox="0 0 15 15">
                  <path d={svgPaths.p3e9cf280} fill="white" />
                </svg>
              </motion.button>"""

new_search_btn = """              <motion.button
                whileHover={{ scale: 1.06 }}
                whileTap={{ scale: 0.94 }}
                onClick={handleSearchAction}
                className={`shrink-0 w-14 h-14 flex items-center justify-center rounded-2xl transition-all duration-300 cursor-pointer relative border shadow-lg text-slate-900 bg-white group ${searchOpen ? 'border-white' : 'border-white/80 hover:border-white'}`}
                title="Search ModX Lab"
                aria-label="Search"
              >
                <svg className="w-6 h-6 transition-transform duration-300" fill="none" viewBox="0 0 15 15">
                  <path d={svgPaths.p3e9cf280} fill="currentColor" />
                </svg>
              </motion.button>"""

content = content.replace(old_search_btn, new_search_btn)

with open(file_path, "w") as f:
    f.write(content)

