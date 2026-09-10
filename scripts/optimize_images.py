from PIL import Image
import os

images_dir = r"c:\Users\Samudra Ganguly\Antigravity\Website_005\techzyan\public\images"

# 1. Subhashish Banerjee Tutor
sub_in = os.path.join(images_dir, "subhashish_tutor.png")
sub_out = os.path.join(images_dir, "subhashish-tutor.jpg")
with Image.open(sub_in) as im:
    print("Subhashish original size:", im.size, im.mode)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    im.thumbnail((1200, 800), Image.Resampling.LANCZOS)
    im.save(sub_out, "JPEG", quality=90, optimize=True)
print("Saved subhashish-tutor.jpg:", os.path.getsize(sub_out), "bytes")

# 2. Baruipur Durga Puja Theme
bar_in = os.path.join(images_dir, "baruipur_theme.jpeg")
bar_out = os.path.join(images_dir, "baruipur-durga-puja.jpg")
with Image.open(bar_in) as im:
    print("Baruipur original size:", im.size, im.mode)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    im.thumbnail((1200, 800), Image.Resampling.LANCZOS)
    im.save(bar_out, "JPEG", quality=90, optimize=True)
print("Saved baruipur-durga-puja.jpg:", os.path.getsize(bar_out), "bytes")
