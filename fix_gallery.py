import re

file_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# 1. Replace the state
old_state = "const [fullscreenImage, setFullscreenImage] = useState<string | null>(null);"
new_state = """  const [fullscreenGallery, setFullscreenGallery] = useState<{images: string[], index: number} | null>(null);

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
  };"""
content = content.replace(old_state, new_state)

# 2. Update the horizontal scroll wrapper for the preview thumbnails
old_preview_scroll = """<div className="flex gap-4 w-full overflow-x-auto pb-4 flex-nowrap scrollbar-hide snap-x touch-pan-x" style={{ WebkitOverflowScrolling: "touch" }}>
                            {file.previewImages.map((img: string, i: number) => (
                              <div key={i} className="relative w-[150px] sm:w-[180px] aspect-[9/16] shrink-0 rounded-2xl overflow-hidden shadow-2xl border border-white/20 snap-center bg-black/20 cursor-pointer" onClick={() => setFullscreenImage(img)}>
                                <img src={img} alt={`Preview ${i+1}`} className="w-full h-full object-cover hover:scale-105 transition-transform duration-500" />"""
new_preview_scroll = """<div className="flex gap-4 w-full overflow-x-auto pb-4 flex-nowrap scrollbar-hide snap-x snap-mandatory" style={{ WebkitOverflowScrolling: "touch", touchAction: "pan-x" }}>
                            {file.previewImages.map((img: string, i: number) => (
                              <div key={i} className="relative w-[150px] sm:w-[180px] aspect-[9/16] shrink-0 rounded-2xl overflow-hidden shadow-2xl border border-white/20 snap-center bg-black/20 cursor-pointer" onClick={() => setFullscreenGallery({images: file.previewImages, index: i})}>
                                <img src={img} alt={`Preview ${i+1}`} className="w-full h-full object-cover hover:scale-105 transition-transform duration-500 pointer-events-none" />"""
content = content.replace(old_preview_scroll, new_preview_scroll)

# 3. Update the fullscreen modal renderer
old_modal = """<AnimatePresence>
        {fullscreenImage && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setFullscreenImage(null)}
            className="fixed inset-0 z-[9999] flex items-center justify-center bg-black/95 p-4 cursor-zoom-out backdrop-blur-sm"
          >
            <button 
              onClick={(e) => {
                e.stopPropagation();
                setFullscreenImage(null);
              }}
              className="absolute top-6 right-6 sm:top-10 sm:right-10 w-12 h-12 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/25 text-white backdrop-blur-md border border-white/20 transition-all z-10"
              aria-label="Close fullscreen"
            >
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
            <motion.img
              initial={{ scale: 0.95, y: 10 }}
              animate={{ scale: 1, y: 0 }}
              exit={{ scale: 0.95, y: 10 }}
              transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
              src={fullscreenImage}
              alt="Fullscreen App Preview"
              className="w-full h-full object-contain rounded-xl"
              style={{ maxHeight: "90vh", maxWidth: "90vw" }}
            />
          </motion.div>
        )}
      </AnimatePresence>"""
new_modal = """<AnimatePresence>
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
      </AnimatePresence>"""
content = content.replace(old_modal, new_modal)

with open(file_path, "w") as f:
    f.write(content)
print("Updated DownloadSection with image gallery and touch fixes")
