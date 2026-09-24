import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "motion/react";
import { Theme } from "../types";
import { dataCache } from "../lib/dataCache";

const defaultInitialDownloads = [
  {
    id: "dl_1788230452440",
    files: [
      {
        title: "Kayes Ahmmed ",
        category: "app",
        tags: "",
        imageUrl: "",
        buttonText: "Download Free APK",
        downloadLink: "",
        previewImages: []
      }
    ],
    boxDate: "20 August 2026",
    howToUse: "",
    youtubeLinks: [],
    howToUseTitle: "How to Use",
    youtubeTitle: "Video Tutorial",
    updatedAt: "2026-09-01T02:40:52.440Z",
    createdAt: "2026-09-01T02:40:52.440Z"
  },
  {
    id: "dl_1788230413491",
    files: [
      {
        title: "ModX Lab",
        category: "App",
        tags: "Antiban",
        imageUrl: "",
        buttonText: "Download Free APK",
        downloadLink: "",
        previewImages: []
      }
    ],
    boxDate: "20 August 2026",
    howToUse: "",
    youtubeLinks: [],
    howToUseTitle: "How to Use",
    youtubeTitle: "Video Tutorial",
    updatedAt: "2026-09-01T02:40:13.491Z",
    createdAt: "2026-09-01T02:40:13.491Z"
  },
  {
    id: "dl_1788230386201",
    files: [
      {
        title: "Modx",
        category: "App",
        tags: "Antiban",
        imageUrl: "",
        buttonText: "Download Free APK",
        downloadLink: "",
        previewImages: []
      }
    ],
    boxDate: "20 August 2026",
    howToUse: "",
    youtubeLinks: [],
    howToUseTitle: "How to Use",
    youtubeTitle: "Video Tutorial",
    updatedAt: "2026-09-01T02:39:46.201Z",
    createdAt: "2026-09-01T02:39:46.201Z"
  },
  {
    id: "dl_1788184610951",
    files: [
      {
        title: "Kayes Ahmmed",
        category: "File",
        tags: "Antiban",
        imageUrl: "/uploads/img_dl_1788184610951_0.png",
        buttonText: "Download APK",
        downloadLink: "",
        previewImages: [
          "/uploads/preview_dl_1788184610951_1.png",
          "/uploads/preview_dl_1788184610951_2.jpg"
        ]
      },
      {
        title: "kayes Ahmmed 1",
        category: "App",
        tags: "Antiban",
        imageUrl: "",
        buttonText: "Download Free APK",
        downloadLink: "",
        previewImages: [
          "/uploads/preview_dl_1788184610951_3.png"
        ]
      }
    ],
    boxDate: "10 AUGUST 2026",
    howToUse: "he \njsjs",
    youtubeLinks: [],
    howToUseTitle: "How to Use",
    youtubeTitle: "Video Tutorial",
    updatedAt: "2026-08-31T13:58:52.822Z",
    createdAt: "2026-08-31T13:56:50.951Z"
  },
  {
    id: "dl_1788102419937",
    files: [
      {
        title: "Kayes",
        category: "App",
        tags: "antiban",
        imageUrl: "/uploads/img_dl_1788102419937_4.png",
        buttonText: "Download Free APK",
        downloadLink: "",
        previewImages: [
          "/uploads/preview_dl_1788102419937_5.jpg"
        ]
      }
    ],
    boxDate: "12 AUGUST 2026",
    howToUse: "hi\nffs",
    youtubeLinks: [
      {
        title: "tutorial",
        url: "https://youtu.be/FQ0Jf8kxMgg?si=S_f2qhEN_LDq51d4"
      }
    ],
    howToUseTitle: "How to Use",
    youtubeTitle: "Video Tutorial",
    updatedAt: "2026-08-30T15:06:59.937Z",
    createdAt: "2026-08-30T15:06:59.937Z"
  }
];

const getInitialDownloads = () => {
  try {
    const memoryData = dataCache.cache.get("downloads");
    if (Array.isArray(memoryData) && memoryData.length > 0) return memoryData;

    const cached = localStorage.getItem("cached_downloads") || localStorage.getItem("cached_json_downloads");
    if (cached) {
      const parsed = JSON.parse(cached);
      if (Array.isArray(parsed) && parsed.length > 0) return parsed;
    }
  } catch (e) {}
  return defaultInitialDownloads;
};

