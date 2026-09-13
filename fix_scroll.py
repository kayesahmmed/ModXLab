import re

file_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Replace the horizontal scroll container and images
old_preview = """<div className="flex gap-4 w-full overflow-x-auto pb-4 flex-nowrap scrollbar-hide snap-x snap-mandatory" style={{ WebkitOverflowScrolling: "touch", touchAction: "pan-x" }}>
                            {file.previewImages.map((img: string, i: number) => (
                              <div key={i} className="relative w-[150px] sm:w-[180px] aspect-[9/16] shrink-0 rounded-2xl overflow-hidden shadow-2xl border border-white/20 snap-center bg-black/20 cursor-pointer" onClick={() => setFullscreenGallery({images: file.previewImages, index: i})}>
                                <img src={img} alt={`Preview ${i+1}`} className="w-full h-full object-cover hover:scale-105 transition-transform duration-500 pointer-events-none" />"""

new_preview = """<div className="flex gap-4 w-full overflow-x-auto pb-4 flex-nowrap scrollbar-hide snap-x snap-mandatory" style={{ WebkitOverflowScrolling: "touch", overscrollBehaviorX: "contain" }}>
                            {file.previewImages.map((img: string, i: number) => (
                              <div key={i} className="relative w-[150px] sm:w-[180px] aspect-[9/16] shrink-0 rounded-2xl overflow-hidden shadow-2xl border border-white/20 snap-center bg-black/20 cursor-pointer" onClick={() => setFullscreenGallery({images: file.previewImages, index: i})}>
                                <img src={img} alt={`Preview ${i+1}`} draggable={false} className="w-full h-full object-cover hover:scale-105 transition-transform duration-500 select-none" style={{ WebkitUserDrag: "none" }} />"""

content = content.replace(old_preview, new_preview)

with open(file_path, "w") as f:
    f.write(content)
print("Updated scroll section")
