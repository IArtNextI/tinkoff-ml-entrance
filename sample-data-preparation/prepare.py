import os

fin = open("a.txt", "r")
lines = fin.readlines()
fin.close()
fout = open("b.txt", "w")
ok = True
for line in lines:
    if line == '\n':
        ok = True
    elif line[-2:] == ":\n":
        ok = False
        continue
    if not ok:
        line = line.replace('\n', ' ').replace(',', '').replace("\"", "").replace(":", '').replace(";", '').replace('!', '.').replace('?', '.').replace("'", '').replace('.', ' ').replace('-', ' ').replace('  ', ' ').lower()
        print(line, end='', file=fout)
fout.close()
fin = open("b.txt", "r")
content = fin.read()
content = content.replace('  ', ' ')
fin.close()
fout = open('c.txt', 'w')
print(content, file=fout)
os.remove('a.txt')
os.remove('b.txt')
os.rename('c.txt', 'data/c.txt')