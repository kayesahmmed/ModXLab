const fs = require('fs');
const file = 'artifacts/cinematic-scroll-site/src/components/ScrollFrameSequence.tsx';
let content = fs.readFileSync(file, 'utf8');

content = content.replace(
  '// try finding previous loaded frame to avoid blank flashes\n         for(let i = frameIndex - 1; i >= 0; i--) {\n            if (frameImagesRef.current[i]?.complete) {\n               imageToDraw = frameImagesRef.current[i];\n               drewFallback = true;\n               break;\n            }\n         }',
  `// try finding a recently loaded frame nearby to avoid freezing on very old frames, 
         // but limit the search to prevent the "fast-forward video" effect when scrolling fast.
         for(let i = frameIndex - 1; i >= Math.max(0, frameIndex - 5); i--) {
            if (frameImagesRef.current[i]?.complete) {
               imageToDraw = frameImagesRef.current[i];
               drewFallback = true;
               break;
            }
         }
         
         // If no recent frame is loaded, fallback to the last visible frame to prevent playback effect
         if (!imageToDraw && lastDrawnFrameRef.current !== -1 && frameImagesRef.current[lastDrawnFrameRef.current]?.complete) {
             // We can't use lastDrawnFrameRef directly if it was set to -1 on a fallback.
             // Wait, the old code sets lastDrawnFrameRef.current = -1 when drewFallback is true.
         }`
);

fs.writeFileSync(file, content);
