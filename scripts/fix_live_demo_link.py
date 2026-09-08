import os

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target pattern for Live Demo button inside card
    old_target = """                    <button
                      onClick={() => setSelectedDemonstration(project)}
                      className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-sky-500/10 hover:bg-sky-500/20 text-brand-cyan text-xs font-bold transition-colors border border-sky-500/30"
                    >
                      <span>Live Demo</span>
                      <ExternalLink className="w-3.5 h-3.5" />
                    </button>"""

    new_replacement = """                    <a
                      href={project.demoUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-sky-500/10 hover:bg-sky-500/20 text-brand-cyan text-xs font-bold transition-colors border border-sky-500/30"
                    >
                      <span>Live Demo</span>
                      <ExternalLink className="w-3.5 h-3.5" />
                    </a>"""

    if old_target in content:
        content = content.replace(old_target, new_replacement)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated Live Demo link in: {path}")
    else:
        print(f"Pattern not found in: {path}")

update_file('src/app/page.tsx')
update_file('src/app/work/page.tsx')
