#Questao 4
class Pessoa:

    def __init__(self,cpf, nome) -> None:
        self.__cpf = cpf
        self.__nome = nome

    def imprimir_dados(self):
        print(self.__cpf,self.__nome)

if __name__ == "__main__":
    pes1 =  Pessoa(1234,"Maria")
    pes1.imprimir_dados()