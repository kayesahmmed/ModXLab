import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"

with open(file_path, "r") as f:
    content = f.read()

# Contact Me Button
old_contact_me = """              className="h-14 pl-7 pr-2.5 rounded-2xl font-['Orbitron',sans-serif] font-extrabold text-white text-xs sm:text-sm tracking-widest uppercase transition-all duration-300 hover:scale-[1.02] cursor-pointer shadow-[0_10px_40px_-10px_rgba(39,144,255,0.4)] active:scale-95 border border-[#2790FF]/40 relative overflow-hidden group flex items-center justify-between gap-4 backdrop-blur-2xl"
              style={{
                background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)",
                boxShadow: "0 8px 32px 0 rgba(39, 144, 255, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.2)",
              }}
            >
              <span className="font-extrabold text-white tracking-wider whitespace-nowrap">CONTACT ME</span>
              <div className="w-10 h-10 rounded-xl bg-black/60 text-white flex items-center justify-center shrink-0 border border-[#2790FF]/40 group-hover:bg-[#2790FF]/40 transition-all duration-300">
                <svg className="w-5 h-5 text-white transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">"""
new_contact_me = """              className="h-14 pl-7 pr-2.5 rounded-2xl font-['Orbitron',sans-serif] font-extrabold text-slate-900 text-xs sm:text-sm tracking-widest uppercase transition-all duration-300 hover:scale-[1.02] cursor-pointer shadow-[0_10px_40px_-10px_rgba(0,229,209,0.4)] active:scale-95 border border-[#00E5D1]/60 relative overflow-hidden group flex items-center justify-between gap-4 backdrop-blur-2xl"
              style={{
                background: "linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(224, 247, 250, 0.95) 50%, rgba(0, 229, 209, 0.8) 100%)",
                boxShadow: "0 8px 32px 0 rgba(0, 229, 209, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.5)",
              }}
            >
              <span className="font-extrabold text-slate-900 tracking-wider whitespace-nowrap">CONTACT ME</span>
              <div className="w-10 h-10 rounded-xl bg-slate-900 text-white flex items-center justify-center shrink-0 border border-slate-700 group-hover:bg-[#00E5D1] group-hover:border-[#00E5D1] group-hover:text-slate-900 transition-all duration-300 shadow-md">
                <svg className="w-5 h-5 text-current transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">"""
content = content.replace(old_contact_me, new_contact_me)


# Search Bar background
old_search_bg = """                <div 
                  className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] ${searchOpen ? "border border-[#2790FF]/40" : "border border-transparent"}`} 
                  style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}
                />"""
new_search_bg = """                <div 
                  className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 shadow-[0_8px_32px_0_rgba(0,229,209,0.25),_inset_0_1px_0_rgba(255,255,255,0.5)] ${searchOpen ? "border border-[#00E5D1]/60" : "border border-transparent"}`} 
                  style={{ background: "linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(224, 247, 250, 0.95) 50%, rgba(0, 229, 209, 0.8) 100%)" }}
                />"""
content = content.replace(old_search_bg, new_search_bg)


# Search Input Text
old_search_input = """className="w-full h-full bg-transparent text-[16px] outline-none border-none shadow-none pl-5 pr-10 font-['Plus_Jakarta_Sans',sans-serif] text-white\""""
new_search_input = """className="w-full h-full bg-transparent text-[16px] outline-none border-none shadow-none pl-5 pr-10 font-['Plus_Jakarta_Sans',sans-serif] text-slate-900 placeholder-slate-500 font-semibold\""""
content = content.replace(old_search_input, new_search_input)


# Search Input close button
old_search_close = """                    className={`absolute right-3.5 w-7 h-7 flex items-center justify-center rounded-full transition-all cursor-pointer text-white hover:bg-white/10 ${searchVal ? "opacity-60 hover:opacity-100" : "opacity-0 pointer-events-none"}`}"""
new_search_close = """                    className={`absolute right-3.5 w-7 h-7 flex items-center justify-center rounded-full transition-all cursor-pointer text-slate-800 hover:bg-slate-900/10 ${searchVal ? "opacity-60 hover:opacity-100" : "opacity-0 pointer-events-none"}`}"""
content = content.replace(old_search_close, new_search_close)


# Search Toggle Button (the icon button)
old_search_btn = """              <motion.button
                whileHover={{ scale: 1.06 }}
                whileTap={{ scale: 0.94 }}
                onClick={handleSearchAction}
                className={`shrink-0 w-14 h-14 flex items-center justify-center rounded-2xl transition-all duration-300 cursor-pointer relative border shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] text-white group ${searchOpen ? 'border-[#2790FF]/50 bg-[#2790FF]/30' : 'border-[#2790FF]/30 hover:border-[#2790FF]/50 hover:bg-[#2790FF]/20'}`}
                style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}
              >
                <svg className="w-6 h-6 transition-transform duration-300" fill="none" viewBox="0 0 15 15">
                  <path d={svgPaths.p3e9cf280} fill="white" />
                </svg>
              </motion.button>"""
new_search_btn = """              <motion.button
                whileHover={{ scale: 1.06 }}
                whileTap={{ scale: 0.94 }}
                onClick={handleSearchAction}
                className={`shrink-0 w-14 h-14 flex items-center justify-center rounded-2xl transition-all duration-300 cursor-pointer relative border shadow-[0_8px_32px_0_rgba(0,229,209,0.25),_inset_0_1px_0_rgba(255,255,255,0.5)] text-slate-900 group ${searchOpen ? 'border-[#00E5D1]/60' : 'border-[#00E5D1]/40 hover:border-[#00E5D1]/60'}`}
                style={{ background: "linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(224, 247, 250, 0.95) 50%, rgba(0, 229, 209, 0.8) 100%)" }}
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
