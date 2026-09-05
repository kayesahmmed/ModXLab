with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "r") as f:
    content = f.read()

bad = """                  </div>
                  </div>
                </motion.div>
              )}
              </AnimatePresence>
            </div>
          </motion.div>
        </motion.div>"""

good = """                  </div>
                  </div>
                </motion.div>
              )}
              </AnimatePresence>
              </div>
            </div>
          </motion.div>
        </motion.div>"""

content = content.replace(bad, good)
with open("./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx", "w") as f:
    f.write(content)
