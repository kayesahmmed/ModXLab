import re

file_path = "./artifacts/cinematic-scroll-site/src/components/ScrollFrameSequence.tsx"

with open(file_path, "r") as f:
    content = f.read()

old_update = """    const updateTargetFrame = () => {
      const docHeight = Math.max(
        document.body.scrollHeight,
        document.body.offsetHeight,
        document.documentElement.clientHeight,
        document.documentElement.scrollHeight,
        document.documentElement.offsetHeight
      );
      const scrollRange = Math.max(docHeight - window.innerHeight, 1);
      
      // Calculate scroll progress with a 99% modifier so the last frame is reached 
      // just before hitting the exact bottom pixel, fixing mobile address bar issues.
      const scrollProgress = clamp(window.scrollY / (scrollRange * 0.99), 0, 1);
      
      targetFrameRef.current = reducedMotionRef.current
        ? 0
        : scrollProgress * (FRAME_COUNT - 1);
    };"""

new_update = """    const updateTargetFrame = () => {
      const docHeight = document.documentElement.scrollHeight;
      const windowHeight = window.innerHeight;
      const scrollRange = Math.max(docHeight - windowHeight, 1);
      
      // Map exactly to the scroll
      const scrollProgress = clamp(window.scrollY / scrollRange, 0, 1);
      
      targetFrameRef.current = reducedMotionRef.current
        ? 0
        : scrollProgress * (FRAME_COUNT - 1);
    };"""
content = content.replace(old_update, new_update)

old_events = """    window.addEventListener("resize", resizeCanvas, { passive: true });
    window.addEventListener("scroll", updateTargetFrame, { passive: true });
    mediaQuery.addEventListener("change", handleMotionPreferenceChange);"""

new_events = """    window.addEventListener("resize", resizeCanvas, { passive: true });
    window.addEventListener("scroll", updateTargetFrame, { passive: true });
    mediaQuery.addEventListener("change", handleMotionPreferenceChange);
    
    const resizeObserver = new ResizeObserver(() => {
      updateTargetFrame();
    });
    resizeObserver.observe(document.documentElement);
    resizeObserver.observe(document.body);"""
content = content.replace(old_events, new_events)

old_cleanup = """      animationFrameRef.current = window.requestAnimationFrame(animate);

    return () => {
      isMounted = false;
      window.removeEventListener("resize", resizeCanvas);
      window.removeEventListener("scroll", updateTargetFrame);
      mediaQuery.removeEventListener("change", handleMotionPreferenceChange);
      if (animationFrameRef.current !== undefined) {
        window.cancelAnimationFrame(animationFrameRef.current);
      }
    };
  }, []);"""

new_cleanup = """      animationFrameRef.current = window.requestAnimationFrame(animate);

    return () => {
      isMounted = false;
      resizeObserver.disconnect();
      window.removeEventListener("resize", resizeCanvas);
      window.removeEventListener("scroll", updateTargetFrame);
      mediaQuery.removeEventListener("change", handleMotionPreferenceChange);
      if (animationFrameRef.current !== undefined) {
        window.cancelAnimationFrame(animationFrameRef.current);
      }
    };
  }, []);"""
content = content.replace(old_cleanup, new_cleanup)

with open(file_path, "w") as f:
    f.write(content)

