import urllib.request
import re

url = "https://unsplash.com/es/fotos/se-ve-un-mostrador-de-cajero-de-banco-moderno-8dtyrlYnGo0"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find the images.unsplash.com URL
    match = re.search(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9-]+', html)
    if match:
        img_url = match.group(0) + "?auto=format&fit=crop&w=1200&q=80"
        print(f"Found URL: {img_url}")
        img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(img_req) as response:
            with open('img/premium_banca.jpg', 'wb') as f:
                f.write(response.read())
        print("Successfully downloaded image.")
    else:
        print("Could not find image URL in HTML.")
except Exception as e:
    print(f"Failed: {e}")
