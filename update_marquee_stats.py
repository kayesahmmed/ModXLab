import re

file_path = "./artifacts/cinematic-scroll-site/src/components/MarqueeSection.tsx"
with open(file_path, "r") as f:
    content = f.read()

old_stats = """const statsData = [
  { icon: <svg className="w-10 h-10" fill="none" viewBox="0 0 47.0588 40"><path clipRule="evenodd" d={svgPaths.pee67100} fill="#00E5D1" fillRule="evenodd" /></svg>, value: "10.5K+", label: "ACTIVE USERS" },
  { icon: <svg className="w-10 h-10" fill="none" viewBox="0 0 40 40"><path d={svgPaths.p25f88280} fill="#A65FED" /></svg>, value: "18.52K+", label: "TOTAL DOWNLOADS" },
  { icon: <svg className="w-10 h-10" fill="none" viewBox="0 0 41.8816 40"><path d={svgPaths.p1c15ee60} fill="#FFB11A" /></svg>, value: "4.9 ★", label: "RATING" },
  { icon: <svg className="w-10 h-10" fill="none" viewBox="0 0 32.4051 40"><path d={svgPaths.p1d073f0} fill="#16CF83" /></svg>, value: "99.9%", label: "UPTIME" },
];"""

new_stats = """const statsData = [
  { icon: <svg className="w-10 h-10" fill="none" viewBox="0 0 40 40"><path d={svgPaths.p25f88280} fill="#A65FED" /></svg>, value: "25K+", label: "TOTAL DOWNLOADS" },
  { icon: <svg className="w-10 h-10" fill="none" viewBox="0 0 47.0588 40"><path clipRule="evenodd" d={svgPaths.pee67100} fill="#00E5D1" fillRule="evenodd" /></svg>, value: "3.2K", label: "ACTIVE USERS" },
  { icon: <svg className="w-10 h-10" fill="none" viewBox="0 0 32.4051 40"><path d={svgPaths.p1d073f0} fill="#16CF83" /></svg>, value: "99.9%", label: "ANTI-BAN SAFE" },
];"""

content = content.replace(old_stats, new_stats)

# Also update the grid from grid-cols-2 to grid-cols-1 md:grid-cols-3
old_grid = 'className="grid grid-cols-2 gap-4 sm:gap-6"'
new_grid = 'className="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:gap-6 max-w-4xl mx-auto"'
content = content.replace(old_grid, new_grid)

with open(file_path, "w") as f:
    f.write(content)
print("Updated MarqueeSection stats")
