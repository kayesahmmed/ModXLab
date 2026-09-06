import re

def replace_in_file(path, old, new):
    with open(path, "r") as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(path, "w") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Failed to find target in {path}")

faq_path = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"

# For the main FAQ
old_faq_main = """              <motion.div 
                key={faq.id} 
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, amount: 0.1 }}
                transition={{ duration: 0.5, delay: i * 0.1, ease: [0.16, 1, 0.3, 1] }}
                className="rounded-[24px] relative group overflow-hidden transition-all duration-300"
                style={{ 
                  background: "rgba(255, 255, 255, 0.05)",
                  backdropFilter: "blur(16px)",
                  WebkitBackdropFilter: "blur(16px)",
                  border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.15)",
                  boxShadow: isOpen ? "0 8px 32px 0 rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                }}
              >
                <div className="relative z-10 w-full h-full">"""

new_faq_main = """              <motion.div 
                key={faq.id} 
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, amount: 0.1 }}
                transition={{ duration: 0.5, delay: i * 0.1, ease: [0.16, 1, 0.3, 1] }}
                className="rounded-[24px] relative group overflow-hidden"
              >
                <div 
                  className="absolute inset-0 z-0 transition-all duration-300 pointer-events-none"
                  style={{
                    background: "rgba(255, 255, 255, 0.05)",
                    backdropFilter: "blur(16px)",
                    WebkitBackdropFilter: "blur(16px)",
                    border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.15)",
                    boxShadow: isOpen ? "0 8px 32px 0 rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                  }}
                />
                <div className="relative z-10 w-full h-full">"""
replace_in_file(faq_path, old_faq_main, new_faq_main)

# For the searched FAQ list
old_faq_search = """                      <div
                        key={faq.id}
                        className="rounded-[18px] relative transition-all duration-300 overflow-hidden"
                        style={{ 
                          background: "rgba(255, 255, 255, 0.05)",
                          backdropFilter: "blur(16px)",
                          WebkitBackdropFilter: "blur(16px)",
                          border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.15)",
                          boxShadow: isOpen ? "0 4px 20px -5px rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                        }}
                      >
                        <div className="relative z-10 w-full h-full">"""

new_faq_search = """                      <div
                        key={faq.id}
                        className="rounded-[18px] relative overflow-hidden"
                      >
                        <div 
                          className="absolute inset-0 z-0 transition-all duration-300 pointer-events-none"
                          style={{
                            background: "rgba(255, 255, 255, 0.05)",
                            backdropFilter: "blur(16px)",
                            WebkitBackdropFilter: "blur(16px)",
                            border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.15)",
                            boxShadow: isOpen ? "0 4px 20px -5px rgba(22, 207, 131, 0.25)" : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                          }}
                        />
                        <div className="relative z-10 w-full h-full">"""
replace_in_file(faq_path, old_faq_search, new_faq_search)

