import re

file_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"

with open(file_path, "r") as f:
    content = f.read()

blue_style = """style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)", boxShadow: "0 8px 32px 0 rgba(39, 144, 255, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.2)", border: "1px solid rgba(39,144,255,0.4)" }}"""

# 1. Verified Release
old_verified = """<span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider bg-white/10 text-white border border-white/25 shadow-sm backdrop-blur-md">"""
new_verified = f"""<span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider text-white backdrop-blur-md shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] border border-[#2790FF]/40" style={{{{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}}}>"""
content = content.replace(old_verified, new_verified)

# 2. Date Box
old_date = """<div className="flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-extrabold tracking-wide" style={{ background: "rgba(255,255,255,0.12)", color: "#ffffff", border: "1px solid rgba(255,255,255,0.25)" }}>"""
new_date = f"""<div className="flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-extrabold tracking-wide text-white shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] border border-[#2790FF]/40 backdrop-blur-md" style={{{{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}}}>"""
content = content.replace(old_date, new_date)

# 3. Category Box
old_cat = """<p className="text-xs sm:text-sm font-bold mt-0.5 text-white/80">{file.category || "APK / Mod"}</p>"""
new_cat = f"""<div className="inline-flex items-center px-2.5 py-1 mt-1.5 rounded-lg text-[11px] sm:text-xs font-extrabold tracking-wide text-white w-fit shadow-[0_4px_16px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] border border-[#2790FF]/40 backdrop-blur-md" style={{{{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}}}>{{file.category || "APK / Mod"}}</div>"""
content = content.replace(old_cat, new_cat)


# 4. Tags Box
old_tags = """                                <span
                                  key={index}
                                  className="px-2.5 py-1 rounded-lg text-[11px] font-bold transition-all"
                                  style={{
                                    background: "rgba(255,255,255,0.12)",
                                    color: "#ffffff",
                                    border: "1px solid rgba(255,255,255,0.2)"
                                  }}
                                >"""
new_tags = """                                <span
                                  key={index}
                                  className="px-2.5 py-1 rounded-lg text-[11px] font-bold transition-all text-white shadow-[0_4px_16px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] border border-[#2790FF]/40 backdrop-blur-md"
                                  style={{
                                    background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)"
                                  }}
                                >"""
content = content.replace(old_tags, new_tags)

with open(file_path, "w") as f:
    f.write(content)

