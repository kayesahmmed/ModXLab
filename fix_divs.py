import re

file_path = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

# For Left Column:
old_left_close = """          </div>
        </div>
        {/* Right Column: Premium Content Showcase Grid */}"""
new_left_close = """          </div>
        </motion.div>
        {/* Right Column: Premium Content Showcase Grid */}"""
content = content.replace(old_left_close, new_left_close)

# For Right Column:
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

with open(file_path, "w") as f:
    f.write(content)
print("Fixed closing tags")
