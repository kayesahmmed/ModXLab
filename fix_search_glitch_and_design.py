import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"

with open(file_path, "r") as f:
    content = f.read()

# Fix 1: Search Button inline styles
old_search_btn = """              <motion.button
                whileHover={{ scale: 1.06 }}
                whileTap={{ scale: 0.94 }}
                onClick={handleSearchAction}
                className="shrink-0 w-14 h-14 flex items-center justify-center rounded-2xl backdrop-blur-xl transition-all duration-300 cursor-pointer relative border border-white/20 shadow-lg text-white"
                style={{
                  background: searchOpen
                    ? "rgba(255, 255, 255, 0.2)"
                    : "rgba(255, 255, 255, 0.1)",
                }}
                title="Search ModX Lab"
                aria-label="Search"
              >"""
new_search_btn = """              <motion.button
                whileHover={{ scale: 1.06 }}
                whileTap={{ scale: 0.94 }}
                onClick={handleSearchAction}
                className={`shrink-0 w-14 h-14 flex items-center justify-center rounded-2xl backdrop-blur-xl transition-all duration-300 cursor-pointer relative border border-white/20 shadow-lg text-white ${searchOpen ? 'bg-white/20' : 'bg-white/10'}`}
                title="Search ModX Lab"
                aria-label="Search"
              >"""
content = content.replace(old_search_btn, new_search_btn)

# Fix 2: Dropdown box inline styles & premium UI
old_dropdown_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0" style={{
                      background: "rgba(15, 23, 42, 0.95)",
                      backdropFilter: "blur(40px)",
                      WebkitBackdropFilter: "blur(40px)",
                      border: "1px solid rgba(255, 255, 255, 0.25)",
                      boxShadow: "0 12px 40px 0 rgba(0, 0, 0, 0.3)",
                    }} />"""
new_dropdown_bg = """                    <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 bg-[#0F172A]/90 backdrop-blur-2xl border border-white/20 shadow-[0_20px_50px_rgba(0,0,0,0.5)]" />"""
content = content.replace(old_dropdown_bg, new_dropdown_bg)

# Fix 3: Premium UI for dropdown items
old_dropdown_list = """                    <div className="flex flex-col divide-y divide-white/10 max-h-72 overflow-y-auto scrollbar-thin overscroll-contain" data-lenis-prevent="true">
                      {filteredResults.map((item, index) => (
                        <button
                          key={index}
                          className="w-full text-left px-3.5 py-3 rounded-xl transition-all duration-150 flex items-center justify-between gap-3 cursor-pointer group hover:bg-white/15 active:bg-white/20 text-white"
                          onMouseDown={(e) => e.preventDefault()}
                          onClick={() => {
                            setSearchVal("");
                            setSearchOpen(false);
                            setShowSuggestions(false);
                            window.location.href = item.url;
                          }}
                        >
                          <div className="flex items-center gap-3 min-w-0 flex-1">
                            {item.img ? (
                              <img src={item.img} alt={item.title} className="w-8 h-8 rounded-lg object-cover shrink-0" />
                            ) : (
                              <div className="w-8 h-8 rounded-lg bg-white/20 flex items-center justify-center shrink-0 text-white group-hover:bg-[#16CF83] group-hover:text-slate-950 transition-colors">
                                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                                </svg>
                              </div>
                            )}
                            <div className="flex flex-col min-w-0 flex-1">
                              <span className="text-sm font-bold truncate text-white group-hover:text-[#16CF83] transition-colors">
                                {item.title}
                              </span>
                              <span className="text-xs font-normal truncate text-white/80">
                                {item.desc}
                              </span>
                            </div>
                          </div>
                          <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md bg-white/15 text-white border border-white/25 shrink-0 group-hover:border-white/40">
                            {item.category || item.type || "App"}
                          </span>
                        </button>
                      ))}
                    </div>"""
                    
new_dropdown_list = """                    <div className="flex flex-col gap-1.5 p-2 max-h-[350px] overflow-y-auto scrollbar-thin overscroll-contain" data-lenis-prevent="true">
                      {filteredResults.map((item, index) => (
                        <button
                          key={index}
                          className="w-full text-left p-3 rounded-xl transition-all duration-300 flex items-center justify-between gap-3 cursor-pointer group hover:bg-white/10 hover:shadow-md hover:border-white/10 border border-transparent active:scale-[0.98] text-white relative overflow-hidden"
                          onMouseDown={(e) => e.preventDefault()}
                          onClick={() => {
                            setSearchVal("");
                            setSearchOpen(false);
                            setShowSuggestions(false);
                            window.location.href = item.url;
                          }}
                        >
                          <div className="absolute inset-0 bg-gradient-to-r from-white/0 via-white/5 to-white/0 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000" />
                          <div className="flex items-center gap-4 min-w-0 flex-1 relative z-10">
                            {item.img ? (
                              <div className="relative shrink-0">
                                <img src={item.img} alt={item.title} className="w-10 h-10 rounded-xl object-cover border border-white/10 group-hover:border-[#2790FF]/50 transition-colors" />
                                <div className="absolute inset-0 rounded-xl ring-2 ring-black/10 shadow-inner pointer-events-none" />
                              </div>
                            ) : (
                              <div className="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center shrink-0 text-white group-hover:bg-[#2790FF]/15 group-hover:border-[#2790FF]/40 group-hover:text-[#2790FF] transition-all duration-300 shadow-sm">
                                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M13 10V3L4 14h7v7l9-11h-7z" />
                                </svg>
                              </div>
                            )}
                            <div className="flex flex-col min-w-0 flex-1">
                              <span className="text-sm font-extrabold truncate text-white/95 group-hover:text-white transition-colors tracking-wide">
                                {item.title}
                              </span>
                              <span className="text-[11px] font-medium truncate text-white/50 group-hover:text-white/70 transition-colors mt-0.5">
                                {item.desc}
                              </span>
                            </div>
                          </div>
                          <span className="text-[9px] font-black uppercase tracking-widest px-2.5 py-1 rounded-lg bg-white/5 text-white/70 border border-white/10 shrink-0 group-hover:border-white/20 group-hover:bg-white/10 group-hover:text-white transition-all duration-300 relative z-10">
                            {item.category || item.type || "App"}
                          </span>
                        </button>
                      ))}
                    </div>"""
content = content.replace(old_dropdown_list, new_dropdown_list)

with open(file_path, "w") as f:
    f.write(content)

