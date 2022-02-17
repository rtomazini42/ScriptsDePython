arq = open("texto.txt", 'r',encoding="utf-8")
arq2 = open("texto2.txt", 'w',encoding="utf-8")
for line in arq:
    line = line.strip()
    line = line + " "
    arq2.write(line)
arq.close()
arq2.close()
