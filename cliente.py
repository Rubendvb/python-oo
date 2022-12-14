class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title() #Método title() retorna uma string em que o primeiro caractere de cada palavra é maiúsculo

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome
