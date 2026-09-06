import re

hero_file = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
faq_file = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"

# Fix Hero Section
with open(hero_file, "r") as f:
    hero = f.read()

old_hero_search = """              <div
                className={`transition-all duration-350 ease-[cubic-bezier(0.16,1,0.3,1)] h-14 flex items-center rounded-2xl relative ${
                  searchOpen ? "w-[260px] sm:w-[320px] opacity-100 pointer-events-auto" : "w-0 opacity-0 pointer-events-none"
                }`}
              >"""
new_hero_search = """              <div
                className={`transition-all duration-350 ease-[cubic-bezier(0.16,1,0.3,1)] h-14 flex items-center rounded-2xl relative ${
                  searchOpen ? "w-[260px] sm:w-[320px] opacity-100 pointer-events-auto" : "w-0 opacity-0 pointer-events-none"
                }`}
                style={{ willChange: 'transform, opacity', WebkitBackfaceVisibility: 'hidden', backfaceVisibility: 'hidden' }}
              >"""
hero = hero.replace(old_hero_search, new_hero_search)

# Also apply it to the main container just in case
old_hero_search_container = """            <div ref={searchContainerRef} className={`flex items-center gap-2 h-14 relative ${searchOpen ? "z-[120]" : "z-50"}`}>"""
new_hero_search_container = """            <div ref={searchContainerRef} className={`flex items-center gap-2 h-14 relative ${searchOpen ? "z-[120]" : "z-50"}`} style={{ willChange: 'transform, opacity', WebkitBackfaceVisibility: 'hidden', backfaceVisibility: 'hidden' }}>"""
hero = hero.replace(old_hero_search_container, new_hero_search_container)

with open(hero_file, "w") as f:
    f.write(hero)


# Fix FAQ Section
with open(faq_file, "r") as f:
    faq = f.read()

old_faq_main = """                className="rounded-[24px] relative group"
              >"""
new_faq_main = """                className="rounded-[24px] relative group"
                style={{ willChange: 'transform, opacity', WebkitBackfaceVisibility: 'hidden', backfaceVisibility: 'hidden' }}
              >"""
faq = faq.replace(old_faq_main, new_faq_main)

old_faq_modal = """                        className="rounded-2xl relative transition-all duration-150"
                      >"""
new_faq_modal = """                        className="rounded-2xl relative transition-all duration-150"
                        style={{ willChange: 'transform, opacity', WebkitBackfaceVisibility: 'hidden', backfaceVisibility: 'hidden' }}
                      >"""
faq = faq.replace(old_faq_modal, new_faq_modal)

with open(faq_file, "w") as f:
    f.write(faq)

