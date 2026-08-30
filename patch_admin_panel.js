const fs = require('fs');
const file = 'artifacts/cinematic-scroll-site/src/components/AdminPanel.tsx';
let content = fs.readFileSync(file, 'utf8');

// Add handlePreviewImagesSelectDlFile
const handlerCode = `
  const handlePreviewImagesSelectDlFile = async (e: React.ChangeEvent<HTMLInputElement>, idx: number) => {
    const files = e.target.files;
    if (!files || files.length === 0) return;
    try {
      setIsProcessing(true);
      const newImages = [];
      for (let i = 0; i < files.length; i++) {
        const base64 = await resizeImage(files[i], 1280, 1280, 0.85);
        newImages.push(base64);
      }
      const existingImages = dlFiles[idx].previewImages || [];
      updateDlFile(idx, 'previewImages', [...existingImages, ...newImages]);
      showToast("Preview images added successfully!");
    } catch (err) {
      console.error(err);
      showToast("Failed to process images", "error");
    } finally {
      setIsProcessing(false);
    }
  };

  const handleRemovePreviewImageDlFile = (fileIdx: number, imgIdx: number) => {
    const file = dlFiles[fileIdx];
    const newImages = [...(file.previewImages || [])];
    newImages.splice(imgIdx, 1);
    updateDlFile(fileIdx, 'previewImages', newImages);
  };
`;
content = content.replace('const handleOpenBlankDownloadForm = () => {', handlerCode + '\n  const handleOpenBlankDownloadForm = () => {');

// Add UI input
const uiCode = `
                            <div className="flex flex-col gap-1.5 col-span-1 sm:col-span-2 mt-2 border-t pt-3" style={{ borderColor: t.cardBorder }}>
                              <label className="text-xs font-semibold uppercase tracking-wider" style={{ color: t.subtext }}>App Previews / Screenshots</label>
                              <input type="file" accept="image/*" multiple onChange={(e) => handlePreviewImagesSelectDlFile(e, idx)} className="w-full px-4 py-2.5 rounded-xl text-sm outline-none file:mr-4 file:py-1 file:px-3 file:rounded-full file:border-0 file:text-xs file:bg-[#2790FF]/20 file:text-[#2790FF] cursor-pointer" style={{ background: t.inputBg, border: \`1px solid \${t.cardBorder}\`, color: t.text }} />
                              {(file.previewImages || []).length > 0 && (
                                <div className="flex gap-3 mt-2 overflow-x-auto pb-2 scrollbar-none">
                                  {file.previewImages.map((img: string, i: number) => (
                                    <div key={i} className="relative w-24 h-40 shrink-0 border rounded-xl" style={{ borderColor: t.cardBorder }}>
                                      <img src={img} alt="Preview" className="w-full h-full object-cover rounded-xl" />
                                      <button type="button" onClick={() => handleRemovePreviewImageDlFile(idx, i)} className="absolute -top-2 -right-2 w-6 h-6 bg-red-500 hover:bg-red-600 transition-colors text-white rounded-full flex items-center justify-center text-xs shadow-md z-10 cursor-pointer">✕</button>
                                    </div>
                                  ))}
                                </div>
                              )}
                            </div>
                          </div>
`;
content = content.replace('</div>\n                        </div>\n                      ))}', uiCode + '\n                        </div>\n                      ))}');

// Empty form state initialization
content = content.replace('setDlFiles([{ title: "", category: "", tags: "", imageUrl: "", buttonText: "Download Free APK", downloadLink: "" }]);', 'setDlFiles([{ title: "", category: "", tags: "", imageUrl: "", buttonText: "Download Free APK", downloadLink: "", previewImages: [] }]);');

fs.writeFileSync(file, content);
