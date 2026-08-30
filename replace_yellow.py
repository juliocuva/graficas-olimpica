with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('#FFD600', '#FFFF00')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced all #FFD600 with #FFFF00")
