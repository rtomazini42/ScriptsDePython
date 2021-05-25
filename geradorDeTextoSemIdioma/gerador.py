import random as rd

listaVogal = ["a","e","i","o","u"]
listaConsoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
listaConsoantesPermitidas = ['r','l','d','h', 'u']
def geradorPalavras():


    palavraGerada = ""

    tamanhoPalavra = rd.randint(1,6)
    for n in range(tamanhoPalavra):
        especial = rd.randint(0,15)
        if(especial == 9):
            escolha = rd.randint(0,len(listaVogal) -1)
            escolha2 = rd.randint(0,len(listaVogal) -1)
            palavraGerada += listaVogal[escolha2] + listaVogal[escolha]
        elif(especial == 1):
            escolha = rd.randint(0,len(listaConsoantes) -1)
            escolha2 = rd.randint(0,len(listaConsoantesPermitidas) -1)
            escolha3 = rd.randint(0,len(listaVogal) -1)
            palavraGerada += listaConsoantes[escolha] + listaConsoantesPermitidas[escolha2] +listaVogal[escolha3]
        elif(especial == 4):
            escolha = rd.randint(0,len(listaConsoantes) -1)
            escolha2 = rd.randint(0,len(listaVogal) -1)
            palavraGerada += listaConsoantes[escolha] + listaVogal[escolha2]
        elif(especial == 14 or especial == 12):
            escolha = rd.randint(0,len(listaVogal) -1)
            palavraGerada += listaVogal[escolha]
        else:
            escolha = rd.randint(0,len(listaVogal) -1)
            escolha2 = rd.randint(0, len(listaConsoantes) - 1)
            palavraGerada += listaConsoantes[escolha2] + listaVogal[escolha]

    return palavraGerada

def geradorTexto(n):
    texto = ""
    capita = True
    for i in range(n):
        palavra = geradorPalavras()
        if(capita):
            palavra = palavra.capitalize()
        capita = False
        texto = texto + palavra
        especial = rd.randint(0,20)
        if(especial > 18):
            texto += ","
        elif(especial == 1):
            capita = True
            texto += "."
            especial2 = rd.randint(0,4)
            if(especial2 == 2):
                texto += "\n"
        texto += " "
    silabasAssinatura = ["ar","or", "hum", "le", "o","re","na","to", "n","zi", "ni","tu", "ka","kle","lu","ana","ano","gi","vi", "tor","gue","gui","ga","hum","hu","va","ne","ssa","po","mo","do","ro","nal","sa","bri","ela"]
    tamPriNome = rd.randint(0,5)
    tamSegNome = rd.randint(0,8)
    PriNome = ""
    SegNome = ""
    for i in range(tamPriNome):
        sil = rd.randint(1,len(silabasAssinatura)-1)
        PriNome += silabasAssinatura[sil]
    for i in range(tamSegNome):
        sil = rd.randint(0,len(silabasAssinatura)-1)
        SegNome += silabasAssinatura[sil]
    assinatura = PriNome.capitalize() + " " + SegNome.capitalize()
    texto += "\n\n\n       "+ assinatura
    return texto


gerado = open('gerado.txt', 'w')
gerado.write(geradorTexto(500))
gerado.close()
