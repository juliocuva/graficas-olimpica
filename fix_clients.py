import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if corrupted
if 'Grǭficas' in content:
    print("It IS corrupted inside the file.")
    # Fix common corruptions
    content = content.replace('Grǭficas Olmpica', 'Gráficas Olímpica')
    content = content.replace('ingeniera', 'ingeniería')
    content = content.replace('Bogotǭ', 'Bogotá')
    content = content.replace('%XITO', 'ÉXITO')
    content = content.replace('Sealizacin', 'Señalización')
    # and others... but hopefully it's not corrupted!

# Remove Grupo Exito and Bancolombia
pattern = re.compile(r'\s*<!-- Client 4 -->\s*<h4[^>]*>GRUPO.*?</h4>', re.DOTALL)
content = pattern.sub('', content)

pattern2 = re.compile(r'\s*<!-- Client 5 -->\s*<h4[^>]*>Bancolombia.*?</h4>', re.DOTALL)
content = pattern2.sub('', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleaned up clients.")
