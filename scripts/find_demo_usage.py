import os

src_dir = 'src'
hits = []
for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith(('.ts', '.tsx')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                if 'demonstrationProjects' in content or 'demonstrations' in content:
                    hits.append(path)

print("Files using demonstrationProjects:")
for h in hits:
    print("- " + h)
