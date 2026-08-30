const fs = require('fs');
const file = 'artifacts/cinematic-scroll-site/src/components/HeroSection.tsx';
let content = fs.readFileSync(file, 'utf8');

content = content.replace(
  /const filteredResults = searchVal\.trim\(\)\s+\? availableDownloads\.filter\(\s+\(item\) =>\s+\(item\.title \|\| ""\)\.toLowerCase\(\)\.includes\(searchVal\.toLowerCase\(\)\) \|\|\s+\(item\.desc \|\| ""\)\.toLowerCase\(\)\.includes\(searchVal\.toLowerCase\(\)\)\s+\)\s+: availableDownloads;/g,
  `const filteredResults = searchVal.trim()
    ? availableDownloads.filter(
        (item) =>
          (item.title || "").toLowerCase().startsWith(searchVal.trim().toLowerCase())
      )
    : availableDownloads;`
);

content = content.replace(
  /className="absolute top-\[68px\] right-0 w-80 sm:w-96 md:w-\[420px\] rounded-2xl p-3\.5 z-\[999\] backdrop-blur-3xl transition-all duration-300 shadow-\[0_25px_60px_-15px_rgba\(0,0,0,0\.9\),0_0_30px_rgba\(0,229,209,0\.15\)\] overflow-hidden border border-white\/20"/g,
  `className="absolute top-[68px] right-0 w-80 sm:w-96 md:w-[420px] rounded-2xl p-3.5 z-[999] transition-all duration-300 overflow-hidden"`
);

content = content.replace(
  /style={{\s+background: "rgba\(255, 255, 255, 0\.12\)",\s+backdropFilter: "blur\(16px\)",\s+WebkitBackdropFilter: "blur\(16px\)",\s+}}/g,
  `style={{
                    background: "rgba(255, 255, 255, 0.12)",
                    backdropFilter: "blur(16px)",
                    WebkitBackdropFilter: "blur(16px)",
                    border: "1px solid rgba(255, 255, 255, 0.2)",
                    boxShadow: "0 8px 32px 0 rgba(0,0,0,0.15)",
                  }}`
);

fs.writeFileSync(file, content);
