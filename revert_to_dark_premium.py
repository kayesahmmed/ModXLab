import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"

with open(file_path, "r") as f:
    content = f.read()

# 1. Contact Me Button -> Premium Glass Dark Theme with White/Cyan accents
old_contact_me = """              className="h-14 pl-7 pr-2.5 rounded-2xl font-['Orbitron',sans-serif] font-extrabold text-slate-900 text-xs sm:text-sm tracking-widest uppercase transition-all duration-300 hover:scale-[1.02] cursor-pointer shadow-[0_10px_40px_-10px_rgba(0,229,209,0.4)] active:scale-95 border border-[#00E5D1]/60 relative overflow-hidden group flex items-center justify-between gap-4 backdrop-blur-2xl"
              style={{
                background: "linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(224, 247, 250, 0.95) 50%, rgba(0, 229, 209, 0.8) 100%)",
                boxShadow: "0 8px 32px 0 rgba(0, 229, 209, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.5)",
              }}
            >
              <span className="font-extrabold text-slate-900 tracking-wider whitespace-nowrap">CONTACT ME</span>
              <div className="w-10 h-10 rounded-xl bg-slate-900 text-white flex items-center justify-center shrink-0 border border-slate-700 group-hover:bg-[#00E5D1] group-hover:border-[#00E5D1] group-hover:text-slate-900 transition-all duration-300 shadow-md">
                <svg className="w-5 h-5 text-current transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">"""
new_contact_me = """              className="h-14 pl-7 pr-2.5 rounded-2xl font-['Orbitron',sans-serif] font-extrabold text-white text-xs sm:text-sm tracking-widest uppercase transition-all duration-300 hover:scale-[1.02] cursor-pointer shadow-lg active:scale-95 border border-white/20 relative overflow-hidden group flex items-center justify-between gap-4 backdrop-blur-xl bg-white/10 hover:bg-white/15"
            >
              <span className="font-extrabold text-white tracking-wider whitespace-nowrap">CONTACT ME</span>
              <div className="w-10 h-10 rounded-xl bg-white text-slate-900 flex items-center justify-center shrink-0 border border-white group-hover:scale-105 transition-all duration-300 shadow-md">
                <svg className="w-5 h-5 text-current transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">"""
content = content.replace(old_contact_me, new_contact_me)


# 2. Search Bar Background -> Light White (No Gradient)
old_search_bg = """                <div 
                  className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 shadow-[0_8px_32px_0_rgba(0,229,209,0.25),_inset_0_1px_0_rgba(255,255,255,0.5)] ${searchOpen ? "border border-[#00E5D1]/60" : "border border-transparent"}`} 
                  style={{ background: "linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(224, 247, 250, 0.95) 50%, rgba(0, 229, 209, 0.8) 100%)" }}
                />"""
new_search_bg = """                <div 
                  className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 bg-white/10 backdrop-blur-xl shadow-lg ${searchOpen ? "border border-white/30" : "border border-transparent"}`} 
                />"""
content = content.replace(old_search_bg, new_search_bg)


# 3. Search Input Text -> Back to White
old_search_input = """className="w-full h-full bg-transparent text-[16px] outline-none border-none shadow-none pl-5 pr-10 font-['Plus_Jakarta_Sans',sans-serif] text-slate-900 placeholder-slate-500 font-semibold\""""
new_search_input = """className="w-full h-full bg-transparent text-[16px] outline-none border-none shadow-none pl-5 pr-10 font-['Plus_Jakarta_Sans',sans-serif] text-white placeholder-white/50 font-medium\""""
content = content.replace(old_search_input, new_search_input)


# 4. Search Input close button -> Back to white
old_search_close = """                    className={`absolute right-3.5 w-7 h-7 flex items-center justify-center rounded-full transition-all cursor-pointer text-slate-800 hover:bg-slate-900/10 ${searchVal ? "opacity-60 hover:opacity-100" : "opacity-0 pointer-events-none"}`}"""
new_search_close = """                    className={`absolute right-3.5 w-7 h-7 flex items-center justify-center rounded-full transition-all cursor-pointer text-white hover:bg-white/10 ${searchVal ? "opacity-60 hover:opacity-100" : "opacity-0 pointer-events-none"}`}"""
content = content.replace(old_search_close, new_search_close)


