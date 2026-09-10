import { useEffect, useRef } from "react";

const FRAME_COUNT = 208;
const FRAME_WIDTH = 1080;
const FRAME_HEIGHT = 1920;

function frameUrl(index: number) {
  let base = import.meta.env.BASE_URL || "/";
  if (base === "./" || base === "") {
    base = window.location.pathname.includes("/Web") ? "/Web/" : "/";
  }
  const cleanBase = base.endsWith("/") ? base : `${base}/`;
  return `${cleanBase}scroll-frames/ezgif-frame-${String(index + 1).padStart(3, "0")}.webp`;
}

function clamp(value: number, min: number, max: number) {
  return Math.min(Math.max(value, min), max);
}

export default function ScrollFrameSequence({ onProgress }: { onProgress?: (progress: number) => void }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frameImagesRef = useRef<HTMLImageElement[]>([]);
  const currentFrameRef = useRef(0);
  const targetFrameRef = useRef(0);
  const lastVisibleFrameRef = useRef<number>(-1);
  const animationFrameRef = useRef<number | undefined>(undefined);
  const drawFrameRef = useRef<(() => void) | undefined>(undefined);
  const reducedMotionRef = useRef(false);
  const lastDrawnFrameRef = useRef(-1);
  const needsResizeRedrawRef = useRef(true);
  const initialWindowHeightRef = useRef(window.innerHeight);
  const initialWindowWidthRef = useRef(window.innerWidth);
  const cachedScrollMaxRef = useRef<number>(-1);
  const anchorScrollYRef = useRef<number>(0);
  const anchorProgressRef = useRef<number>(0);

  useEffect(() => {
    let isMounted = true;
    const canvas = canvasRef.current;
    if (!canvas) return;

    const context = canvas.getContext("2d", { alpha: true });
    if (!context) return;

    const mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    reducedMotionRef.current = mediaQuery.matches;

    const resizeCanvas = () => {
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
      canvas.style.height = `${stableHeight}px`;
      canvas.style.left = "0px";
      canvas.style.top = "0px";
      context.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
      context.imageSmoothingEnabled = true;
      needsResizeRedrawRef.current = true;
      drawFrameRef.current?.();
    };

    const drawSingleFrame = () => {
      const viewportWidth = initialWindowWidthRef.current;
      const viewportHeight = initialWindowHeightRef.current;

      const frameIndex = clamp(
        Math.round(currentFrameRef.current),
        0,
        FRAME_COUNT - 1,
      );

      // PERFORMANCE FIX: Only redraw if the frame index actually changed or canvas resized
      if (frameIndex === lastDrawnFrameRef.current && !needsResizeRedrawRef.current) {
        return;
      }

      // Find the closest loaded frame (fallback to older frames if current isn't loaded)
      let imageToDraw = frameImagesRef.current[frameIndex];
      let drewFallback = false;
      
      if (!imageToDraw || !imageToDraw.complete) {
         let bestFallback = -1;
         // Look back up to 12 frames to find a recently loaded frame.
         // This prevents the "fast-forward playback" effect when scrolling very fast,
         // by refusing to show frames that are too far behind the user's scroll position.
         for(let i = frameIndex - 1; i >= Math.max(0, frameIndex - 12); i--) {
            if (frameImagesRef.current[i]?.complete) {
               bestFallback = i;
               break;
            }
         }
         
         if (bestFallback !== -1 && bestFallback > lastVisibleFrameRef.current) {
             imageToDraw = frameImagesRef.current[bestFallback];
             drewFallback = true;
         } else {
             // Frame is not loaded and no close fallback found. 
             // If canvas is still valid, we just do nothing and keep previous visual.
             if (!needsResizeRedrawRef.current && lastVisibleFrameRef.current !== -1) {
                lastDrawnFrameRef.current = -1; // Force retry later
                return;
             }
             
             // If canvas was resized or cleared, we MUST draw something. Fallback to last visible.
             if (lastVisibleFrameRef.current !== -1 && frameImagesRef.current[lastVisibleFrameRef.current]?.complete) {
                 imageToDraw = frameImagesRef.current[lastVisibleFrameRef.current];
                 drewFallback = true;
             }
         }
      }

      // If STILL no image, try finding any loaded frame (like frame 0)
      if (!imageToDraw || !imageToDraw.complete) {
         for(let i = 0; i < FRAME_COUNT; i++) {
            if (frameImagesRef.current[i]?.complete) {
               imageToDraw = frameImagesRef.current[i];
               drewFallback = true;
               break;
            }
         }
      }

      if (imageToDraw?.complete && imageToDraw.naturalWidth > 0) {
        context.clearRect(0, 0, viewportWidth, viewportHeight);

        const imgWidth = imageToDraw.naturalWidth || FRAME_WIDTH;
        const imgHeight = imageToDraw.naturalHeight || FRAME_HEIGHT;

        const scale = Math.max(
          viewportWidth / imgWidth,
          viewportHeight / imgHeight,
        );
        const width = imgWidth * scale;
        const height = imgHeight * scale;
        const x = (viewportWidth - width) / 2;
        const y = (viewportHeight - height) / 2;

        context.imageSmoothingEnabled = true;
        context.drawImage(imageToDraw, x, y, width, height);
        
        lastVisibleFrameRef.current = frameImagesRef.current.indexOf(imageToDraw);

        if (!drewFallback) {
          lastDrawnFrameRef.current = frameIndex;
          needsResizeRedrawRef.current = false;
        } else {
          // We drew a fallback, force a redraw next time
          lastDrawnFrameRef.current = -1;
        }
      } else {
        // We failed to draw anything valid, must retry
        lastDrawnFrameRef.current = -1;
      }
    };

    const drawFrame = () => {
      drawSingleFrame();
    };

    drawFrameRef.current = drawFrame;

    const updateTargetFrame = () => {
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
    };

    const animate = () => {
      const difference = targetFrameRef.current - currentFrameRef.current;
      currentFrameRef.current +=
        reducedMotionRef.current ? difference : difference * 0.35; // Snappier easing

      if (Math.abs(difference) > 0.001 || lastDrawnFrameRef.current === -1) {
        drawFrame();
      }

      animationFrameRef.current = window.requestAnimationFrame(animate);
    };

    const handleMotionPreferenceChange = (event: MediaQueryListEvent) => {
      reducedMotionRef.current = event.matches;
      updateTargetFrame();
    };

    resizeCanvas();
    updateTargetFrame();
    window.addEventListener("resize", resizeCanvas, { passive: true });
    window.addEventListener("scroll", updateTargetFrame, { passive: true });
    mediaQuery.addEventListener("change", handleMotionPreferenceChange);
    


    const loadAllFrames = async () => {
      let loadedCount = 0;
      const loadFrame = (index: number) => {
        return new Promise<void>((resolve) => {
          if (!isMounted) return resolve();
          const image = new Image();
          image.decoding = "async";
          image.onload = () => {
            frameImagesRef.current[index] = image;
            if (Math.round(currentFrameRef.current) === index || lastDrawnFrameRef.current === -1) {
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
          };
          image.src = frameUrl(index);
        });
      };

      // 1. Load frame 0 first to show it immediately
      await loadFrame(0);

      // 2. Load sparse frames (every 10th) so fast scrolling has fallbacks
      const sparsePromises = [];
      for (let i = 10; i < FRAME_COUNT; i += 10) {
        sparsePromises.push(loadFrame(i));
      }
      await Promise.all(sparsePromises);

      // 3. Load remaining frames in small batches to prevent network/CPU saturation (lag)
      const batchSize = 6;
      for (let i = 1; i < FRAME_COUNT; i += batchSize) {
        if (!isMounted) return;
        const promises = [];
        for (let j = 0; j < batchSize && i + j < FRAME_COUNT; j++) {
          if ((i + j) % 10 !== 0) { // Skip already loaded sparse frames
            promises.push(loadFrame(i + j));
          }
        }
        await Promise.all(promises);
      }
    };

    loadAllFrames();

    animationFrameRef.current = window.requestAnimationFrame(animate);

    return () => {
      isMounted = false;

      window.removeEventListener("resize", resizeCanvas);
      window.removeEventListener("scroll", updateTargetFrame);
      mediaQuery.removeEventListener("change", handleMotionPreferenceChange);
      if (animationFrameRef.current) {
        window.cancelAnimationFrame(animationFrameRef.current);
      }
      drawFrameRef.current = undefined;
      frameImagesRef.current = [];
    };
  }, []);

  return (
    <div className="fixed inset-0 z-0 pointer-events-none w-full h-full overflow-hidden">
      <canvas
        ref={canvasRef}
        aria-hidden="true"
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          opacity: 1,
          filter: "none",
        }}
      />
    </div>
  );
}