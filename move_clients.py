import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract the Trusted By section
pattern = re.compile(r'(\s*<!-- 1\.5\. Trusted By \(Clients Marquee/Grid\) -->\s*<section class="py-16 bg-white border-y border-gray-100">.*?</section>)', re.DOTALL)
match = pattern.search(content)

if match:
    trusted_by_section = match.group(1)
    
    # 2. Remove Grupo Exito from the section
    trusted_by_section = re.sub(r'\s*<!-- Client 4 -->\s*<h4 class="text-2xl font-light tracking-widest text-\[#111\]">GRUPO <span class="font-black">ÉXITO</span></h4>', '', trusted_by_section)
    
    # Also adjust the comment number for Client 5
    trusted_by_section = trusted_by_section.replace('<!-- Client 5 -->', '<!-- Client 4 -->')
    
    # 3. Remove the section from its original place
    content = content.replace(match.group(1), '')
    
    # 4. Insert it right before Infrastructure
    infra_marker = '    <!-- 4. Infrastructure List (Editorial Typographic) -->'
    content = content.replace(infra_marker, trusted_by_section.lstrip() + '\n\n' + infra_marker)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully moved and updated the Clients section.")
else:
    print("Could not find the Trusted By section.")
