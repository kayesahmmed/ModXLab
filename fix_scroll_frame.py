import re

file_path = "./artifacts/cinematic-scroll-site/src/components/ScrollFrameSequence.tsx"
with open(file_path, "r") as f:
    content = f.read()

# Remove ResizeObserver code
old_resize_observer = """    const resizeObserver = new ResizeObserver(() => {
      updateTargetFrame();
    });
    resizeObserver.observe(document.documentElement);
    resizeObserver.observe(document.body);"""

content = content.replace(old_resize_observer, "")

old_disconnect = """      resizeObserver.disconnect();"""
content = content.replace(old_disconnect, "")

with open(file_path, "w") as f:
    f.write(content)

