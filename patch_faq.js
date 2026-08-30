const fs = require('fs');
const file = 'artifacts/cinematic-scroll-site/src/components/FAQSection.tsx';
let content = fs.readFileSync(file, 'utf8');

// Replace standard accordion open animation
content = content.replace(
  'transition={{ duration: 0.3 }}',
  'transition={{ duration: 0.15, ease: "easeOut" }}'
);
content = content.replace(
  'transition={{ duration: 0.3 }}',
  'transition={{ duration: 0.15, ease: "easeOut" }}'
);

// We should globally make sure the chevron rotate is also fast
content = content.replace(
  'transition-all duration-300 relative group',
  'transition-all duration-150 relative group'
);
content = content.replace(
  'transition-colors duration-300',
  'transition-colors duration-150'
);
content = content.replace(
  'transition-all duration-300 shrink-0',
  'transition-all duration-150 shrink-0'
);

fs.writeFileSync(file, content);
