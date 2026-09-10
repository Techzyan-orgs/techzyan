import urllib.request
import os

images_dir = r"c:\Users\Samudra Ganguly\Antigravity\Website_005\techzyan\public\images"
os.makedirs(images_dir, exist_ok=True)

urls = {
    "subhashish_tutor.png": "https://demo-tutor-subhashish-banerjee.vercel.app/assets/subhashish_teaching-CEfvHFdE.png",
    "subhashish_portrait.png": "https://demo-tutor-subhashish-banerjee.vercel.app/assets/subhashish-Bko7uNyP.png",
    "baruipur_theme.jpeg": "https://baruipurbhattacharyaparapujo.info/gallery/theme.jpeg",
    "baruipur_pandal.jpeg": "https://baruipurbhattacharyaparapujo.info/gallery/img_3.jpeg"
}

headers = {"User-Agent": "Mozilla/5.0"}

for filename, url in urls.items():
    dest = os.path.join(images_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        size = os.path.getsize(dest)
        print(f"Downloaded {filename}: {size} bytes")
    except Exception as e:
        print(f"Failed {filename}: {e}")
