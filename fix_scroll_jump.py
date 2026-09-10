import re

file_path = "./artifacts/cinematic-scroll-site/src/components/ScrollFrameSequence.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Add anchor refs
old_refs = """  const needsResizeRedrawRef = useRef(true);
  const initialWindowHeightRef = useRef(window.innerHeight);
  const initialWindowWidthRef = useRef(window.innerWidth);"""

new_refs = """  const needsResizeRedrawRef = useRef(true);
  const initialWindowHeightRef = useRef(window.innerHeight);
  const initialWindowWidthRef = useRef(window.innerWidth);
  const cachedScrollMaxRef = useRef<number>(-1);
  const anchorScrollYRef = useRef<number>(0);
  const anchorProgressRef = useRef<number>(0);"""

content = content.replace(old_refs, new_refs)

old_update = """    const updateTargetFrame = () => {
      const docHeight = document.documentElement.scrollHeight;
      const windowHeight = initialWindowHeightRef.current; // Use stable height
      const scrollRange = Math.max(docHeight - windowHeight, 1);
      
      // Map exactly to the scroll
      const scrollProgress = clamp(window.scrollY / scrollRange, 0, 1);
      
      targetFrameRef.current = reducedMotionRef.current
        ? 0
        : scrollProgress * (FRAME_COUNT - 1);
    };"""

new_update = """    const updateTargetFrame = () => {
      const docHeight = document.documentElement.scrollHeight;
      const windowHeight = initialWindowHeightRef.current;
      const currentScrollMax = Math.max(docHeight - windowHeight, 1);
      
      // If height changed (e.g. accordion open), set anchor to prevent jumping
      if (Math.abs(currentScrollMax - cachedScrollMaxRef.current) > 2) {
        anchorScrollYRef.current = window.scrollY;
        anchorProgressRef.current = (targetFrameRef.current || 0) / (FRAME_COUNT - 1);
        cachedScrollMaxRef.current = currentScrollMax;
      }

      const scrollY = window.scrollY;
      let progress = 0;

      if (anchorScrollYRef.current <= 0 || currentScrollMax <= 0) {
          progress = clamp(scrollY / currentScrollMax, 0, 1);
      } else if (scrollY >= anchorScrollYRef.current) {
          const remainingScroll = currentScrollMax - anchorScrollYRef.current;
          if (remainingScroll <= 0) {
              progress = 1;
          } else {
              progress = anchorProgressRef.current + ((scrollY - anchorScrollYRef.current) / remainingScroll) * (1 - anchorProgressRef.current);
          }
      } else {
          progress = anchorProgressRef.current * (scrollY / anchorScrollYRef.current);
      }
      
      progress = clamp(progress, 0, 1);

      targetFrameRef.current = reducedMotionRef.current
        ? 0
        : progress * (FRAME_COUNT - 1);
    };"""

content = content.replace(old_update, new_update)

old_events = """    window.addEventListener("resize", resizeCanvas, { passive: true });
    window.addEventListener("scroll", updateTargetFrame, { passive: true });
    mediaQuery.addEventListener("change", handleMotionPreferenceChange);
    
    const loadAllFrames = async () => {"""

new_events = """    window.addEventListener("resize", resizeCanvas, { passive: true });
    window.addEventListener("scroll", updateTargetFrame, { passive: true });
    mediaQuery.addEventListener("change", handleMotionPreferenceChange);
    
    const resizeObserver = new ResizeObserver(() => {
      updateTargetFrame();
    });
    if (document.body) resizeObserver.observe(document.body);
    
    const loadAllFrames = async () => {"""

content = content.replace(old_events, new_events)

old_cleanup = """    return () => {
      isMounted = false;
      window.removeEventListener("resize", resizeCanvas);
      window.removeEventListener("scroll", updateTargetFrame);
      mediaQuery.removeEventListener("change", handleMotionPreferenceChange);
      if (animationFrameRef.current) {
        window.cancelAnimationFrame(animationFrameRef.current);
      }"""

new_cleanup = """    return () => {
      isMounted = false;
      resizeObserver.disconnect();
      window.removeEventListener("resize", resizeCanvas);
      window.removeEventListener("scroll", updateTargetFrame);
      mediaQuery.removeEventListener("change", handleMotionPreferenceChange);
      if (animationFrameRef.current) {
        window.cancelAnimationFrame(animationFrameRef.current);
      }"""

content = content.replace(old_cleanup, new_cleanup)

with open(file_path, "w") as f:
    f.write(content)

