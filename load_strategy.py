import re

file_path = "./artifacts/cinematic-scroll-site/src/components/ScrollFrameSequence.tsx"
with open(file_path, "r") as f:
    content = f.read()

target = """      // Load frame 0 first to show it immediately
      await loadFrame(0);

      // Load remaining frames in small batches to prevent network/CPU saturation (lag)
      const batchSize = 4;
      for (let i = 1; i < FRAME_COUNT; i += batchSize) {
        if (!isMounted) return;
        const promises = [];
        for (let j = 0; j < batchSize && i + j < FRAME_COUNT; j++) {
          promises.push(loadFrame(i + j));
        }
        await Promise.all(promises);
      }"""

replacement = """      // 1. Load frame 0 first to show it immediately
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
      }"""

content = content.replace(target, replacement)
with open(file_path, "w") as f:
    f.write(content)
print("Updated load strategy")
