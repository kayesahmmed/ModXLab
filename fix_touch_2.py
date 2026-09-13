import re

file_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Completely remove touch-action to let native scrolling handle it
# Sometimes touch-action: pan-x prevents any scrolling on certain mobile browsers
old_preview = """<div className="flex gap-4 w-full overflow-x-auto pb-4 flex-nowrap scrollbar-hide snap-x snap-mandatory" style={{ WebkitOverflowScrolling: "touch", overscrollBehaviorX: "contain", touchAction: "pan-x" }}>"""
new_preview = """<div className="flex gap-4 w-full overflow-x-auto pb-4 flex-nowrap scrollbar-hide snap-x snap-mandatory" style={{ WebkitOverflowScrolling: "touch", overscrollBehaviorX: "contain" }} onTouchMove={(e) => e.stopPropagation()}>"""
content = content.replace(old_preview, new_preview)

with open(file_path, "w") as f:
    f.write(content)
print("Updated scroll handling")
