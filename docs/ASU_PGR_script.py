import os

# Папки с блоками
folders = ['blocks/functional', 'blocks/architecture', 'blocks/scenarios', 'blocks/glossary']

# Итоговый документ
with open('ASU_PGR_manual.md', 'w', encoding='utf-8') as outfile:
    for folder in folders:
        files = sorted(os.listdir(folder))
        for file in files:
            path = os.path.join(folder, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                outfile.write(content + '\n\n')
