import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "motion/react";
import { Theme } from "../types";
import { dataCache } from "../lib/dataCache";

const getInitialDownloads = () => {
  try {
    const cached = localStorage.getItem("cached_downloads");
    if (cached) {
      const parsed = JSON.parse(cached);
      if (Array.isArray(parsed) && parsed.length > 0) return parsed;
    }
  } catch (e) {}
  return [];
};

export default function DownloadSection({ t, isDark }: { t: Theme; isDark?: boolean }) {
  const [downloads, setDownloads] = useState<any[]>(getInitialDownloads);
  const [openHowToUseMap, setOpenHowToUseMap] = useState<Record<string, boolean>>({});
  const [fullscreenImage, setFullscreenImage] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [slideDirection, setSlideDirection] = useState(1);

  useEffect(() => {
    const loadDownloads = async () => {
      const fetched = await dataCache.getData<any[]>("downloads", []);
      if (Array.isArray(fetched) && fetched.length > 0) {
        setDownloads(fetched);
      }
    };

    loadDownloads();
    const unsub = dataCache.subscribe("downloads", (fetched) => {
      if (Array.isArray(fetched) && fetched.length > 0) {
        setDownloads(fetched);
      }
    });
    return () => unsub();
  }, []);

  const toggleHowToUse = (id: string) => {
    setOpenHowToUseMap(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const getYouTubeId = (url: string) => {
    if (!url) return null;
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
    const match = url.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
  };

  const defaultDownload = {
    id: "default-1",
    boxDate: "12 August 2026",
    files: [{
      title: "ModX Lab",
      category: "Free Fire Mod Panel · Android",
      tags: "Free Fire, Free Fire Max, Android 7+, Anti-Ban, All Devices",
      imageUrl: "",
      buttonText: "Download Free APK",
      downloadLink: "https://t.me/kayesahmmedpro"
    }],
    howToUseTitle: "How to Use",
    howToUse: "Step 1: Download Shizuku\nInstall the official Shizuku app directly from Google Play Store.\nStep 2: Start Shizuku Service\nSetup & start Shizuku via Wireless Debugging or ADB mode.\nStep 3: Open Mod Panel\nOpen ModX Lab, sign in, and activate your panel.\nStep 4: Launch & Enjoy\nLaunch Free Fire / FF Max and enjoy safe anti-ban features.",
    youtubeTitle: "Video Tutorial",
    youtubeLinks: ["https://www.youtube.com/watch?v=C4LMW4iIVgA"]
  };

  const rawDownloads = downloads.length > 0 ? downloads : [defaultDownload];
  const itemsPerPage = 4;
  const totalItems = rawDownloads.length;
  const totalPages = Math.ceil(totalItems / itemsPerPage);
  
  const maxStartIndex = Math.max(0, totalItems - itemsPerPage);
  const rawStartIndex = (currentPage - 1) * itemsPerPage;
  const startIndex = Math.min(rawStartIndex, maxStartIndex);
  
  const displayDownloads = rawDownloads.slice(startIndex, startIndex + itemsPerPage);

  return (
    <section id="download" className="relative py-16 sm:py-20 px-4 sm:px-8 lg:px-14 max-w-7xl mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.1 }}
        transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
        className="flex flex-col gap-6 w-full"
        style={{ willChange: "transform, opacity", z: 0 }}
      >
        <div className="text-center mb-6 px-4 sm:px-8 lg:px-14 relative z-10 w-full max-w-7xl mx-auto">
          <h2 className="text-3xl sm:text-4xl font-black mb-3 tracking-tight" style={{ color: t.text }}>Download</h2>
          <p className="text-sm font-semibold max-w-xl mx-auto" style={{ color: t.subtext }}>Get the latest updates and mod files.</p>
        </div>
        <AnimatePresence mode="wait" custom={slideDirection}>
          <motion.div 
            key={`page-${currentPage}`} 
            custom={slideDirection}
            initial={{ opacity: 0, x: slideDirection > 0 ? 50 : -50 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: slideDirection > 0 ? -50 : 50 }}
            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
            className="w-full flex flex-col gap-6"
          >
            {displayDownloads.map((dl, idx) => {
              const isHowToUseOpen = openHowToUseMap[dl.id] || false;
              
              const files = (dl.files && dl.files.length > 0) ? dl.files : [{ title: dl.title, category: dl.category, tags: dl.tags, imageUrl: dl.imageUrl, buttonText: dl.buttonText, downloadLink: dl.downloadLink, previewImages: dl.previewImages }];
              const ytLinks = (dl.youtubeLinks && dl.youtubeLinks.length > 0) ? dl.youtubeLinks : (dl.youtubeLink ? [dl.youtubeLink] : []);
              
              const howToUseSteps = dl.howToUse ? dl.howToUse.split('\n').filter((l: string) => l.trim() !== '') : [];
              const downloadFiles = files.filter((f: any) => f.downloadLink && f.downloadLink.trim() !== "");
              return (
                <motion.div
                  layout
                  key={dl.id}
                  id={`download-${dl.id}`}
                  initial={{ opacity: 0, y: 40, scale: 0.98 }}
                  animate={{ opacity: 1, y: 0, scale: 1 }}
                  exit={{ opacity: 0, y: -40, scale: 0.98 }}
                  whileHover={{ y: -4, scale: 1.01 }}
                  transition={{ duration: 0.6, delay: idx * 0.1, ease: [0.16, 1, 0.3, 1] }}
                  className="w-full max-w-7xl mx-auto px-5 sm:px-8 lg:px-10 py-8 sm:py-10 flex flex-col gap-6 relative overflow-hidden rounded-3xl border shadow-2xl mb-8 backdrop-blur-2xl"
              style={{
                background: isDark ? "rgba(255, 255, 255, 0.08)" : "rgba(255, 255, 255, 0.85)",
                borderColor: "rgba(255, 255, 255, 0.2)",
                boxShadow: isDark
                  ? "0 20px 50px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 0 30px rgba(255, 255, 255, 0.05)"
                  : "0 20px 50px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.8)"
              }}
            >
              {/* Radial glow background accents */}
              <div className="absolute top-0 right-0 w-96 h-96 pointer-events-none rounded-full filter blur-3xl opacity-15" style={{ background: "radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%)" }} />
              <div className="absolute bottom-0 left-0 w-80 h-80 pointer-events-none rounded-full filter blur-3xl opacity-15" style={{ background: "radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%)" }} />

              <div className="relative z-10 flex flex-col gap-6">
                
                <div className="flex flex-wrap items-center justify-between gap-3 border-b pb-4" style={{ borderColor: isDark ? "rgba(255,255,255,0.12)" : "rgba(0,0,0,0.06)" }}>
                  <div className="flex items-center gap-2">
                    <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider bg-white/10 text-white border border-white/25 shadow-sm backdrop-blur-md">
                      <svg className="w-3.5 h-3.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                      </svg>
                      VERIFIED RELEASE
                    </span>
                  </div>

                  {dl.boxDate && (
                    <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-extrabold tracking-wide" style={{ background: "rgba(255,255,255,0.12)", color: "#ffffff", border: "1px solid rgba(255,255,255,0.25)" }}>
                      <span className="w-2 h-2 rounded-full bg-white animate-pulse" />
                      <span>{dl.boxDate}</span>
                    </div>
                  )}
                </div>

                <div className={`grid gap-5 ${files.length >= 2 ? 'grid-cols-1 md:grid-cols-2' : 'grid-cols-1'}`}>
                  {files.map((file: any, fIdx: number) => {
                    const tagsArray = file.tags ? file.tags.split(',').map((t: string) => t.trim()).filter(Boolean) : [];
                    const downloadUrl = file.downloadLink || file.link || "#";
                    return (
                      <div 
                        key={fIdx} 
                        className="flex flex-col justify-between gap-4 p-5 sm:p-6 rounded-2xl border transition-all duration-300 hover:border-white/40 shadow-xl backdrop-blur-xl" 
                        style={{ 
                          background: isDark ? "rgba(255, 255, 255, 0.06)" : "rgba(248, 250, 252, 0.85)", 
                          borderColor: isDark ? "rgba(255,255,255,0.15)" : "rgba(0,0,0,0.08)" 
                        }}
                      >
                        <div className="flex flex-col gap-3">
                          <div className="flex items-start gap-4">
                            {file.imageUrl ? (
                              <img src={file.imageUrl} className="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl object-cover shadow-lg border border-white/30 shrink-0" alt="Icon" />
                            ) : (
                              <div className="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-white text-slate-900 flex items-center justify-center shrink-0 shadow-lg border border-white/40">
                                <svg className="w-8 h-8 text-slate-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">
                                  <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                                </svg>
                              </div>
                            )}
                            <div className="flex-1 min-w-0">
                              <h3 className="font-['Plus_Jakarta_Sans',sans-serif] font-black text-lg sm:text-xl tracking-tight" style={{ color: t.text }}>{file.title || "Download File"}</h3>
                              <p className="text-xs sm:text-sm font-bold mt-0.5 text-white/80">{file.category || "APK / Mod"}</p>
                            </div>
                          </div>

                          {tagsArray.length > 0 && (
                            <div className="flex flex-wrap gap-1.5 pt-1">
                              {tagsArray.map((tag: string, index: number) => (
                                <span
                                  key={index}
                                  className="px-2.5 py-1 rounded-lg text-[11px] font-bold transition-all"
                                  style={{
                                    background: "rgba(255,255,255,0.12)",
                                    color: "#ffffff",
                                    border: "1px solid rgba(255,255,255,0.2)"
                                  }}
                                >
                                  {tag}
                                </span>
                              ))}
                            </div>
                          )}
                        </div>

                        {/* Direct Download Button paired with this file */}
                        <motion.a
                          whileHover={{ scale: 1.02, boxShadow: "0 10px 30px rgba(255,255,255,0.35)" }}
                          whileTap={{ scale: 0.98 }}
                          href={downloadUrl}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="relative overflow-hidden group flex items-center justify-center gap-2.5 w-full py-3.5 px-5 rounded-xl font-['Plus_Jakarta_Sans',sans-serif] font-black text-sm sm:text-base text-slate-950 transition-all cursor-pointer border border-white/50 mt-2"
                          style={{
                            background: "linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%)",
                            boxShadow: "0 8px 25px rgba(255,255,255,0.2)"
                          }}
                        >
                          <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-gradient-to-r from-transparent via-slate-200/50 to-transparent -translate-x-full group-hover:translate-x-full ease-in-out" style={{ transitionDuration: "1s" }} />
                          <svg className="w-4.5 h-4.5 relative z-10 animate-bounce text-slate-950" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="3">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                          </svg>
                          <span className="relative z-10 tracking-wide text-slate-950">{file.buttonText || "Download Free APK"}</span>
                        </motion.a>

                      {file.previewImages && file.previewImages.length > 0 && (
                        <div className="mt-4 pt-4 border-t w-full flex flex-col gap-3" style={{ borderColor: isDark ? "rgba(255,255,255,0.15)" : "rgba(0,0,0,0.06)" }}>
                          <span className="text-xs font-bold uppercase tracking-widest text-white/70 ml-1">App Previews</span>
                          <div className="flex gap-4 overflow-x-auto pb-4 scrollbar-none snap-x" style={{ WebkitOverflowScrolling: "touch" }}>
                            {file.previewImages.map((img: string, i: number) => (
                              <div key={i} className="relative w-[150px] sm:w-[180px] aspect-[9/16] shrink-0 rounded-2xl overflow-hidden shadow-2xl border border-white/20 snap-center bg-black/20 cursor-pointer" onClick={() => setFullscreenImage(img)}>
                                <img src={img} alt={`Preview ${i+1}`} className="w-full h-full object-cover hover:scale-105 transition-transform duration-500" />
                              </div>
                            ))}
                          </div>
                        </div>
                      )}

                      </div>
                    );
                  })}
                </div>

                <div className="flex items-center justify-center gap-4 text-[11px] font-bold text-center mt-1 text-white/80">
                  <span className="flex items-center gap-1">
                    <svg className="w-3.5 h-3.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="3">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                    Fast Speed
                  </span>
                  <span>•</span>
                  <span className="flex items-center gap-1">
                    <svg className="w-3.5 h-3.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="3">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                    Virus Tested
                  </span>
                  <span>•</span>
                  <span className="flex items-center gap-1">
                    <svg className="w-3.5 h-3.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="3">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                    Anti-Ban Safe
                  </span>
                </div>

                {(howToUseSteps.length > 0 || ytLinks.length > 0) && (
                  <div
                    className="mt-2"
                    style={{ borderRadius: "20px" }}
                  >
                    <button
                      onClick={() => toggleHowToUse(dl.id)}
                      className="w-full flex items-center justify-between p-4 sm:p-5 rounded-2xl transition-all hover:bg-white/10 group cursor-pointer border shadow-md duration-300 backdrop-blur-xl"
                      style={{
                        borderColor: isHowToUseOpen ? "rgba(255,255,255,0.3)" : "rgba(255,255,255,0.18)",
                        background: isHowToUseOpen ? "rgba(255,255,255,0.08)" : "rgba(255,255,255,0.03)"
                      }}
                    >
                      <div className="flex items-center gap-4 text-left">
                        <div className="w-12 h-12 rounded-2xl bg-white text-slate-900 flex items-center justify-center shrink-0 shadow-lg border border-white/40">
                          <svg className="w-6 h-6 text-slate-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                          </svg>
                        </div>
                        <div>
                          <h3 className="font-['Plus_Jakarta_Sans',sans-serif] font-bold text-lg text-white">{dl.howToUseTitle || "How to Use"}</h3>
                          <p className="text-xs font-semibold mt-0.5 opacity-90 text-white/80">
                            Click here for step-by-step setup guide
                          </p>
                        </div>
                      </div>
                      <div className="flex items-center gap-2.5">
                        <span className="text-xs font-semibold hidden sm:inline transition-colors text-white/80">
                          {isHowToUseOpen ? "Close guide" : "Expand guide"}
                        </span>
                        <motion.div 
                          animate={{
                            rotate: isHowToUseOpen ? 180 : 0,
                            backgroundColor: isHowToUseOpen ? "#ffffff" : "rgba(255,255,255,0.15)",
                            color: isHowToUseOpen ? "#0f0c20" : "#ffffff",
                            boxShadow: isHowToUseOpen ? "0 0 15px rgba(255,255,255,0.4)" : "0 0 0px transparent"
                          }}
                          transition={{ duration: 0.2, ease: [0.16, 1, 0.3, 1] }}
                          className="w-9 h-9 rounded-xl flex items-center justify-center group-hover:scale-105"
                        >
                          <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
                          </svg>
                        </motion.div>
                      </div>
                    </button>
                    <AnimatePresence>
                      {isHowToUseOpen && (
                        <motion.div
                          initial={{ opacity: 0, height: 0 }}
                          animate={{ opacity: 1, height: "auto" }}
                          exit={{ opacity: 0, height: 0 }}
                          transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
                          className="overflow-hidden"
                        >
                          <div
                            className="mt-3 p-5 sm:p-6 rounded-[24px] flex flex-col gap-4 relative overflow-hidden shadow-2xl transition-colors duration-300"
                            style={{
                              background: isDark ? "rgba(255, 255, 255, 0.06)" : "rgba(255, 255, 255, 0.65)",
                              backdropFilter: "blur(24px)",
                              WebkitBackdropFilter: "blur(24px)",
                              border: "1px solid rgba(255, 255, 255, 0.2)"
                            }}
                          >
                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 relative z-10">
                              {howToUseSteps.map((step: string, i: number) => {
                                return (
                                  <div
                                    key={i}
                                    className="p-4 sm:p-5 rounded-2xl flex flex-col gap-2.5 relative overflow-hidden transition-colors duration-300 hover:translate-y-[-2px] hover:border-white/40 shadow-lg"
                                    style={{
                                      background: isDark ? "rgba(255, 255, 255, 0.08)" : "rgba(255, 255, 255, 0.8)",
                                      backdropFilter: "blur(16px)",
                                      WebkitBackdropFilter: "blur(16px)",
                                      border: "1px solid rgba(255, 255, 255, 0.25)"
                                    }}
                                  >
                                    <div className="flex items-center justify-between gap-2">
                                      <span
                                        className="font-mono font-black text-xs px-3 py-1 rounded-lg bg-white/20 text-white shadow-sm border border-white/30 backdrop-blur-md"
                                      >
                                        STEP 0{i + 1}
                                      </span>
                                    </div>
                                    <p className="font-['Plus_Jakarta_Sans',sans-serif] text-xs sm:text-sm leading-relaxed mt-1 text-white font-bold tracking-wide drop-shadow-sm">
                                      {step}
                                    </p>
                                  </div>
                                );
                              })}
                            </div>
                            
                            {ytLinks.length > 0 && (
                              <div
                                className="mt-4 pt-5 border-t rounded-2xl transition-colors duration-300"
                                style={{ borderColor: "rgba(255,255,255,0.2)" }}
                              >
                                <div className="flex items-center gap-3 mb-3.5">
                                  <div className="w-10 h-10 rounded-xl bg-[#FF0000]/20 flex items-center justify-center shrink-0 text-[#FF0000] shadow-[0_0_15px_rgba(255,0,0,0.3)] border border-red-500/30">
                                    <svg className="w-5 h-5 fill-current" viewBox="0 0 24 24">
                                      <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                                    </svg>
                                  </div>
                                  <div>
                                    <div className="flex items-center gap-2">
                                      <h3 className="font-['Plus_Jakarta_Sans',sans-serif] font-bold text-base sm:text-lg text-white">{dl.youtubeTitle || "Video Tutorial"}</h3>
                                      <span className="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase tracking-wider" style={{ background: "rgba(255,0,0,0.2)", color: "#FF6B6B", border: "1px solid rgba(255,0,0,0.4)" }}>
                                        YouTube Guide
                                      </span>
                                    </div>
                                    <p className="text-xs font-medium mt-0.5 text-white/80">
                                      Watch step-by-step setup video tutorials
                                    </p>
                                  </div>
                                </div>
                                <div className="grid grid-cols-1 gap-4 mt-4">
                                  {ytLinks.map((linkData: any, lIdx: number) => {
                                    const ytUrl = typeof linkData === 'string' ? linkData : linkData.url;
                                    const ytTitle = typeof linkData === 'string' ? null : linkData.title;
                                    const ytId = getYouTubeId(ytUrl);
                                    if (!ytId) return null;
                                    return (
                                      <div key={lIdx} className="flex flex-col gap-2">
                                        {ytTitle && (
                                          <h4 className="font-semibold text-sm pl-1 text-white">{ytTitle}</h4>
                                        )}
                                        <div
                                          className="relative w-full rounded-2xl overflow-hidden shadow-2xl border transition-all duration-300"
                                          style={{
                                            aspectRatio: "16/9",
                                            background: "rgba(0, 0, 0, 0.5)",
                                            borderColor: "rgba(255, 255, 255, 0.25)"
                                          }}
                                        >
                                          <iframe
                                            className="absolute top-0 left-0 w-full h-full rounded-2xl"
                                            src={`https://www.youtube.com/embed/${ytId}?rel=0&cc_load_policy=1`}
                                            title={`ModX Lab Video Tutorial ${lIdx + 1}`}
                                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                            allowFullScreen
                                          />
                                        </div>
                                      </div>
                                    );
                                  })}
                                </div>
                              </div>
                            )}
                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                )}
              </div>
            </motion.div>
          );
        })}
          </motion.div>
        </AnimatePresence>

        {totalPages > 1 && (
          <div className="flex items-center justify-center gap-3 mt-10 relative z-20">
            <button
              onClick={() => {
                setSlideDirection(-1);
                setCurrentPage(p => Math.max(1, p - 1));
              }}
              disabled={currentPage === 1}
              className="w-10 h-10 rounded-full flex items-center justify-center transition-all bg-white/10 hover:bg-white/20 disabled:opacity-50 disabled:cursor-not-allowed border border-white/20 text-white shadow-lg backdrop-blur-md cursor-pointer"
            >
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M15 19l-7-7 7-7" />
              </svg>
            </button>
            
            <div className="flex items-center gap-2">
              {Array.from({length: totalPages}, (_, i) => i + 1).map(p => (
                <button
                  key={p}
                  onClick={() => {
                    setSlideDirection(p > currentPage ? 1 : -1);
                    setCurrentPage(p);
                  }}
                  className={`w-10 h-10 rounded-full font-bold text-sm transition-all border shadow-lg backdrop-blur-md cursor-pointer ${currentPage === p ? "bg-[#2790FF] text-white border-[#2790FF]" : "bg-white/5 text-white border-white/20 hover:bg-white/15"}`}
                >
                  {p}
                </button>
              ))}
            </div>

            <button
              onClick={() => {
                setSlideDirection(1);
                setCurrentPage(p => Math.min(totalPages, p + 1));
              }}
              disabled={currentPage === totalPages}
              className="w-10 h-10 rounded-full flex items-center justify-center transition-all bg-white/10 hover:bg-white/20 disabled:opacity-50 disabled:cursor-not-allowed border border-white/20 text-white shadow-lg backdrop-blur-md cursor-pointer"
            >
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </div>
        )}
      </motion.div>

      <AnimatePresence>
        {fullscreenImage && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setFullscreenImage(null)}
            className="fixed inset-0 z-[9999] flex items-center justify-center bg-black/90 p-4 cursor-pointer"
          >
            <motion.img
              initial={{ scale: 0.9 }}
              animate={{ scale: 1 }}
              exit={{ scale: 0.9 }}
              src={fullscreenImage}
              alt="Fullscreen App Preview"
              className="w-full h-full object-contain rounded-xl"
              style={{ maxHeight: "90vh", maxWidth: "90vw" }}
            />
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
