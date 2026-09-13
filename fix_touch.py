import re

file_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

old_preview = """<div className="flex gap-4 w-full overflow-x-auto pb-4 flex-nowrap scrollbar-hide snap-x snap-mandatory" style={{ WebkitOverflowScrolling: "touch", overscrollBehaviorX: "contain" }}>"""
new_preview = """<div className="flex gap-4 w-full overflow-x-auto pb-4 flex-nowrap scrollbar-hide snap-x snap-mandatory" style={{ WebkitOverflowScrolling: "touch", overscrollBehaviorX: "contain", touchAction: "pan-x" }}>"""
content = content.replace(old_preview, new_preview)

with open(file_path, "w") as f:
    f.write(content)
print("Updated touch-action for horizontal scroll only")
