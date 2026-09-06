import re

def update_file(path, old, new):
    with open(path, "r") as f:
        content = f.read()
    content = content.replace(old, new)
    with open(path, "w") as f:
        f.write(content)

# FAQ SECTION
faq_path = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"

update_file(faq_path, '<div className="flex flex-col items-center gap-4 mb-10">', '<div className="flex flex-col items-center gap-4 mb-16">')

old_faq_item_main = """              <motion.div 
                key={faq.id} 
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, amount: 0.1 }}
                transition={{ duration: 0.5, delay: i * 0.1, ease: [0.16, 1, 0.3, 1] }}
                className="rounded-[24px] relative group"
                style={{ willChange: 'transform, opacity', WebkitBackfaceVisibility: 'hidden', backfaceVisibility: 'hidden' }}
              >
                <div className={`absolute inset-0 rounded-[24px] pointer-events-none z-0 transition-all duration-150 bg-white/10 backdrop-blur-md ${isOpen ? 'border border-[#16CF83]/40 shadow-[0_8px_32px_0_rgba(22,207,131,0.25)]' : 'border border-white/20 shadow-xl'}`} />
                <div className="relative z-10 w-full rounded-[24px] overflow-hidden">"""

new_faq_item_main = """              <motion.div 
                key={faq.id} 
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, amount: 0.1 }}
                transition={{ duration: 0.5, delay: i * 0.1, ease: [0.16, 1, 0.3, 1] }}
                className="rounded-[24px] relative group overflow-hidden transition-all duration-300"
                style={{ 
                  willChange: 'transform, opacity', 
                  WebkitBackfaceVisibility: 'hidden', 
                  backfaceVisibility: 'hidden',
                  background: "rgba(255, 255, 255, 0.12)",
                  backdropFilter: "blur(12px)",
                  WebkitBackdropFilter: "blur(12px)",
                  border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.2)",
                  boxShadow: isOpen ? "0 8px 32px 0 rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                  transform: "translateZ(0)"
                }}
              >
                <div className="relative z-10 w-full h-full">"""

update_file(faq_path, old_faq_item_main, new_faq_item_main)

old_faq_item_modal = """                      <div
                        key={faq.id}
                        className="rounded-2xl relative transition-all duration-150"
                        style={{ willChange: 'transform, opacity', WebkitBackfaceVisibility: 'hidden', backfaceVisibility: 'hidden' }}
                      >
                        <div className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-150 bg-white/5 backdrop-blur-md ${isOpen ? 'border border-[#16CF83]/40 shadow-[0_4px_20px_-5px_rgba(22,207,131,0.25)]' : 'border border-white/10'}`} />
                        <div className="relative z-10 rounded-2xl overflow-hidden w-full">"""

new_faq_item_modal = """                      <div
                        key={faq.id}
                        className="rounded-[18px] relative transition-all duration-300 overflow-hidden"
                        style={{ 
                          willChange: 'transform, opacity', 
                          WebkitBackfaceVisibility: 'hidden', 
                          backfaceVisibility: 'hidden',
                          background: "rgba(255, 255, 255, 0.12)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.2)",
                          boxShadow: isOpen ? "0 4px 20px -5px rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                          transform: "translateZ(0)"
                        }}
                      >
                        <div className="relative z-10 w-full h-full">"""

update_file(faq_path, old_faq_item_modal, new_faq_item_modal)


# FEATURES SECTION
features_path = "./artifacts/cinematic-scroll-site/src/components/FeaturesSection.tsx"
update_file(features_path, '<div className="text-center mb-10 relative z-10">', '<div className="text-center mb-16 relative z-10">')


# DOWNLOAD SECTION
download_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"
update_file(download_path, '<div className="text-center mb-10 px-4 sm:px-8 lg:px-14 relative z-10 w-full max-w-7xl mx-auto">', '<div className="text-center mb-16 px-4 sm:px-8 lg:px-14 relative z-10 w-full max-w-7xl mx-auto">')

# Also fix the Download section box blur to match exactly
old_dl_box = """                      <div 
                        key={fIdx} 
                        className="flex flex-col justify-between gap-4 p-5 sm:p-6 rounded-2xl border transition-all duration-300 hover:border-white/40 shadow-xl backdrop-blur-xl" 
                        style={{ 
                          background: isDark ? "rgba(255, 255, 255, 0.06)" : "rgba(248, 250, 252, 0.85)", 
                          borderColor: isDark ? "rgba(255,255,255,0.15)" : "rgba(0,0,0,0.08)" 
                        }}
                      >"""

new_dl_box = """                      <div 
                        key={fIdx} 
                        className="flex flex-col justify-between gap-4 p-5 sm:p-6 rounded-[18px] transition-all duration-300 overflow-hidden group" 
                        style={{ 
                          background: "rgba(255, 255, 255, 0.12)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          border: "1px solid rgba(255, 255, 255, 0.2)",
                          boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                          transform: "translateZ(0)"
                        }}
                      >"""

update_file(download_path, old_dl_box, new_dl_box)

# We also need to fix the how to use dropdown section box blur inside DownloadSection
old_howtouse = """                          <div
                            className="mt-3 p-5 sm:p-6 rounded-[24px] flex flex-col gap-4 relative overflow-hidden shadow-2xl transition-colors duration-300"
                            style={{
                              background: isDark ? "rgba(255, 255, 255, 0.06)" : "rgba(255, 255, 255, 0.65)",
                              backdropFilter: "blur(24px)",
                              WebkitBackdropFilter: "blur(24px)",
                              border: "1px solid rgba(255, 255, 255, 0.2)"
                            }}
                          >"""

new_howtouse = """                          <div
                            className="mt-3 p-5 sm:p-6 rounded-[24px] flex flex-col gap-4 relative overflow-hidden transition-all duration-300"
                            style={{
                              background: "rgba(255, 255, 255, 0.12)",
                              backdropFilter: "blur(12px)",
                              WebkitBackdropFilter: "blur(12px)",
                              border: "1px solid rgba(255, 255, 255, 0.2)",
                              boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                              transform: "translateZ(0)"
                            }}
                          >"""
update_file(download_path, old_howtouse, new_howtouse)

old_howtouse_step = """                                  <div
                                    key={i}
                                    className="p-4 sm:p-5 rounded-2xl flex flex-col gap-2.5 relative overflow-hidden transition-colors duration-300 hover:translate-y-[-2px] hover:border-white/40 shadow-lg"
                                    style={{
                                      background: isDark ? "rgba(255, 255, 255, 0.08)" : "rgba(255, 255, 255, 0.8)",
                                      backdropFilter: "blur(16px)",
                                      WebkitBackdropFilter: "blur(16px)",
                                      border: "1px solid rgba(255, 255, 255, 0.25)"
                                    }}
                                  >"""

new_howtouse_step = """                                  <div
                                    key={i}
                                    className="p-4 sm:p-5 rounded-[18px] flex flex-col gap-2.5 relative overflow-hidden transition-all duration-300 hover:translate-y-[-2px]"
                                    style={{
                                      background: "rgba(255, 255, 255, 0.12)",
                                      backdropFilter: "blur(12px)",
                                      WebkitBackdropFilter: "blur(12px)",
                                      border: "1px solid rgba(255, 255, 255, 0.2)",
                                      boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
                                      transform: "translateZ(0)"
                                    }}
                                  >"""
update_file(download_path, old_howtouse_step, new_howtouse_step)