export default function DownloadSection({ t, isDark }: { t: Theme; isDark?: boolean }) {
  const [downloads, setDownloads] = useState<any[]>(getInitialDownloads);
  const [openHowToUseMap, setOpenHowToUseMap] = useState<Record<string, boolean>>({});
    const [fullscreenGallery, setFullscreenGallery] = useState<{images: string[], index: number} | null>(null);

  const handleNextImage = (e: React.MouseEvent) => {
    e.stopPropagation();
    if (fullscreenGallery) {
      setFullscreenGallery({
        ...fullscreenGallery,
        index: (fullscreenGallery.index + 1) % fullscreenGallery.images.length
      });
    }
  };

  const handlePrevImage = (e: React.MouseEvent) => {
    e.stopPropagation();
    if (fullscreenGallery) {
      setFullscreenGallery({
        ...fullscreenGallery,
        index: (fullscreenGallery.index - 1 + fullscreenGallery.images.length) % fullscreenGallery.images.length
      });
    }
  };
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

  const rawDownloads = downloads.length > 0 ? downloads : defaultInitialDownloads;
  const itemsPerPage = 4;
  const totalItems = rawDownloads.length;
  const totalPages = Math.ceil(totalItems / itemsPerPage);
  
  const maxStartIndex = Math.max(0, totalItems - itemsPerPage);
  const rawStartIndex = (currentPage - 1) * itemsPerPage;
  const startIndex = Math.min(rawStartIndex, maxStartIndex);
  
  const displayDownloads = rawDownloads.slice(startIndex, startIndex + itemsPerPage);

  return (
    <section id="download" className="relative py-16 sm:py-20 px-4 sm:px-8 lg:px-14 max-w-7xl mx-auto">
      <div className="flex flex-col gap-6 w-full">
        <div className="text-center mb-16 px-4 sm:px-8 lg:px-14 relative z-10 w-full max-w-7xl mx-auto">
          <h2 className="text-4xl sm:text-5xl lg:text-6xl font-black mb-4 tracking-tight" style={{ color: t.text }}>Download</h2>
          <p className="text-base sm:text-lg md:text-xl font-semibold max-w-xl mx-auto" style={{ color: t.subtext }}>Get the latest updates and mod files.</p>
        </div>
        
        <div className="relative w-full">
          <div className="w-full flex flex-col gap-6">
            {displayDownloads.map((dl, idx) => {
              const isHowToUseOpen = openHowToUseMap[dl.id] || false;
              
              const files = (dl.files && dl.files.length > 0) ? dl.files : [{ title: dl.title, category: dl.category, tags: dl.tags, imageUrl: dl.imageUrl, buttonText: dl.buttonText, downloadLink: dl.downloadLink, previewImages: dl.previewImages }];
              const ytLinks = (dl.youtubeLinks && dl.youtubeLinks.length > 0) ? dl.youtubeLinks : (dl.youtubeLink ? [dl.youtubeLink] : []);
              
              const howToUseSteps = dl.howToUse ? dl.howToUse.split('\n').filter((l: string) => l.trim() !== '') : [];
              const downloadFiles = files.filter((f: any) => f.downloadLink && f.downloadLink.trim() !== "");
              return (
                <div
                  key={`${currentPage}-${dl.id}`}
                  id={`download-${dl.id}`}
                  className="w-full max-w-7xl mx-auto px-5 sm:px-8 lg:px-10 py-8 sm:py-10 flex flex-col gap-6 relative overflow-hidden rounded-3xl mb-8"
              style={{
                background: isDark ? "rgba(13, 17, 28, 0.88)" : "rgba(255, 255, 255, 0.88)",
                backdropFilter: "blur(20px)",
                WebkitBackdropFilter: "blur(20px)",
                border: isDark ? "1px solid rgba(255, 255, 255, 0.12)" : "1px solid rgba(0, 0, 0, 0.08)",
                boxShadow: isDark ? "0 16px 40px -12px rgba(0, 0, 0, 0.6)" : "0 16px 40px -12px rgba(0, 0, 0, 0.08)"
              }}
            >
              {/* Radial glow background accents */}
              <div className="absolute top-0 right-0 w-96 h-96 pointer-events-none rounded-full filter blur-3xl opacity-15" style={{ background: "radial-gradient(circle, rgba(39,144,255,0.4) 0%, transparent 70%)" }} />
              <div className="absolute bottom-0 left-0 w-80 h-80 pointer-events-none rounded-full filter blur-3xl opacity-15" style={{ background: "radial-gradient(circle, rgba(0,229,209,0.3) 0%, transparent 70%)" }} />

              <div className="relative z-10 flex flex-col gap-6">
                
                <div className="flex flex-wrap items-center justify-between gap-3 border-b pb-4" style={{ borderColor: isDark ? "rgba(255,255,255,0.12)" : "rgba(0,0,0,0.06)" }}>
                  <div className="flex items-center gap-2">
                    <span className="inline-flex items-center gap-2 px-4 py-2 rounded-full text-xs sm:text-sm font-black uppercase tracking-wider text-white backdrop-blur-md shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] border border-[#2790FF]/40" style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}>
                      <svg className="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                      </svg>
                      VERIFIED RELEASE
                    </span>
                  </div>

                  {dl.boxDate && (
                    <div className="flex items-center gap-2 px-4 py-2 rounded-full text-xs sm:text-sm font-extrabold tracking-wide text-white shadow-[0_8px_32px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] border border-[#2790FF]/40 backdrop-blur-md" style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}>
                      <span className="w-2.5 h-2.5 rounded-full bg-white animate-pulse" />
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
                        className="flex flex-col justify-between gap-4 p-5 sm:p-6 rounded-[18px] transition-all duration-300 overflow-hidden group" 
                        style={{ 
                          background: isDark ? "rgba(22, 28, 44, 0.85)" : "rgba(245, 247, 250, 0.9)",
                          backdropFilter: "blur(14px)",
                          WebkitBackdropFilter: "blur(14px)",
                          border: isDark ? "1px solid rgba(255, 255, 255, 0.1)" : "1px solid rgba(0, 0, 0, 0.06)",
                          boxShadow: "0 8px 24px 0 rgba(0, 0, 0, 0.18)"
                        }}
                      >
                        <div className="flex flex-col gap-3">
                          <div className="flex items-start gap-4">
                            {file.imageUrl ? (
                              <img src={file.imageUrl} className="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl object-cover shadow-lg border border-white/30 shrink-0" alt="Icon" />
                            ) : (
                              <div className="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl bg-white text-slate-900 flex items-center justify-center shrink-0 shadow-lg border border-white/40">
                                <svg className="w-10 h-10 text-slate-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">
                                  <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                                </svg>
                              </div>
                            )}
                            <div className="flex-1 min-w-0">
                              <h3 className="font-['Plus_Jakarta_Sans',sans-serif] font-black text-xl sm:text-2xl lg:text-3xl tracking-tight" style={{ color: t.text }}>{file.title || "Download File"}</h3>
                              <div className="inline-flex items-center px-3.5 py-1.5 mt-2 rounded-xl text-xs sm:text-sm font-extrabold tracking-wide text-white w-fit shadow-[0_4px_16px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] border border-[#2790FF]/40 backdrop-blur-md" style={{ background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)" }}>{file.category || "APK / Mod"}</div>
                            </div>
                          </div>

                          {tagsArray.length > 0 && (
                            <div className="flex flex-wrap gap-2 pt-1.5">
                              {tagsArray.map((tag: string, index: number) => (
                                <span
                                  key={index}
                                  className="px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold transition-all text-white shadow-[0_4px_16px_0_rgba(39,144,255,0.25),_inset_0_1px_0_rgba(255,255,255,0.2)] border border-[#2790FF]/40 backdrop-blur-md"
                                  style={{
                                    background: "linear-gradient(135deg, rgba(39, 144, 255, 0.25) 0%, rgba(39, 144, 255, 0.05) 100%)"
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
                          className="relative overflow-hidden group flex items-center justify-center gap-3 w-full py-4 px-6 rounded-2xl font-['Plus_Jakarta_Sans',sans-serif] font-black text-base sm:text-lg lg:text-xl text-slate-950 transition-all cursor-pointer border border-white/50 mt-3"
                          style={{
                            background: "linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%)",
                            boxShadow: "0 8px 25px rgba(255,255,255,0.2)"
                          }}
                        >
                          <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-gradient-to-r from-transparent via-slate-200/50 to-transparent -translate-x-full group-hover:translate-x-full ease-in-out" style={{ transitionDuration: "1s" }} />
                          <svg className="w-5 h-5 sm:w-6 sm:h-6 relative z-10 animate-bounce text-slate-950" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="3">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                          </svg>
                          <span className="relative z-10 tracking-wide text-slate-950">{file.buttonText || "Download Free APK"}</span>
                        </motion.a>

                      {file.previewImages && file.previewImages.length > 0 && (
                        <div className="mt-4 pt-4 border-t w-full flex flex-col gap-3" style={{ borderColor: isDark ? "rgba(255,255,255,0.15)" : "rgba(0,0,0,0.06)" }}>
                          <span className="text-sm sm:text-base font-extrabold uppercase tracking-widest text-white/90 ml-1">App Previews</span>
                          <div className="flex gap-4 w-full overflow-x-auto pb-4 flex-nowrap scrollbar-hide snap-x snap-mandatory" style={{ WebkitOverflowScrolling: "touch", overscrollBehaviorX: "contain" }} onTouchMove={(e) => e.stopPropagation()}>
                            {file.previewImages.map((img: string, i: number) => (
                              <div key={i} className="relative w-[150px] sm:w-[180px] aspect-[9/16] shrink-0 rounded-2xl overflow-hidden shadow-2xl border border-white/20 snap-center bg-black/20 cursor-pointer" onClick={() => setFullscreenGallery({images: file.previewImages, index: i})}>
                                <img src={img} alt={`Preview ${i+1}`} draggable={false} className="w-full h-full object-cover hover:scale-105 transition-transform duration-500 select-none" style={{ WebkitUserDrag: "none" } as React.CSSProperties} />
                              </div>
                            ))}
                          </div>
                        </div>
                      )}

                      </div>
                    );
                  })}
                </div>

                <div className="flex flex-wrap items-center justify-center gap-3 sm:gap-6 text-xs sm:text-sm md:text-base font-extrabold text-center mt-2 text-white/90">
                  <span className="flex items-center gap-1.5">
                    <svg className="w-4 h-4 text-[#16CF83]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="3">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                    Fast Speed
                  </span>
                  <span>•</span>
                  <span className="flex items-center gap-1.5">
                    <svg className="w-4 h-4 text-[#16CF83]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="3">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                    </svg>
                    Virus Tested
                  </span>
                  <span>•</span>
                  <span className="flex items-center gap-1.5">
                    <svg className="w-4 h-4 text-[#16CF83]" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="3">
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
                        borderColor: "rgba(255,255,255,0.18)",
                        background: "rgba(255,255,255,0.05)",
                        backdropFilter: "blur(12px)",
                        WebkitBackdropFilter: "blur(12px)",
                      }}
                    >
                      <div className="flex items-center gap-4 text-left">
                        <div className="w-12 h-12 rounded-2xl bg-white text-slate-900 flex items-center justify-center shrink-0 shadow-lg border border-white/40">
                          <svg className="w-6 h-6 text-slate-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                          </svg>
                        </div>
                        <div>
                          <h3 className="font-['Plus_Jakarta_Sans',sans-serif] font-black text-xl sm:text-2xl text-white">{dl.howToUseTitle || "How to Use"}</h3>
                          <p className="text-xs sm:text-sm font-bold mt-1 opacity-90 text-white/80">
                            Click here for step-by-step setup guide
                          </p>
                        </div>
                      </div>
                      <div className="flex items-center gap-2.5">
                        <span className="text-xs sm:text-sm font-bold hidden sm:inline transition-colors text-white/80">
                          {isHowToUseOpen ? "Close guide" : "Expand guide"}
                        </span>
                        <motion.div 
                          animate={{
                            rotate: isHowToUseOpen ? 180 : 0,
                            backgroundColor: "rgba(255,255,255,0.15)",
                            color: "#ffffff",
                            boxShadow: "0 0 0px transparent"
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
                            className="mt-3 p-5 sm:p-6 rounded-[24px] flex flex-col gap-4 relative overflow-hidden transition-all duration-300"
                            style={{
                              background: "rgba(255, 255, 255, 0.08)",
                              backdropFilter: "blur(12px)",
                              WebkitBackdropFilter: "blur(12px)",
                              border: "1px solid rgba(255, 255, 255, 0.2)",
                              boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                            }}
                          >
                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 relative z-10">
                              {howToUseSteps.map((step: string, i: number) => {
                                return (
                                  <div
                                    key={i}
                                    className="p-4 sm:p-5 rounded-[18px] flex flex-col gap-2.5 relative overflow-hidden transition-all duration-300 hover:translate-y-[-2px]"
                                    style={{
                                      background: "rgba(255, 255, 255, 0.03)",
                                      backdropFilter: "blur(12px)",
                                      WebkitBackdropFilter: "blur(12px)",
                                      border: "1px solid rgba(255, 255, 255, 0.1)",
                                      boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                                    }}
                                  >
                                    <div className="flex items-center justify-between gap-2">
                                      <span
                                        className="font-mono font-black text-xs sm:text-sm px-3.5 py-1.5 rounded-lg bg-white/20 text-white shadow-sm border border-white/30 backdrop-blur-md"
                                      >
                                        STEP 0{i + 1}
                                      </span>
                                    </div>
                                    <p className="font-['Plus_Jakarta_Sans',sans-serif] text-sm sm:text-base leading-relaxed mt-2 text-white font-bold tracking-wide drop-shadow-sm">
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
                                      <h3 className="font-['Plus_Jakarta_Sans',sans-serif] font-black text-lg sm:text-xl text-white">{dl.youtubeTitle || "Video Tutorial"}</h3>
                                      <span className="px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider" style={{ background: "rgba(255,0,0,0.2)", color: "#FF6B6B", border: "1px solid rgba(255,0,0,0.4)" }}>
                                        YouTube Guide
                                      </span>
                                    </div>
                                    <p className="text-xs sm:text-sm font-medium mt-1 text-white/80">
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
            </div>
          );
        })}
          </div>
        </div>

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
      </div>

      
        <AnimatePresence>
        {fullscreenGallery && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setFullscreenGallery(null)}
            className="fixed inset-0 z-[9999] flex items-center justify-center bg-black/95 p-4 cursor-zoom-out backdrop-blur-sm"
          >
            <button 
              onClick={(e) => {
                e.stopPropagation();
                setFullscreenGallery(null);
              }}
              className="absolute top-6 right-6 sm:top-10 sm:right-10 w-12 h-12 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/25 text-white backdrop-blur-md border border-white/20 transition-all z-50"
              aria-label="Close fullscreen"
            >
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>

            {fullscreenGallery.images.length > 1 && (
              <>
                <button
                  onClick={handlePrevImage}
                  className="absolute left-2 sm:left-10 top-1/2 -translate-y-1/2 w-12 h-12 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/25 text-white backdrop-blur-md border border-white/20 transition-all z-50 cursor-pointer"
                >
                  <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
                  </svg>
                </button>
                <button
                  onClick={handleNextImage}
                  className="absolute right-2 sm:right-10 top-1/2 -translate-y-1/2 w-12 h-12 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/25 text-white backdrop-blur-md border border-white/20 transition-all z-50 cursor-pointer"
                >
                  <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
                  </svg>
                </button>
              </>
            )}

            <motion.div
              key={fullscreenGallery.index}
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              transition={{ duration: 0.2 }}
              drag="x"
              dragConstraints={{ left: 0, right: 0 }}
              dragElastic={0.2}
              onDragEnd={(e, { offset, velocity }) => {
                const swipe = Math.abs(offset.x) * velocity.x;
                if (swipe < -100) {
                  // Swipe Left (Next)
                  handleNextImage(e as unknown as React.MouseEvent);
                } else if (swipe > 100) {
                  // Swipe Right (Prev)
                  handlePrevImage(e as unknown as React.MouseEvent);
                }
              }}
              className="w-full h-full flex items-center justify-center cursor-grab active:cursor-grabbing"
              onClick={(e) => e.stopPropagation()}
            >
              <img
                src={fullscreenGallery.images[fullscreenGallery.index]}
                alt={`Fullscreen App Preview ${fullscreenGallery.index + 1}`}
                className="object-contain rounded-xl pointer-events-none"
                style={{ maxHeight: "90vh", maxWidth: "90vw" }}
              />
            </motion.div>
            
            {fullscreenGallery.images.length > 1 && (
              <div className="absolute bottom-6 left-1/2 -translate-x-1/2 flex gap-2 z-50">
                {fullscreenGallery.images.map((_, idx) => (
                  <div 
                    key={idx} 
                    className={`w-2 h-2 rounded-full transition-all duration-300 ${idx === fullscreenGallery.index ? 'bg-white scale-125' : 'bg-white/30'}`}
                  />
                ))}
              </div>
            )}
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
