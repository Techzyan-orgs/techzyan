import os

src_dir = 'src'
hits = []
for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith(('.ts', '.tsx', '.json', '.md')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                if 'Aura' in content or 'aura' in content:
                    hits.append(path)

print("Files mentioning Aura/aura:")
for h in hits:
    print("- " + h)
