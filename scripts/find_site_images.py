import re

def find_imgs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    # Look for image extensions
    matches = re.findall(r'https?://[^\s"\'`]+\.(?:png|jpg|jpeg|webp|svg)|/[^\s"\'`]+\.(?:png|jpg|jpeg|webp|svg)', text, re.I)
    return set(matches)

print("--- SUBHASHISH BANERJEE ---")
for img in sorted(find_imgs(r"C:\Users\Samudra Ganguly\.gemini\antigravity\brain\406949a6-6c75-4203-b9b8-0b4973427140\.system_generated\steps\2329\content.md")):
    print(img)

print("\n--- BARUIPUR PUJA ---")
for img in sorted(find_imgs(r"C:\Users\Samudra Ganguly\.gemini\antigravity\brain\406949a6-6c75-4203-b9b8-0b4973427140\.system_generated\steps\2178\content.md")):
    print(img)
