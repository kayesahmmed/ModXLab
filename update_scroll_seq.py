import re

file_path = "./artifacts/cinematic-scroll-site/src/components/ScrollFrameSequence.tsx"
with open(file_path, "r") as f:
    content = f.read()

# 1. Update export signature
old_export = "export default function ScrollFrameSequence() {"
new_export = "export default function ScrollFrameSequence({ onProgress }: { onProgress?: (progress: number) => void }) {"
content = content.replace(old_export, new_export)

# 2. Update .jpg to .webp
old_ext = 'return `${cleanBase}scroll-frames/ezgif-frame-${String(index + 1).padStart(3, "0")}.jpg`;'
new_ext = 'return `${cleanBase}scroll-frames/ezgif-frame-${String(index + 1).padStart(3, "0")}.webp`;'
content = content.replace(old_ext, new_ext)

# 3. Add onProgress callback logic in loadAllFrames
old_load = """    const loadAllFrames = async () => {
      const loadFrame = (index: number) => {
        return new Promise<void>((resolve) => {
          if (!isMounted) return resolve();
          const image = new Image();"""

new_load = """    const loadAllFrames = async () => {
      let loadedCount = 0;
      const loadFrame = (index: number) => {
        return new Promise<void>((resolve) => {
          if (!isMounted) return resolve();
          const image = new Image();"""
content = content.replace(old_load, new_load)

old_resolve = """            if (Math.round(currentFrameRef.current) === index || lastDrawnFrameRef.current === -1) {
              drawFrame();
            }
            resolve();
          };
          image.onerror = () => {
            console.warn(`Failed to load frame ${index}`);
            resolve();
          };"""

new_resolve = """            if (Math.round(currentFrameRef.current) === index || lastDrawnFrameRef.current === -1) {
              drawFrame();
            }
            loadedCount++;
            if (onProgress) onProgress(Math.floor((loadedCount / FRAME_COUNT) * 100));
            resolve();
          };
          image.onerror = () => {
            console.warn(`Failed to load frame ${index}`);
            loadedCount++;
            if (onProgress) onProgress(Math.floor((loadedCount / FRAME_COUNT) * 100));
            resolve();
          };"""
content = content.replace(old_resolve, new_resolve)

with open(file_path, "w") as f:
    f.write(content)

print("ScrollFrameSequence updated")
