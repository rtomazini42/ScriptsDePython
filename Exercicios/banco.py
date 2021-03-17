class Conta():
    def __init__(self, nome,saldo,conta):
        self.__nome= nome
        self.__saldo= saldo
        self.__conta= conta

    def saque(self,saque):
        print("retirando {}".format(saque))
        if self.__saldo > saque:
            self.__saldo = self.__saldo - saque
            print("\n retirados {}\n".format(saque))
        else:
            print("\n saldo insuficiene \n")

    def deposito(self,deposito):
        print("depositando {}".format(deposito))
        self.__saldo = self.__saldo + deposito

    def extrato(self):
        print("{} tem {:.2f}".format(self.__nome,self.__saldo))

    def renderJuros(self):
        Juros = self.__saldo * 0.0002
        self.__saldo = self.__saldo + Juros
        print("Rendimento com juros: {:.2f}".format(self.__saldo))
        print("Foi rendido: {:.2f}".format(Juros))



api = Conta("Heroldo", 55.00, 123321)
api.extrato()
api.saque(33.0)
api.extrato()
api.deposito(300.12)
api.extrato()
api.saque(129.44)
api.extrato()
api.saque(3100.00)
api.deposito(3500.12)
api.saque(3650.00)
api.extrato()

for i in range(64):
    api.deposito(8)
    api.renderJuros()
