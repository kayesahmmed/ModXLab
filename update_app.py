import re

file_path = "./artifacts/cinematic-scroll-site/src/app/App.tsx"
with open(file_path, "r") as f:
    content = f.read()

# 1. Add Preloader import
import_preloader = 'import Preloader from "../components/Preloader";\n'
if "import Preloader" not in content:
    content = content.replace('import ScrollFrameSequence from "../components/ScrollFrameSequence";', 
                            'import ScrollFrameSequence from "../components/ScrollFrameSequence";\n' + import_preloader)

# 2. Add loadProgress state to App component
old_state = """export default function App() {
  const [isDark, setIsDark] = useState(true);"""

new_state = """export default function App() {
  const [isDark, setIsDark] = useState(true);
  const [loadProgress, setLoadProgress] = useState(0);"""
content = content.replace(old_state, new_state)

# 3. Add Preloader and update ScrollFrameSequence inside ReactLenis
old_jsx = """    <ReactLenis
      root
      options={{
        lerp: 0.08,
        duration: 1.2,
        smoothWheel: true,
        orientation: "vertical",
        gestureOrientation: "vertical",
        touchMultiplier: 1.5,
        infinite: false,
      }}
      className="min-h-screen relative text-[#151022] selection:bg-[#7B2CBF]/20 selection:text-[#7B2CBF] w-full max-w-[100vw] overflow-x-hidden font-['Plus_Jakarta_Sans',sans-serif]"
      style={{ background: "transparent" }}
    >
      <ScrollFrameSequence />"""

new_jsx = """    <ReactLenis
      root
      options={{
        lerp: 0.08,
        duration: 1.2,
        smoothWheel: true,
        orientation: "vertical",
        gestureOrientation: "vertical",
        touchMultiplier: 1.5,
        infinite: false,
      }}
      className="min-h-screen relative text-[#151022] selection:bg-[#7B2CBF]/20 selection:text-[#7B2CBF] w-full max-w-[100vw] overflow-x-hidden font-['Plus_Jakarta_Sans',sans-serif]"
      style={{ background: "transparent" }}
    >
      <Preloader progress={loadProgress} />
      <ScrollFrameSequence onProgress={setLoadProgress} />"""
content = content.replace(old_jsx, new_jsx)

with open(file_path, "w") as f:
    f.write(content)
print("App.tsx updated")
