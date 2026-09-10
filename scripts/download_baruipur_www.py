import urllib.request
import os

images_dir = r"c:\Users\Samudra Ganguly\Antigravity\Website_005\techzyan\public\images"

urls = [
    ("baruipur_theme.jpeg", "https://www.baruipurbhattacharyaparapujo.info/gallery/theme.jpeg"),
    ("baruipur_pandal.jpeg", "https://www.baruipurbhattacharyaparapujo.info/gallery/img_3.jpeg"),
    ("baruipur_logo.png", "https://www.baruipurbhattacharyaparapujo.info/logo.png")
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for filename, url in urls:
    dest = os.path.join(images_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            with open(dest, "wb") as f:
                f.write(data)
        print(f"Downloaded {filename}: {len(data)} bytes")
    except Exception as e:
        print(f"Failed {filename}: {e}")
