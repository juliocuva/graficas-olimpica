import urllib.request
import os

os.makedirs('img', exist_ok=True)

images = [
    ('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80', 'img/premium_hero.jpg'),
    ('https://images.unsplash.com/photo-1555529771-835f59fc5efe?auto=format&fit=crop&w=1200&q=80', 'img/premium_float.jpg'),
    ('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80', 'img/premium_banca.jpg'),
    ('https://images.unsplash.com/photo-1567474441249-165c71c1fce9?auto=format&fit=crop&w=1200&q=80', 'img/premium_retail.jpg')
]

for url, filename in images:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
