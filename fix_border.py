import re

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "r") as f:
    content = f.read()

# Issue: The absolute inset-0 child overlaps the border because it has the same border-radius, but the border is applied to the parent.
# Wait, if the parent has border AND the absolute child stretches to inset-0 (the padding box), the child actually sits *over* or exactly behind the parent depending on z-index, but often it obscures the border if there is any sub-pixel rendering.
# To fix: apply the border to the absolute blur layer! Or better yet, put the border on a ring div.
# Or, let's just restore the structure to exactly what it was, but JUST add the GPU acceleration to the style object without removing `overflow-hidden` or making a separate absolute div for FAQ items. Wait, separating the div WAS what fixed the glitch, because we decoupled the transform/willChange properties.
# But if the absolute div is the one that has the blur, we should give the border to it or the parent.
# Let's fix the absolute div by adding `border` to the parent's `style` object and removing the `inset-0` overlap by setting `inset: -1px` or something, OR we can put the border inside the absolute div.

# Actually, the user's issue might just be the `overflow-hidden` on the parent being removed, or the border radius not applying cleanly.
# If I look at the new code:
"""
              <motion.div 
                key={faq.id} 
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, amount: 0.1 }}
                transition={{ duration: 0.5, delay: i * 0.1, ease: [0.16, 1, 0.3, 1] }}
                className="rounded-[24px] transition-all duration-150 relative group"
                style={{ 
                  border: isOpen ? `1px solid rgba(22, 207, 131, 0.4)` : `1px solid rgba(255, 255, 255, 0.2)`,
                  boxShadow: isOpen ? `0 8px 32px 0 rgba(22, 207, 131, 0.25)` : "0 8px 32px 0 rgba(0, 0, 0, 0.15)"
                }}
              >
                <div className="absolute inset-0 rounded-[24px] pointer-events-none z-0" style={{
                  background: "rgba(255, 255, 255, 0.12)", 
                  backdropFilter: "blur(12px)",
                  WebkitBackdropFilter: "blur(12px)",
                  WebkitTransform: "translate3d(0, 0, 0)",
                  transform: "translate3d(0, 0, 0)",
                  WebkitBackfaceVisibility: "hidden",
                  backfaceVisibility: "hidden",
                }} />
                <div className="relative z-10 w-full overflow-hidden rounded-[24px]">
"""
# The problem here is that the absolute div is inside the border, so the blur effect bleeds or the border looks weird (smudged). 
# If we add `overflow-hidden` to the parent `<motion.div>`, it clips the absolute div perfectly so the border looks sharp.

content = content.replace('className="rounded-[24px] transition-all duration-150 relative group"', 'className="rounded-[24px] overflow-hidden transition-all duration-150 relative group"')
content = content.replace('className="rounded-2xl transition-all duration-150 relative border"', 'className="rounded-2xl overflow-hidden transition-all duration-150 relative border"')

with open("./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx", "w") as f:
    f.write(content)

