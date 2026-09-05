import re

def process_hero():
    with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
        content = f.read()

    # 1. Fix Search Bar Input Container
    old_input_container = """              <div
                className={`transition-all duration-350 ease-[cubic-bezier(0.16,1,0.3,1)] h-14 flex items-center overflow-hidden rounded-2xl border ${
                  searchOpen ? "w-[260px] sm:w-[320px] opacity-100 border-white/20 pointer-events-auto" : "w-0 opacity-0 border-transparent pointer-events-none"
                }`}
                style={{
                  background: "rgba(255, 255, 255, 0.18)",
                  backdropFilter: "blur(16px)",
                  WebkitBackdropFilter: "blur(16px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                  boxShadow: "0 8px 32px 0 rgba(0,0,0,0.15)",
                }}
              >
                <div className="relative w-full h-full flex items-center">"""
    
    new_input_container = """              <div
                className={`transition-all duration-350 ease-[cubic-bezier(0.16,1,0.3,1)] h-14 flex items-center rounded-2xl border relative ${
                  searchOpen ? "w-[260px] sm:w-[320px] opacity-100 border-white/20 pointer-events-auto" : "w-0 opacity-0 border-transparent pointer-events-none"
                }`}
                style={{
                  boxShadow: "0 8px 32px 0 rgba(0,0,0,0.15)"
                }}
              >
                <div 
                  className="absolute inset-0 rounded-2xl pointer-events-none" 
                  style={{
                    background: "rgba(255, 255, 255, 0.18)",
                    backdropFilter: "blur(16px)",
                    WebkitBackdropFilter: "blur(16px)",
                    WebkitTransform: "translate3d(0,0,0)",
                    transform: "translate3d(0,0,0)",
                    backfaceVisibility: "hidden",
                    WebkitBackfaceVisibility: "hidden"
                  }} 
                />
                <div className="relative w-full h-full flex items-center z-10 overflow-hidden rounded-2xl">"""
                
    content = content.replace(old_input_container, new_input_container)

    # 2. Fix Search Bar Dropdown Container
    # Find the dropdown motion.div
    # className="absolute top-[68px] right-0 w-80 sm:w-96 md:w-[420px] rounded-2xl p-2 z-[9999]"
    
    old_dropdown_style = """                    className="absolute top-[68px] right-0 w-80 sm:w-96 md:w-[420px] rounded-2xl p-2 z-[9999]"
                  style={{
                    background: "rgba(15, 23, 42, 0.95)",
                    backdropFilter: "blur(40px)",
                    WebkitBackdropFilter: "blur(40px)",
                    WebkitTransform: "translate3d(0, 0, 0)",
                    transform: "translate3d(0, 0, 0)",
                    WebkitBackfaceVisibility: "hidden",
                    backfaceVisibility: "hidden",
                    border: "1px solid rgba(255, 255, 255, 0.25)",
                    boxShadow: "0 12px 40px 0 rgba(0, 0, 0, 0.3)",
                    color: "white",
                    
                  }}
                >
                  {filteredResults.length > 0 ? ("""
                  
    # Wait, my previous cleanup might have left willChange: "transform, opacity" but it's removed now!
    # Let's use regex to replace the whole dropdown motion.div opening
    
    dropdown_regex = r'(<motion\.div\s+key="search-dropdown".*?className="absolute top-\[68px\] right-0 w-80 sm:w-96 md:w-\[420px\] rounded-2xl p-2 z-\[9999\]"\s*style=\{\{.*?\}\}\s*>)'
    
    def repl_dropdown(m):
        return """<motion.div
                    key="search-dropdown"
                    initial={{ opacity: 0, y: -10, scale: 0.98 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -5, scale: 0.98 }}
                    transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
                    className="absolute top-[68px] right-0 w-80 sm:w-96 md:w-[420px] rounded-2xl z-[9999]"
                    style={{
                      border: "1px solid rgba(255, 255, 255, 0.25)",
                      boxShadow: "0 12px 40px 0 rgba(0, 0, 0, 0.3)",
                      color: "white"
                    }}
                  >
                    <div 
                      className="absolute inset-0 rounded-2xl pointer-events-none" 
                      style={{
                        background: "rgba(15, 23, 42, 0.95)",
                        backdropFilter: "blur(40px)",
                        WebkitBackdropFilter: "blur(40px)",
                        WebkitTransform: "translate3d(0,0,0)",
                        transform: "translate3d(0,0,0)",
                        backfaceVisibility: "hidden",
                        WebkitBackfaceVisibility: "hidden"
                      }} 
                    />
                    <div className="relative w-full h-full p-2 z-10">"""
    
    content = re.sub(dropdown_regex, repl_dropdown, content, flags=re.DOTALL)
    
    # Close the extra div for dropdown
    # The end of the dropdown is:
    #                   )}
    #                 </motion.div>
    #               )}
    
    end_dropdown_regex = r'(                  \)\}\n                <\/motion\.div>)'
    content = re.sub(end_dropdown_regex, r'                  )}\n                    </div>\n                </motion.div>', content)

    with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
        f.write(content)

process_hero()
