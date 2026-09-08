svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="8" fill="#080C14"/>
  <circle cx="16" cy="16" r="6" fill="#38BDF8"/>
  <circle cx="22" cy="10" r="2.5" fill="#F59E0B"/>
</svg>"""

with open('public/favicon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

with open('public/icon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print('Icons written successfully')
