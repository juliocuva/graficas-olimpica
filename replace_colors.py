import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace blue tailwind classes with yellow
# e.g., text-blue-500 -> text-yellow-500, bg-blue-600 -> bg-yellow-500 (since yellow-600 is a bit dark/muddy in tailwind, yellow-500 is better for accents)
content = re.sub(r'bg-blue-600', 'bg-yellow-500', content)
content = re.sub(r'bg-blue-500', 'bg-yellow-400', content)
content = re.sub(r'text-blue-500', 'text-yellow-500', content)
content = re.sub(r'text-blue-600', 'text-yellow-500', content)
content = re.sub(r'border-blue-500', 'border-yellow-500', content)
content = re.sub(r'border-blue-600', 'border-yellow-500', content)
content = re.sub(r'border-l-blue-500', 'border-l-yellow-500', content)
content = re.sub(r'from-blue-900', 'from-yellow-900', content)
content = re.sub(r'bg-blue-900', 'bg-yellow-900', content)
content = re.sub(r'hover:text-blue-400', 'hover:text-yellow-400', content)
content = re.sub(r'hover:text-blue-500', 'hover:text-yellow-500', content)
content = re.sub(r'hover:bg-blue-500', 'hover:bg-yellow-500', content)
content = re.sub(r'hover:bg-blue-600', 'hover:bg-yellow-500', content)
content = re.sub(r'hover:border-blue-500', 'hover:border-yellow-500', content)
content = re.sub(r'selection:bg-blue-600', 'selection:bg-yellow-500', content)
content = re.sub(r'rgba\(59,130,246', 'rgba(234,179,8', content) # shadow for yellow-500
content = re.sub(r'#3b82f6', '#eab308', content) # hex for yellow-500

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
