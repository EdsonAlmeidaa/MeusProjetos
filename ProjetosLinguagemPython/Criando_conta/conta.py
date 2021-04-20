class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero # Parametro
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self): # Método para receber como um argumento uma referencia do proprio objeto. (IMPRIME O SALDO DA CONTA)
        print('Saldo {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor): # Método para adicionar o valor ao saldo da conta.
        self.__saldo += valor

    def saca(self, valor): # Método para subtraí o valor do saldo da conta.
        self.__saldo -= valor