# 5. Search Toggle Button (the icon button) -> Pure White Box
# It's currently using the gradient
old_search_btn = """              <motion.button
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

# 6. Suggestions box match dark theme
old_sugg_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 bg-slate-900/95 backdrop-blur-3xl border border-[#2790FF]/30 shadow-[0_24px_60px_-10px_rgba(39,144,255,0.25)] ring-1 ring-white/10" />"""
new_sugg_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 bg-slate-900/95 backdrop-blur-3xl border border-[#00E5D1]/30 shadow-[0_24px_60px_-10px_rgba(0,229,209,0.15)] ring-1 ring-white/10" />"""
content = content.replace(old_sugg_bg, new_sugg_bg)

# 7. Suggestions item hover effect match cyan theme
old_item_hover = """                          className="w-full text-left p-3 rounded-xl transition-all duration-300 flex items-center justify-between gap-3 cursor-pointer group hover:bg-[#2790FF]/10 active:scale-[0.98] text-white border border-transparent hover:border-[#2790FF]/30 relative overflow-hidden\""""
new_item_hover = """                          className="w-full text-left p-3 rounded-xl transition-all duration-300 flex items-center justify-between gap-3 cursor-pointer group hover:bg-[#00E5D1]/10 active:scale-[0.98] text-white border border-transparent hover:border-[#00E5D1]/30 relative overflow-hidden\""""
content = content.replace(old_item_hover, new_item_hover)

# 8. More Cyan/Theme tweaks
old_icon_1 = """                                <img src={item.imageUrl} className="w-10 h-10 rounded-xl object-cover shadow-sm ring-1 ring-white/10 group-hover:ring-[#2790FF]/50 transition-all duration-300" alt="Icon" />"""
new_icon_1 = """                                <img src={item.imageUrl} className="w-10 h-10 rounded-xl object-cover shadow-sm ring-1 ring-white/10 group-hover:ring-[#00E5D1]/50 transition-all duration-300" alt="Icon" />"""
content = content.replace(old_icon_1, new_icon_1)

old_icon_2 = """                              <div className="w-10 h-10 rounded-xl bg-white/10 border border-white/10 flex items-center justify-center shrink-0 text-white group-hover:bg-[#2790FF]/20 group-hover:border-[#2790FF]/50 group-hover:text-[#2790FF] transition-all duration-300 shadow-sm">"""
new_icon_2 = """                              <div className="w-10 h-10 rounded-xl bg-white/10 border border-white/10 flex items-center justify-center shrink-0 text-white group-hover:bg-[#00E5D1]/20 group-hover:border-[#00E5D1]/50 group-hover:text-[#00E5D1] transition-all duration-300 shadow-sm">"""
content = content.replace(old_icon_2, new_icon_2)

old_text = """                              <span className="font-extrabold text-sm truncate group-hover:text-[#2790FF] transition-colors text-white/95">"""
new_text = """                              <span className="font-extrabold text-sm truncate group-hover:text-[#00E5D1] transition-colors text-white/95">"""
content = content.replace(old_text, new_text)

old_badge = """                          <span className="text-[9px] font-black uppercase tracking-widest px-2.5 py-1 rounded-md bg-white/10 text-white/70 border border-white/10 shrink-0 group-hover:border-[#2790FF]/40 group-hover:bg-[#2790FF]/20 group-hover:text-white transition-all duration-300 relative z-10">"""
new_badge = """                          <span className="text-[9px] font-black uppercase tracking-widest px-2.5 py-1 rounded-md bg-white/10 text-white/70 border border-white/10 shrink-0 group-hover:border-[#00E5D1]/40 group-hover:bg-[#00E5D1]/20 group-hover:text-[#00E5D1] transition-all duration-300 relative z-10">"""
content = content.replace(old_badge, new_badge)


with open(file_path, "w") as f:
    f.write(content)

