import os

def Shakespeare():
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

def Harry():
    fin = open("harry.txt", 'r')
    content = fin.readlines()
    fin.close()
    content = content[1:]
    fout = open("harry-2.txt", 'w')
    for line in content:
        if "J.K. Rowling" in line:
            continue
        if line == '\n':
            continue
        print(line, file=fout)
    fout.close()
    fin = open("harry-2.txt", 'r')
    content = fin.read()
    fin.close()
    fout = open("harry-3.txt", 'w')
    content = content.replace('\n', ' ').replace(',', '').replace("\"", "").replace(":", '').replace(";", '').replace('!', '.').replace('?', '.').replace("'", '').replace('.', ' ').replace('-', ' ').replace('  ', ' ').replace('’', '').replace("—", "").replace("”", "").replace("“", "").lower()
    content = content.replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace('\\', '')
    print(content, file=fout)
    fout.close()
    os.remove("harry.txt")    
    os.remove("harry-2.txt")
    os.rename("harry-3.txt", "data/harry-3.txt")

if __name__ == "__main__":
    Shakespeare()
    Harry()