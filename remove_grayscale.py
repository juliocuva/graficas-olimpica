import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(' grayscale ', ' ')
content = content.replace('hover:grayscale-0 ', '')
content = content.replace('group-hover:grayscale-0 ', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
