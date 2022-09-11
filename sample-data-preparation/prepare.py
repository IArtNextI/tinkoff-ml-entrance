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
    content = content.replace('\n', ' ').replace(',', '').replace("\"", "").replace(":", '').replace(";", '').replace('(', ' ').replace(')', ' ').replace('!', '.').replace('?', '.').replace("'", '').replace('.', ' ').replace('-', ' ').replace('  ', ' ').replace('’', '').replace("—", "").replace("”", "").replace("“", "").lower()
    content = content.replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace('\\', '').replace('/', '')
    print(content, file=fout)
    fout.close()
    os.remove("harry.txt")    
    os.remove("harry-2.txt")
    os.rename("harry-3.txt", "data/harry-3.txt")
    
def Harry2():
    fin = open("2harry.txt", 'r')
    content = fin.readlines()
    fin.close()
    content = content[7:]
    fout = open("2harry-2.txt", 'w')
    for line in content:
        if "J.K. Rowling" in line:
            continue
        if line == '\n':
            continue
        print(line, file=fout)
    fout.close()
    fin = open("2harry-2.txt", 'r')
    content = fin.read()
    fin.close()
    fout = open("2harry-3.txt", 'w')
    content = content.replace('\n', ' ').replace(',', '').replace("\"", "").replace(":", '').replace(";", '').replace('(', ' ').replace(')', ' ').replace('!', '.').replace('?', '.').replace("'", '').replace('.', ' ').replace('-', ' ').replace('  ', ' ').replace('’', '').replace("—", "").replace("”", "").replace("“", "").lower()
    content = content.replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace('\\', '').replace('/', '')
    print(content, file=fout)
    fout.close()
    os.remove("2harry.txt")    
    os.remove("2harry-2.txt")
    os.rename("2harry-3.txt", "data/2harry-3.txt")

def Harry3():
    fin = open("3harry.txt", 'r')
    content = fin.readlines()
    fin.close()
    content = content[12:]
    fout = open("3harry-2.txt", 'w')
    for line in content:
        if "J.K. Rowling" in line:
            continue
        if line == '\n':
            continue
        print(line, file=fout)
    fout.close()
    fin = open("3harry-2.txt", 'r')
    content = fin.read()
    fin.close()
    fout = open("3harry-3.txt", 'w')
    content = content.replace('\n', ' ').replace(',', '').replace("\"", "").replace(":", '').replace(";", '').replace('(', ' ').replace(')', ' ').replace('!', '.').replace('?', '.').replace("'", '').replace('.', ' ').replace('-', ' ').replace('  ', ' ').replace('’', '').replace("—", "").replace("”", "").replace("“", "").lower()
    content = content.replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace('\\', '').replace('/', '')
    print(content, file=fout)
    fout.close()
    os.remove("3harry.txt")    
    os.remove("3harry-2.txt")
    os.rename("3harry-3.txt", "data/3harry-3.txt")

if __name__ == "__main__":
    Shakespeare()
    Harry()
    Harry2()
    Harry3()
