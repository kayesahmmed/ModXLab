import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"

with open(file_path, "r") as f:
    content = f.read()

# 1. Search Bar Background -> Revert to blue glass
old_search_bg = """                <div 
                  className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 shadow-[0_8px_32px_0_rgba(0,229,209,0.25),_inset_0_1px_0_rgba(255,255,255,0.5)] ${searchOpen ? "border border-[#00E5D1]/60" : "border border-transparent"}`} 
                  style={{ background: "linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(224, 247, 250, 0.95) 50%, rgba(0, 229, 209, 0.8) 100%)" }}
                />"""
new_search_bg = """                <div 
                  className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] ${searchOpen ? "border border-[#2790FF]/40" : "border border-transparent"}`} 
                  style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}
                />"""
content = content.replace(old_search_bg, new_search_bg)


# 2. Search Input Text -> Back to White
old_search_input = """className="w-full h-full bg-transparent text-[16px] outline-none border-none shadow-none pl-5 pr-10 font-['Plus_Jakarta_Sans',sans-serif] text-slate-900 placeholder-slate-500 font-semibold\""""
new_search_input = """className="w-full h-full bg-transparent text-[16px] outline-none border-none shadow-none pl-5 pr-10 font-['Plus_Jakarta_Sans',sans-serif] text-white placeholder-white/50\""""
content = content.replace(old_search_input, new_search_input)


# 3. Search Input close button -> Back to white
old_search_close = """                    className={`absolute right-3.5 w-7 h-7 flex items-center justify-center rounded-full transition-all cursor-pointer text-slate-800 hover:bg-slate-900/10 ${searchVal ? "opacity-60 hover:opacity-100" : "opacity-0 pointer-events-none"}`}"""
new_search_close = """                    className={`absolute right-3.5 w-7 h-7 flex items-center justify-center rounded-full transition-all cursor-pointer text-white hover:bg-white/10 ${searchVal ? "opacity-60 hover:opacity-100" : "opacity-0 pointer-events-none"}`}"""
content = content.replace(old_search_close, new_search_close)


# 4. Search Toggle Button (the icon button) -> Back to blue gradient glass
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
                className={`shrink-0 w-14 h-14 flex items-center justify-center rounded-2xl transition-all duration-300 cursor-pointer relative border shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] text-white group ${searchOpen ? 'border-[#2790FF]/50 bg-[#2790FF]/30' : 'border-[#2790FF]/30 hover:border-[#2790FF]/50 hover:bg-[#2790FF]/20'}`}
                style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}
                title="Search ModX Lab"
                aria-label="Search"
              >
                <svg className="w-6 h-6 transition-transform duration-300" fill="none" viewBox="0 0 15 15">
                  <path d={svgPaths.p3e9cf280} fill="white" />
                </svg>
              </motion.button>"""
content = content.replace(old_search_btn, new_search_btn)

# 5. Suggestions box match blue dark theme
old_sugg_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 bg-white/95 backdrop-blur-3xl border border-[#00E5D1]/40 shadow-[0_24px_60px_-10px_rgba(0,229,209,0.25)] ring-1 ring-black/5" />"""
new_sugg_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 bg-slate-900/95 backdrop-blur-3xl border border-[#2790FF]/30 shadow-[0_24px_60px_-10px_rgba(39,144,255,0.25)] ring-1 ring-white/10" />"""
content = content.replace(old_sugg_bg, new_sugg_bg)

# 6. Suggestions container text color -> White
old_sugg_text = """                    <div className="relative z-10 w-full h-full text-slate-900">"""
new_sugg_text = """                    <div className="relative z-10 w-full h-full text-white">"""
content = content.replace(old_sugg_text, new_sugg_text)

# 7. Suggestions item hover effect -> Match blue theme
old_item_hover = """                          className="w-full text-left p-3 rounded-xl transition-all duration-300 flex items-center justify-between gap-3 cursor-pointer group hover:bg-[#00E5D1]/15 active:scale-[0.98] text-slate-900 border border-transparent hover:border-[#00E5D1]/30 relative overflow-hidden\""""
new_item_hover = """                          className="w-full text-left p-3 rounded-xl transition-all duration-300 flex items-center justify-between gap-3 cursor-pointer group hover:bg-[#2790FF]/10 active:scale-[0.98] text-white border border-transparent hover:border-[#2790FF]/30 relative overflow-hidden\""""
content = content.replace(old_item_hover, new_item_hover)

# 8. Icons
old_icon_1 = """                                <img src={item.imageUrl} className="w-10 h-10 rounded-xl object-cover shadow-sm ring-1 ring-black/5 group-hover:ring-[#00E5D1]/50 transition-all duration-300" alt="Icon" />"""
new_icon_1 = """                                <img src={item.imageUrl} className="w-10 h-10 rounded-xl object-cover shadow-sm ring-1 ring-white/10 group-hover:ring-[#2790FF]/50 transition-all duration-300" alt="Icon" />"""
content = content.replace(old_icon_1, new_icon_1)

old_icon_2 = """                              <div className="w-10 h-10 rounded-xl bg-slate-100 border border-slate-200 flex items-center justify-center shrink-0 text-slate-500 group-hover:bg-[#00E5D1]/20 group-hover:border-[#00E5D1]/50 group-hover:text-[#00E5D1] transition-all duration-300 shadow-sm">"""
new_icon_2 = """                              <div className="w-10 h-10 rounded-xl bg-white/10 border border-white/10 flex items-center justify-center shrink-0 text-white group-hover:bg-[#2790FF]/20 group-hover:border-[#2790FF]/50 group-hover:text-[#2790FF] transition-all duration-300 shadow-sm">"""
content = content.replace(old_icon_2, new_icon_2)

# 9. Item Title/Desc
old_title = """                              <span className="font-extrabold text-sm truncate group-hover:text-[#00E5D1] transition-colors text-slate-900">"""
new_title = """                              <span className="font-extrabold text-sm truncate group-hover:text-[#2790FF] transition-colors text-white/95">"""
content = content.replace(old_title, new_title)

old_desc = """                              <span className="text-[11px] font-medium mt-0.5 truncate text-slate-500 group-hover:text-slate-700">"""
new_desc = """                              <span className="text-[11px] font-medium mt-0.5 truncate text-white/50 group-hover:text-white/70">"""
content = content.replace(old_desc, new_desc)

# 10. Badge
old_badge = """                          <span className="text-[9px] font-black uppercase tracking-widest px-2.5 py-1 rounded-md bg-slate-100 text-slate-500 border border-slate-200 shrink-0 group-hover:border-[#00E5D1]/40 group-hover:bg-[#00E5D1]/20 group-hover:text-[#00E5D1] transition-all duration-300 relative z-10">"""
new_badge = """                          <span className="text-[9px] font-black uppercase tracking-widest px-2.5 py-1 rounded-md bg-white/10 text-white/70 border border-white/10 shrink-0 group-hover:border-[#2790FF]/40 group-hover:bg-[#2790FF]/20 group-hover:text-white transition-all duration-300 relative z-10">"""
content = content.replace(old_badge, new_badge)

# 11. No matches text
old_nomatch = """                    <div className="p-4 text-center flex items-center justify-center gap-2 text-xs font-semibold text-slate-700">"""
new_nomatch = """                    <div className="p-4 text-center flex items-center justify-center gap-2 text-xs font-semibold text-white/90">"""
content = content.replace(old_nomatch, new_nomatch)


with open(file_path, "w") as f:
    f.write(content)

