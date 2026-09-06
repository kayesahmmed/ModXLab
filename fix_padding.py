import re

def update_file(file_path, old_text, new_text):
    with open(file_path, "r") as f:
        content = f.read()
    content = content.replace(old_text, new_text)
    with open(file_path, "w") as f:
        f.write(content)

# ReviewsSection.tsx
# In reviews, it has mb-10 on the container, and mb-6 on the buttons.
# Let's make it consistent across all by putting mb-10 or a standard gap.
# We don't need to touch Reviews.

# FAQSection.tsx
faq_path = "./artifacts/cinematic-scroll-site/src/components/FAQSection.tsx"
update_file(faq_path, 
    '        <div className="flex flex-col items-center gap-4 mb-14">', 
    '        <div className="flex flex-col items-center gap-4 mb-10">')

# FeaturesSection.tsx
features_path = "./artifacts/cinematic-scroll-site/src/components/FeaturesSection.tsx"
update_file(features_path,
    '      <div className="text-center mb-10 relative z-10">',
    '      <div className="text-center mb-10 relative z-10">') # It already has mb-10

# DownloadSection.tsx
download_path = "./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx"
update_file(download_path,
    '        <div className="text-center mb-6 px-4 sm:px-8 lg:px-14 relative z-10 w-full max-w-7xl mx-auto">',
    '        <div className="text-center mb-10 px-4 sm:px-8 lg:px-14 relative z-10 w-full max-w-7xl mx-auto">')

