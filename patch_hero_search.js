const fs = require('fs');
const file = 'artifacts/cinematic-scroll-site/src/components/HeroSection.tsx';
let content = fs.readFileSync(file, 'utf8');

content = content.replace(
  '{searchOpen && showSuggestions && (',
  '{searchOpen && showSuggestions && searchVal.trim().length > 0 && ('
);

content = content.replace(
  'background: "rgba(10, 8, 22, 0.75)",',
  'background: "rgba(255, 255, 255, 0.12)",'
);

content = content.replace(
  'backdropFilter: "blur(32px)",',
  'backdropFilter: "blur(16px)",'
);
content = content.replace(
  'WebkitBackdropFilter: "blur(32px)",',
  'WebkitBackdropFilter: "blur(16px)",'
);

content = content.replace(
  /\{searchVal && \(\s+<button[\s\S]*?<\/button>\s+\)\}/,
  `{searchVal && (
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setSearchVal("");
                        setShowSuggestions(false);
                      }}
                      className="absolute right-3.5 w-7 h-7 flex items-center justify-center rounded-full opacity-60 hover:opacity-100 transition-all cursor-pointer text-white hover:bg-white/10"
                      aria-label="Clear search"
                    >
                      <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2.5">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                      </svg>
                    </button>
                  )}`
);

fs.writeFileSync(file, content);
