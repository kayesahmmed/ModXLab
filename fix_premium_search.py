with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

# Fix 1: Search bar parent and glass effect for glitch fix
# Ensure input and wrapper are free of transforms causing repaints
old_dropdown_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0" style={{
                      background: "rgba(15, 23, 42, 0.95)",
                      backdropFilter: "blur(40px)",
                      WebkitBackdropFilter: "blur(40px)",
                      border: "1px solid rgba(255, 255, 255, 0.25)",
                      boxShadow: "0 12px 40px 0 rgba(0, 0, 0, 0.3)",
                    }} />"""
new_dropdown_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 bg-[#0B0F19]/90 backdrop-blur-3xl border border-white/20 shadow-[0_24px_48px_-12px_rgba(0,0,0,0.5)]" />"""
content = content.replace(old_dropdown_bg, new_dropdown_bg)

old_divide = 'className="flex flex-col divide-y divide-white/10 max-h-72 overflow-y-auto scrollbar-thin overscroll-contain" data-lenis-prevent="true"'
new_divide = 'className="flex flex-col max-h-[340px] overflow-y-auto scrollbar-thin overscroll-contain p-2" data-lenis-prevent="true"'
content = content.replace(old_divide, new_divide)

old_button = 'className="w-full text-left px-3.5 py-3 rounded-xl transition-all duration-150 flex items-center justify-between gap-3 cursor-pointer group hover:bg-white/15 active:bg-white/20 text-white"'
new_button = 'className="w-full text-left p-3 rounded-xl transition-all duration-200 flex items-center justify-between gap-3 cursor-pointer group hover:bg-white/10 active:bg-white/15 text-white outline-none border border-transparent hover:border-white/10"'
content = content.replace(old_button, new_button)

old_icon = 'className="w-8 h-8 rounded-lg bg-white/20 flex items-center justify-center shrink-0 text-white group-hover:bg-[#16CF83] group-hover:text-slate-950 transition-colors"'
new_icon = 'className="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center shrink-0 text-white/80 group-hover:bg-gradient-to-br group-hover:from-[#16CF83] group-hover:to-[#00E5D1] group-hover:text-slate-950 group-hover:scale-105 group-hover:shadow-[0_0_15px_rgba(22,207,131,0.5)] transition-all duration-300 border border-white/10 group-hover:border-transparent"'
content = content.replace(old_icon, new_icon)

old_text = 'className="font-bold text-sm text-white group-hover:text-white transition-colors line-clamp-1"'
new_text = 'className="font-bold text-[15px] text-white/90 group-hover:text-white transition-colors line-clamp-1 tracking-wide"'
content = content.replace(old_text, new_text)

old_desc = 'className="text-xs font-normal truncate text-white/80"'
new_desc = 'className="text-xs font-medium truncate text-white/50 group-hover:text-white/70 transition-colors"'
content = content.replace(old_desc, new_desc)

old_tag = 'className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md bg-white/15 text-white border border-white/25 shrink-0 group-hover:border-white/40"'
new_tag = 'className="text-[10px] font-bold uppercase tracking-widest px-2.5 py-1 rounded-md bg-white/5 text-white/70 border border-white/10 shrink-0 group-hover:bg-white/20 group-hover:text-white group-hover:border-white/30 transition-all duration-300"'
content = content.replace(old_tag, new_tag)

old_empty = 'className="p-4 text-center flex items-center justify-center gap-2 text-xs font-semibold text-white/90"'
new_empty = 'className="p-8 text-center flex flex-col items-center justify-center gap-3"'
content = content.replace(old_empty, new_empty)

old_empty_icon = '<span>🔍</span>'
new_empty_icon = '<div className="w-12 h-12 rounded-full bg-white/5 flex items-center justify-center text-white/40 mb-1 border border-white/10"><svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}><path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg></div>'
content = content.replace(old_empty_icon, new_empty_icon)

old_empty_text = '<span>No items match "{searchVal}"</span>'
new_empty_text = '<span className="text-[15px] font-semibold text-white/80">No results found</span><span className="text-[13px] font-medium text-white/40">Try searching for a different keyword</span>'
content = content.replace(old_empty_text, new_empty_text)

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)

