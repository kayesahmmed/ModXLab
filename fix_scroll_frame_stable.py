import re

file_path = "./artifacts/cinematic-scroll-site/src/components/ScrollFrameSequence.tsx"
with open(file_path, "r") as f:
    content = f.read()

old_resize = """    const resizeCanvas = () => {
      const viewportWidth = window.innerWidth;
      // Only update cached height if width changed (e.g. orientation change), 
      // preventing virtual keyboard from messing up the scroll range on mobile
      if (Math.abs(viewportWidth - initialWindowWidthRef.current) > 10) {
        initialWindowHeightRef.current = window.innerHeight;
        initialWindowWidthRef.current = viewportWidth;
      }
      const viewportHeight = window.innerHeight;
      const pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.round(viewportWidth * pixelRatio);
      canvas.height = Math.round(viewportHeight * pixelRatio);
      canvas.style.width = "100vw";
      canvas.style.height = "100vh";"""

new_resize = """    const resizeCanvas = () => {
      const viewportWidth = window.innerWidth;
      // Only update cached height if width changed (e.g. orientation change), 
      // preventing virtual keyboard from messing up the scroll range on mobile
      if (Math.abs(viewportWidth - initialWindowWidthRef.current) > 10) {
        initialWindowHeightRef.current = window.innerHeight;
        initialWindowWidthRef.current = viewportWidth;
      }
      
      const stableWidth = initialWindowWidthRef.current;
      const stableHeight = initialWindowHeightRef.current;
      const pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
      
      canvas.width = Math.round(stableWidth * pixelRatio);
      canvas.height = Math.round(stableHeight * pixelRatio);
      canvas.style.width = `${stableWidth}px`;
      canvas.style.height = `${stableHeight}px`;"""

content = content.replace(old_resize, new_resize)

old_draw = """    const drawSingleFrame = () => {
      const viewportWidth = window.innerWidth;
      const viewportHeight = window.innerHeight;"""

new_draw = """    const drawSingleFrame = () => {
      const viewportWidth = initialWindowWidthRef.current;
      const viewportHeight = initialWindowHeightRef.current;"""

content = content.replace(old_draw, new_draw)

with open(file_path, "w") as f:
    f.write(content)

