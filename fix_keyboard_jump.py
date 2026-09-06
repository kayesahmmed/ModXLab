import re

file_path = "./artifacts/cinematic-scroll-site/src/components/ScrollFrameSequence.tsx"
with open(file_path, "r") as f:
    content = f.read()

old_refs = """  const animationFrameRef = useRef<number | undefined>(undefined);
  const drawFrameRef = useRef<(() => void) | undefined>(undefined);
  const reducedMotionRef = useRef(false);
  const lastDrawnFrameRef = useRef(-1);
  const needsResizeRedrawRef = useRef(true);"""

new_refs = """  const animationFrameRef = useRef<number | undefined>(undefined);
  const drawFrameRef = useRef<(() => void) | undefined>(undefined);
  const reducedMotionRef = useRef(false);
  const lastDrawnFrameRef = useRef(-1);
  const needsResizeRedrawRef = useRef(true);
  const initialWindowHeightRef = useRef(window.innerHeight);
  const initialWindowWidthRef = useRef(window.innerWidth);"""

content = content.replace(old_refs, new_refs)

old_resize = """    const resizeCanvas = () => {
      const viewportWidth = window.innerWidth;
      const viewportHeight = window.innerHeight;"""

new_resize = """    const resizeCanvas = () => {
      const viewportWidth = window.innerWidth;
      // Only update cached height if width changed (e.g. orientation change), 
      // preventing virtual keyboard from messing up the scroll range on mobile
      if (Math.abs(viewportWidth - initialWindowWidthRef.current) > 10) {
        initialWindowHeightRef.current = window.innerHeight;
        initialWindowWidthRef.current = viewportWidth;
      }
      const viewportHeight = window.innerHeight;"""

content = content.replace(old_resize, new_resize)

old_update = """    const updateTargetFrame = () => {
      const docHeight = document.documentElement.scrollHeight;
      const windowHeight = window.innerHeight;
      const scrollRange = Math.max(docHeight - windowHeight, 1);
      
      // Map exactly to the scroll
      const scrollProgress = clamp(window.scrollY / scrollRange, 0, 1);"""

new_update = """    const updateTargetFrame = () => {
      const docHeight = document.documentElement.scrollHeight;
      const windowHeight = initialWindowHeightRef.current; // Use stable height
      const scrollRange = Math.max(docHeight - windowHeight, 1);
      
      // Map exactly to the scroll
      const scrollProgress = clamp(window.scrollY / scrollRange, 0, 1);"""

content = content.replace(old_update, new_update)

with open(file_path, "w") as f:
    f.write(content)

