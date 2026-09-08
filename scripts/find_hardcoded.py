import os
import re

src_dir = 'src'
patterns = {
    'email': r'[\w\.-]+@[\w\.-]+\.\w+',
    'phone': r'(\+?\d[\d\s-]{7,}\d)',
    'url': r'https?://[^\s"\'`<>]+',
    'hours': r'\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun|AM|PM|IST)\b',
    'location': r'\b(Kolkata|West Bengal|India)\b'
}

results = []

for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith(('.tsx', '.ts', '.jsx', '.js')) and f != 'site.ts':
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for idx, line in enumerate(lines):
                    # Check for emails
                    for match in re.finditer(patterns['email'], line):
                        results.append(f"{filepath}:{idx+1} [EMAIL] {match.group(0)} -> {line.strip()[:100]}")
                    # Check for phone-like patterns
                    for match in re.finditer(r'\+91[\d\s-]+', line):
                        results.append(f"{filepath}:{idx+1} [PHONE] {match.group(0)} -> {line.strip()[:100]}")
                    # Check for mailto: or tel:
                    if 'mailto:' in line or 'tel:' in line or 'wa.me' in line:
                        results.append(f"{filepath}:{idx+1} [CONTACT_LINK] -> {line.strip()[:100]}")
                    # Check for external URLs
                    for match in re.finditer(r'https?://(?:www\.)?(?:linkedin|twitter|github|facebook|instagram|wa\.me)[^\s"\'`<>]*', line):
                        results.append(f"{filepath}:{idx+1} [SOCIAL_URL] {match.group(0)} -> {line.strip()[:100]}")

print(f"Total potential hardcoded instances found: {len(results)}")
for r in results:
    print(r)
