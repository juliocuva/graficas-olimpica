from PIL import Image

# Open the logo
img = Image.open('img/logo-graficas.png').convert('RGB')
colors = img.getcolors(maxcolors=1000000)

yellows = []
for count, (r, g, b) in colors:
    # A yellow color should have high R and G, and low B
    if r > 200 and g > 150 and b < 100:
        yellows.append((count, (r, g, b)))

if yellows:
    # Sort by count to find the most prominent yellow
    yellows.sort(reverse=True, key=lambda x: x[0])
    most_prominent = yellows[0][1]
    hex_color = "#{:02x}{:02x}{:02x}".format(most_prominent[0], most_prominent[1], most_prominent[2]).upper()
    print(f"EXACT YELLOW: {hex_color}")
else:
    print("No prominent yellow found.")
