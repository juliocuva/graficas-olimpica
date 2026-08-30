import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'\s*<!-- Footer Minimal -->.*?<div class="text-\[9px\] uppercase tracking-widest text-gray-400">\s*(?=<!-- 6\. Footer)', re.DOTALL)

new_content = pattern.sub('\n\n', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed old minimalist footer.")
