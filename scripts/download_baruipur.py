import urllib.request
import os

images_dir = r"c:\Users\Samudra Ganguly\Antigravity\Website_005\techzyan\public\images"

urls = [
    ("baruipur_theme.jpeg", "https://baruipurbhattacharyaparapujo.in/gallery/theme.jpeg"),
    ("baruipur_theme_info.jpeg", "https://baruipurbhattacharyaparapujo.info/gallery/theme.jpeg"),
    ("baruipur_pandal.jpeg", "https://baruipurbhattacharyaparapujo.in/gallery/img_3.jpeg"),
    ("baruipur_logo.png", "https://baruipurbhattacharyaparapujo.in/logo.png")
]

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        print(f"Redirecting {code} to: {newurl}")
        return urllib.request.Request(newurl, headers={"User-Agent": "Mozilla/5.0"})

opener = urllib.request.build_opener(NoRedirect)

for filename, url in urls:
    dest = os.path.join(images_dir, filename)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with opener.open(req) as resp:
            data = resp.read()
            with open(dest, "wb") as f:
                f.write(data)
        print(f"Downloaded {filename}: {len(data)} bytes")
    except Exception as e:
        print(f"Failed {filename}: {e}")
