with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()
    
# Replace:
#                 </motion.div>
#               )}
#               
#               
#             </div>
target = """                </motion.div>
              )}
              
              
            </div>"""
replacement = """                </motion.div>
              )}
              </AnimatePresence>
            </div>"""
content = content.replace(target, replacement)

with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)
