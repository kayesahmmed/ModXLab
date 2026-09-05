with open("./artifacts/cinematic-scroll-site/src/app/App.tsx", "r") as f:
    content = f.read()

# syncTouch is what blocks native pull to refresh because it sets touch-action: none under the hood to intercept events
content = content.replace("syncTouch: true,", "syncTouch: false,")

with open("./artifacts/cinematic-scroll-site/src/app/App.tsx", "w") as f:
    f.write(content)
