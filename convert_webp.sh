#!/bin/bash
cd ./artifacts/cinematic-scroll-site/public/scroll-frames
echo "Converting JPG to WEBP..."
for file in *.jpg; do
    if [ -f "$file" ]; then
        cwebp -q 80 "$file" -o "${file%.jpg}.webp" >/dev/null 2>&1
        rm "$file"
    fi
done
echo "Done!"
