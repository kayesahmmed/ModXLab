import re

hero_file = "./artifacts/cinematic-scroll-site/src/components/HeroSection.tsx"
faq_file = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"
reviews_file = "./artifacts/cinematic-scroll-site/src/components/ReviewsSection.tsx"

# --- HERO SECTION ---
with open(hero_file, "r") as f:
    hero = f.read()

hero = hero.replace(
    '<div className="flex flex-col divide-y divide-white/10 max-h-72 overflow-y-auto scrollbar-thin">',
    '<div className="flex flex-col divide-y divide-white/10 max-h-72 overflow-y-auto scrollbar-thin overscroll-contain" data-lenis-prevent="true">'
)

old_hero_blur = """                <div className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 border ${searchOpen ? "border-white/20" : "border-transparent"}`} style={{
                  background: "rgba(255, 255, 255, 0.18)",
                  backdropFilter: "blur(16px)",
                  WebkitBackdropFilter: "blur(16px)",
                  boxShadow: "0 8px 32px 0 rgba(0,0,0,0.15)"
                }} />"""
new_hero_blur = """                <div className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-350 bg-white/20 backdrop-blur-xl shadow-2xl ${searchOpen ? "border border-white/20" : "border border-transparent"}`} />"""
hero = hero.replace(old_hero_blur, new_hero_blur)

with open(hero_file, "w") as f:
    f.write(hero)


# --- FAQ SECTION ---
with open(faq_file, "r") as f:
    faq = f.read()

faq = faq.replace(
    '<div className="overflow-y-auto flex flex-col gap-3 pr-1 max-h-[55vh]">',
    '<div className="overflow-y-auto flex flex-col gap-3 pr-1 max-h-[55vh] overscroll-contain" data-lenis-prevent="true">'
)

# FAQ New Question Form
old_faq_form_blur = """                <div className="absolute inset-0 rounded-[24px] pointer-events-none z-0" style={{ 
                  background: "rgba(255, 255, 255, 0.12)", 
                  backdropFilter: "blur(12px)", 
                  WebkitBackdropFilter: "blur(12px)",
                  border: `1px solid rgba(255, 255, 255, 0.2)`,
                  boxShadow: "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                }} />"""
new_faq_form_blur = """                <div className="absolute inset-0 rounded-[24px] pointer-events-none z-0 bg-white/10 backdrop-blur-md border border-white/20 shadow-xl" />"""
faq = faq.replace(old_faq_form_blur, new_faq_form_blur)

# FAQ Main Items
old_faq_item_blur = """                <div className="absolute inset-0 rounded-[24px] pointer-events-none z-0 transition-all duration-150" style={{ 
                  background: "rgba(255, 255, 255, 0.12)", 
                  backdropFilter: "blur(12px)",
                  WebkitBackdropFilter: "blur(12px)",
                  border: isOpen ? `1px solid rgba(22, 207, 131, 0.4)` : `1px solid rgba(255, 255, 255, 0.2)`,
                  boxShadow: isOpen ? `0 8px 32px 0 rgba(22, 207, 131, 0.25)` : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                }} />"""
new_faq_item_blur = """                <div className={`absolute inset-0 rounded-[24px] pointer-events-none z-0 transition-all duration-150 bg-white/10 backdrop-blur-md ${isOpen ? 'border border-[#16CF83]/40 shadow-[0_8px_32px_0_rgba(22,207,131,0.25)]' : 'border border-white/20 shadow-xl'}`} />"""
faq = faq.replace(old_faq_item_blur, new_faq_item_blur)

# FAQ Modal Overlay
old_faq_modal_blur = """              <div className="absolute inset-0 rounded-3xl pointer-events-none z-0" style={{
                background: "rgba(30, 30, 40, 0.6)",
                backdropFilter: "blur(24px)",
                WebkitBackdropFilter: "blur(24px)",
                border: "1px solid rgba(255, 255, 255, 0.15)",
                boxShadow: "0 20px 50px -10px rgba(0, 0, 0, 0.85)"
              }} />"""
new_faq_modal_blur = """              <div className="absolute inset-0 rounded-3xl pointer-events-none z-0 bg-[#1E1E28]/60 backdrop-blur-2xl border border-white/15 shadow-[0_20px_50px_-10px_rgba(0,0,0,0.85)]" />"""
faq = faq.replace(old_faq_modal_blur, new_faq_modal_blur)

# FAQ Modal Items
old_faq_modal_item_blur = """                        <div className="absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-150" style={{
                          background: "rgba(255, 255, 255, 0.05)",
                          backdropFilter: "blur(12px)",
                          WebkitBackdropFilter: "blur(12px)",
                          border: isOpen ? "1px solid rgba(22, 207, 131, 0.4)" : "1px solid rgba(255, 255, 255, 0.1)",
                          boxShadow: isOpen ? "0 4px 20px -5px rgba(22, 207, 131, 0.25)" : "none"
                        }} />"""
new_faq_modal_item_blur = """                        <div className={`absolute inset-0 rounded-2xl pointer-events-none z-0 transition-all duration-150 bg-white/5 backdrop-blur-md ${isOpen ? 'border border-[#16CF83]/40 shadow-[0_4px_20px_-5px_rgba(22,207,131,0.25)]' : 'border border-white/10'}`} />"""
faq = faq.replace(old_faq_modal_item_blur, new_faq_modal_item_blur)

with open(faq_file, "w") as f:
    f.write(faq)


# --- REVIEWS SECTION ---
with open(reviews_file, "r") as f:
    reviews = f.read()

reviews = reviews.replace(
    'max-h-[70vh] overflow-y-auto pr-2 scrollbar-thin">',
    'max-h-[70vh] overflow-y-auto pr-2 scrollbar-thin overscroll-contain" data-lenis-prevent="true">'
)

reviews = reviews.replace(
    'className={`fixed inset-0 z-[999] overflow-y-auto',
    'data-lenis-prevent="true" className={`fixed inset-0 z-[999] overflow-y-auto'
)

with open(reviews_file, "w") as f:
    f.write(reviews)

