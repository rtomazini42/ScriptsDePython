class Jogador:
    def __init__(self,nome,elo):
        self._nome = nome
        self._elo = elo


Jorge = Jogador("Jorge",100)
Ricardo = Jogador("Ricardo",130)
Ana = Jogador("Ana",500)
Lucia = Jogador("Lucia", 344)
Carlos = Jogador("Carlos",223)
Paula = Jogador("Paula", 234)

def eloRating(Ra,Rb):
    chances = 1/(1+10**((Rb._elo-Ra._elo)/400))
    print("A chance de " + Ra._nome + " derrotar " + Rb._nome +  " é : {:.2f}%".format(chances))
    return chances

Jogadores = [Jorge,Ricardo,Ana,Lucia,Carlos,Paula]
for jogador in Jogadores:
    print(jogador._nome)
    for oponente in Jogadores:
        if jogador == oponente:
            pass
        else:
            p = eloRating(jogador,oponente)
