class Ponto():
    def __init__(self,nome,x,y):
        self.nome = nome
        self.x = x
        self.y = y
        distancias = []

    def distancia(self, Ponto):
        x = self.x - Ponto.x
        y = self.y - Ponto.y
        d = (x**2+y**2)**0.5
        return(d)

class Caminho():
    def __init__(self, pontoA, pontoB):
        self.pontoA = pontoA
        self.pontoB = pontoB
        self.distancia = pontoA.distancia(pontoB)

a = Ponto('a',0,1)
b = Ponto('b',3,2)
c = Ponto('c',4,5)
d = Ponto('d',10,5)
e = Ponto('e',7,5)
f = Ponto('f',2,1)
g = Ponto('g',3,3)

pontos = [a,b,c,d,e,f,g]
caminhos = []
for ponto in pontos:
    for p in pontos:
        cam =Caminho(ponto, p)
        if cam.pontoA != cam.pontoB:
            caminhos.append(cam)

caminhos_ordenados = sorted(caminhos,key = lambda caminho: caminho.distancia)

pontos_conectados = []
kruskal = []
for cam in caminhos_ordenados:
    if cam.pontoA not in pontos_conectados:
        if cam.pontoB not in pontos_conectados:
            kruskal.append(cam)
            pontos_conectados.append(cam.pontoA)

#for pontos in pontos_conectados:
 #   print(pontos.nome)
for element in kruskal:
    print("O ponto {} está conectado ao {} pela distancia {}".format(element.pontoA.nome,element.pontoB.nome,element.distancia))
