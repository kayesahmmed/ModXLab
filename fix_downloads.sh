sed -i 's/<div className="relative w-full grid" style={{ gridTemplateAreas: "'\''stack'\''" }}>/<div className="relative w-full">/g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
sed -i 's/<AnimatePresence>//g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
sed -i 's/key={`page-${currentPage}`}//g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
sed -i 's/initial={{ opacity: 0, scale: 0.98, filter: "blur(4px)" }}//g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
sed -i 's/animate={{ opacity: 1, scale: 1, filter: "blur(0px)", zIndex: 10, transition: { duration: 0.35, ease: \[0.16, 1, 0.3, 1\] } }}//g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
sed -i 's/exit={{ opacity: 0, scale: 0.98, filter: "blur(4px)", zIndex: 0, transition: { duration: 0.25, ease: \[0.16, 1, 0.3, 1\] } }}//g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
sed -i 's/style={{ gridArea: "stack" }}//g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
sed -i 's/key={dl.id}/key={`${currentPage}-${dl.id}`}/g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
sed -i 's/initial={{ opacity: 0, y: 30 }}/initial={{ opacity: 0.3, y: 15 }}/g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
sed -i 's/transition={{ duration: 0.5, delay: idx \* 0.08, ease: \[0.16, 1, 0.3, 1\] }}/transition={{ duration: 0.25, delay: idx \* 0.04, ease: "easeOut" }}/g' ./artifacts/cinematic-scroll-site/src/components/DownloadSection.tsx
