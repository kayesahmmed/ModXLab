import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# 1. Update HeroMockPanel definition
old_def = "export function HeroMockPanel({ isDark }: { isDark: boolean }) {"
new_def = """export function HeroMockPanel({ 
  isDark, yPanel, scalePanel, opacityPanel, rotateXPanel 
}: { 
  isDark: boolean; yPanel?: any; scalePanel?: any; opacityPanel?: any; rotateXPanel?: any; 
}) {"""
content = content.replace(old_def, new_def)

# 2. Update Left Column
old_left = """<div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] h-full overflow-hidden backdrop-blur-md"
          style={{ background: "rgba(255, 255, 255, 0.12)", backdropFilter: "blur(12px)", WebkitBackdropFilter: "blur(12px)", border: "1px solid rgba(255, 255, 255, 0.2)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)" }}
        >"""
new_left = """<motion.div 
          className="w-full flex flex-col justify-between gap-4 relative z-10 p-5 rounded-[24px] h-full overflow-hidden"
          style={{ 
            background: "rgba(255, 255, 255, 0.12)", backdropFilter: "blur(12px)", WebkitBackdropFilter: "blur(12px)", border: "1px solid rgba(255, 255, 255, 0.2)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
            y: yPanel, scale: scalePanel, opacity: opacityPanel, rotateX: rotateXPanel, transformPerspective: 1200, z: 0,
            transformOrigin: "center center"
          }}
        >"""
content = content.replace(old_left, new_left)
# Change closing div to motion.div for Left column
old_left_close = """            )}
          </div>
        </div>
        {/* Right Column: Premium Content Showcase Grid */}"""
new_left_close = """            )}
          </div>
        </motion.div>
        {/* Right Column: Premium Content Showcase Grid */}"""
content = content.replace(old_left_close, new_left_close)

# 3. Update Right Column
old_right = """<div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] h-full overflow-hidden backdrop-blur-md"
          style={{ background: "rgba(255, 255, 255, 0.12)", backdropFilter: "blur(12px)", WebkitBackdropFilter: "blur(12px)", border: "1px solid rgba(255, 255, 255, 0.2)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)" }}
        >"""
new_right = """<motion.div 
          className="flex-1 flex flex-col justify-between gap-4 relative z-10 p-5 sm:p-6 rounded-[24px] h-full overflow-hidden"
          style={{ 
            background: "rgba(255, 255, 255, 0.12)", backdropFilter: "blur(12px)", WebkitBackdropFilter: "blur(12px)", border: "1px solid rgba(255, 255, 255, 0.2)", boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)",
            y: yPanel, scale: scalePanel, opacity: opacityPanel, rotateX: rotateXPanel, transformPerspective: 1200, z: 0,
            transformOrigin: "center center"
          }}
        >"""
content = content.replace(old_right, new_right)

# Closing tag for Right column is at the very end of HeroMockPanel
old_right_close = """          </div>
        </div>
      </div>
    </div>
  );
}"""
new_right_close = """          </div>
        </motion.div>
      </div>
    </div>
  );
}"""
content = content.replace(old_right_close, new_right_close)

# 4. Update the wrapper in HeroSection
old_wrapper = """        <motion.div
          initial={{ opacity: 0, scale: 0.96, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          style={{ y: yPanel, scale: scalePanel, opacity: opacityPanel, rotateX: rotateXPanel, transformPerspective: 1200, z: 0 }}
          transition={{ duration: 0.6, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
          className="w-full max-w-[960px] z-10 relative mt-16 sm:mt-24 lg:mt-28"
        >
          <HeroMockPanel isDark={isDark} />
        </motion.div>"""
new_wrapper = """        <motion.div
          initial={{ opacity: 0, scale: 0.96, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
          className="w-full max-w-[960px] z-10 relative mt-16 sm:mt-24 lg:mt-28"
        >
          <HeroMockPanel 
            isDark={isDark} 
            yPanel={yPanel} 
            scalePanel={scalePanel} 
            opacityPanel={opacityPanel} 
            rotateXPanel={rotateXPanel} 
          />
        </motion.div>"""
content = content.replace(old_wrapper, new_wrapper)

with open(file_path, "w") as f:
    f.write(content)
print("Updated HeroMockPanel")
