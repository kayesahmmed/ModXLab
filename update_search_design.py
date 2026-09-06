import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"

with open(file_path, "r") as f:
    content = f.read()

# 1. Update the Search Bar Input container background (to match Contact Me without backdrop-blur)
old_search_bg = """                <div className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 bg-white/20 backdrop-blur-xl shadow-2xl ${searchOpen ? "border border-white/20" : "border border-transparent"}`} />"""
new_search_bg = """                <div 
                  className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] ${searchOpen ? "border border-[#2790FF]/40" : "border border-transparent"}`} 
                  style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}
                />"""
content = content.replace(old_search_bg, new_search_bg)

# 2. Update Search Button background (to match Contact Me)
old_search_btn = """                className={`shrink-0 w-14 h-14 flex items-center justify-center rounded-2xl backdrop-blur-xl transition-all duration-300 cursor-pointer relative border border-white/20 shadow-lg text-white ${searchOpen ? 'bg-white/20' : 'bg-white/10'}`}"""
new_search_btn = """                className={`shrink-0 w-14 h-14 flex items-center justify-center rounded-2xl transition-all duration-300 cursor-pointer relative border shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] text-white group ${searchOpen ? 'border-[#2790FF]/50 bg-[#2790FF]/30' : 'border-[#2790FF]/30 hover:border-[#2790FF]/50 hover:bg-[#2790FF]/20'}`}
                style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}"""
content = content.replace(old_search_btn, new_search_btn)


# 3. Update the Suggestions Box design (Premium)
# Background
old_sugg_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 bg-[#0F172A]/90 backdrop-blur-2xl border border-white/20 shadow-[0_20px_50px_rgba(0,0,0,0.5)]" />"""
new_sugg_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 bg-slate-900/95 backdrop-blur-3xl border border-[#2790FF]/30 shadow-[0_24px_60px_-10px_rgba(39,144,255,0.25)] ring-1 ring-white/10" />"""
content = content.replace(old_sugg_bg, new_sugg_bg)

# List container and items
old_list_start = """                    <div className="flex flex-col divide-y divide-white/10 max-h-72 overflow-y-auto scrollbar-thin overscroll-contain" data-lenis-prevent="true">
                      {filteredResults.map((item, index) => (
                        <button
                          key={index}
                          className="w-full text-left px-3.5 py-3 rounded-xl transition-all duration-150 flex items-center justify-between gap-3 cursor-pointer group hover:bg-white/15 active:bg-white/20 text-white"
                          onMouseDown={(e) => e.preventDefault()}
                          onClick={() => {"""
new_list_start = """                    <div className="flex flex-col gap-1 p-2 max-h-[340px] overflow-y-auto scrollbar-thin overscroll-contain" data-lenis-prevent="true">
                      {filteredResults.map((item, index) => (
                        <button
                          key={index}
                          className="w-full text-left p-3 rounded-xl transition-all duration-300 flex items-center justify-between gap-3 cursor-pointer group hover:bg-[#2790FF]/10 active:scale-[0.98] text-white border border-transparent hover:border-[#2790FF]/30 relative overflow-hidden"
                          onMouseDown={(e) => e.preventDefault()}
                          onClick={() => {"""
content = content.replace(old_list_start, new_list_start)

# Items inner design
old_items_inner = """                          <div className="flex items-center gap-3 min-w-0 flex-1">
                            {item.imageUrl ? (
                              <img src={item.imageUrl} className="w-8 h-8 rounded-lg object-cover shadow-sm shrink-0" alt="Icon" />
                            ) : (
                              <div className="w-8 h-8 rounded-lg bg-white/20 flex items-center justify-center shrink-0 text-white group-hover:bg-[#16CF83] group-hover:text-slate-950 transition-colors">
                                <svg className="w-4.5 h-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.2">
                                  <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                                </svg>
                              </div>
                            )}                                          
                            <div className="flex flex-col min-w-0 flex-1">
                              <span className="font-bold text-sm truncate group-hover:text-white transition-colors text-white">
                                {item.title}
                              </span>
                              <span className="text-xs font-normal truncate text-white/80">
                                {item.desc}
                              </span>
                            </div>
                          </div>
                          <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md bg-white/15 text-white border border-white/25 shrink-0 group-hover:border-white/40">
                            {item.category || item.type || "App"}
                          </span>"""

new_items_inner = """                          <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000" />
                          <div className="flex items-center gap-3.5 min-w-0 flex-1 relative z-10">
                            {item.imageUrl ? (
                              <div className="relative shrink-0">
                                <img src={item.imageUrl} className="w-10 h-10 rounded-xl object-cover shadow-sm ring-1 ring-white/10 group-hover:ring-[#2790FF]/50 transition-all duration-300" alt="Icon" />
                              </div>
                            ) : (
                              <div className="w-10 h-10 rounded-xl bg-white/10 border border-white/10 flex items-center justify-center shrink-0 text-white group-hover:bg-[#2790FF]/20 group-hover:border-[#2790FF]/50 group-hover:text-[#2790FF] transition-all duration-300 shadow-sm">
                                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.2">
                                  <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                                </svg>
                              </div>
                            )}                                          
                            <div className="flex flex-col min-w-0 flex-1">
                              <span className="font-extrabold text-sm truncate group-hover:text-[#2790FF] transition-colors text-white/95">
                                {item.title}
                              </span>
                              <span className="text-[11px] font-medium mt-0.5 truncate text-white/50 group-hover:text-white/70">
                                {item.desc}
                              </span>
                            </div>
                          </div>
                          <span className="text-[9px] font-black uppercase tracking-widest px-2.5 py-1 rounded-md bg-white/10 text-white/70 border border-white/10 shrink-0 group-hover:border-[#2790FF]/40 group-hover:bg-[#2790FF]/20 group-hover:text-white transition-all duration-300 relative z-10">
                            {item.category || item.type || "App"}
                          </span>"""
content = content.replace(old_items_inner, new_items_inner)

with open(file_path, "w") as f:
    f.write(content)
