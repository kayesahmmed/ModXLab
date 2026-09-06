import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"

with open(file_path, "r") as f:
    content = f.read()

# Fix Left Column
old_left = """        <div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] backdrop-blur-[12px] transition-all duration-700 border h-full"
          style={{
            background: "rgba(255, 255, 255, 0.12)",
            backdropFilter: "blur(12px)",
            WebkitBackdropFilter: "blur(12px)",
            border: "1px solid rgba(255, 255, 255, 0.2)",
            boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
          }}
        >"""
new_left = """        <div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] backdrop-blur-xl transition-all duration-700 border border-white/20 h-full bg-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.15)]"
        >"""
content = content.replace(old_left, new_left)


# Fix Right Column
old_right = """        <div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] backdrop-blur-[12px] transition-all duration-700 border h-full"
          style={{
            background: "rgba(255, 255, 255, 0.12)",
            backdropFilter: "blur(12px)",
            WebkitBackdropFilter: "blur(12px)",
            border: "1px solid rgba(255, 255, 255, 0.2)",
            boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
          }}
        >"""
new_right = """        <div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] backdrop-blur-xl transition-all duration-700 border border-white/20 h-full bg-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.15)]"
        >"""
content = content.replace(old_right, new_right)

with open(file_path, "w") as f:
    f.write(content)
