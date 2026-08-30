const fs = require('fs');
const file = 'artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx';
let content = fs.readFileSync(file, 'utf8');

const replacement = `
                        <motion.a
                          href={file.downloadLink}
                          target="_blank"
                          rel="noopener noreferrer"
                          whileHover={{ scale: 1.02 }}
                          whileTap={{ scale: 0.98 }}
                          className="w-full sm:w-auto px-6 py-3.5 rounded-[18px] bg-white font-['Plus_Jakarta_Sans',sans-serif] font-extrabold text-[13px] uppercase flex items-center justify-center gap-2.5 shadow-xl hover:shadow-[0_15px_30px_rgba(255,255,255,0.25)] transition-all duration-300 relative overflow-hidden group shrink-0"
                        >
                          <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-gradient-to-r from-transparent via-slate-200/50 to-transparent -translate-x-full group-hover:translate-x-full ease-in-out" style={{ transitionDuration: "1s" }} />
                          <svg className="w-4.5 h-4.5 relative z-10 animate-bounce text-slate-950" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="3">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                          </svg>
                          <span className="relative z-10 tracking-wide text-slate-950">{file.buttonText || "Download Free APK"}</span>
                        </motion.a>
                      </div>
                      
                      {file.previewImages && file.previewImages.length > 0 && (
                        <div className="mt-4 pt-4 border-t w-full flex flex-col gap-2" style={{ borderColor: isDark ? "rgba(255,255,255,0.15)" : "rgba(0,0,0,0.06)" }}>
                          <span className="text-xs font-bold uppercase tracking-widest text-white/70 ml-1 mb-1">App Previews</span>
                          <div className="flex gap-4 overflow-x-auto pb-4 scrollbar-none snap-x" style={{ WebkitOverflowScrolling: "touch" }}>
                            {file.previewImages.map((img: string, i: number) => (
                              <div key={i} className="relative w-[150px] sm:w-[180px] aspect-[9/16] shrink-0 rounded-2xl overflow-hidden shadow-2xl border border-white/20 snap-center bg-black/20">
                                <img src={img} alt={\`Preview \${i+1}\`} className="w-full h-full object-cover hover:scale-110 transition-transform duration-700" />
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                      
                    </div>
`;
content = content.replace(/<motion\.a\s+href=\{file\.downloadLink\}[^]+?<\/motion\.a>\s+<\/div>\s+\);\s+\}\)}/m, replacement.trim() + '\n                    );\n                  })}');

fs.writeFileSync(file, content);
