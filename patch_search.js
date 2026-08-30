const fs = require('fs');
const file = 'artifacts/cinematic-scroll-site/src/components/HeroSection.tsx';
let content = fs.readFileSync(file, 'utf8');

content = content.replace(
  /\(item\.title \|\| ""\)\.toLowerCase\(\)\.startsWith\(searchVal\.trim\(\)\.toLowerCase\(\)\)/g,
  '(item.title || "").toLowerCase().includes(searchVal.trim().toLowerCase()) || (item.desc || "").toLowerCase().includes(searchVal.trim().toLowerCase())'
);

fs.writeFileSync(file, content);
