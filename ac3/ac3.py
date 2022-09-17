#Questão 1
class Individuo:
    def __init__(self,nome,altura,idade):
        self.__nome = nome
        self.altura = altura
        nova_idade = self.idade

indiv =  Individuo("Carolina",1.59,37)

#Questão 2

class Empresa:
    def __init__(self,nome, cnpj):
        self.__nome = nome
        self.__cnpj = None
        self.set_cnpj(cnpj)

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome

    def get_cnpj(self):
        return self.__cnpj

    def set_cnpj(self,cnpj):
        if len(str(cnpj))==14:
            __cnpj = cnpj

#emp = Empresa("Teste","11111111111111")
#print(emp.get_cnpj())


#Questao 3
def questao_3():

    try:
        idade = int(input("informe a idade: "))
        if not(idade >= 26 and idade <=75):
            raise ValueError
    except ValueError:
        print("Valor invalido: Informe uma idade entre 26 e 75 anos")
    except TypeError:
        print("Type Error tratado")
    except:
        print("Erro tratado")

#questao_3()


#Questao 4
class Pessoa:

    def __init__(self,cpf, nome) -> None:
        self.__cpf = cpf
        self.__nome = nome

    def imprimir_dados(self):
        print(self.__cpf,self.__nome)

#if __name__ == "__main__":
#    pes1 =  Pessoa(1234,"Maria")
#    pes1.imprimir_dados()


#Questao 5
class Paciente:
    def __init__(self,nome, altura) -> None:
        self.__nome = nome
        self.altura = altura

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self,valor):
        if valor < 1:
            valor = 1.0
        self.__altura = valor
    
#p = Paciente("Bia",0.4)
#print(p.altura)

#Questao 6

class Televisao:
    
    def __init__(self,modelo,preco) -> None:
        self.set_modelo(modelo)
        self.set_preco(preco)
    
    def get_modelo(self):
        return self.__modelo
    
    def get_preco(self):
        return self.__preco
    
    def set_modelo(self,valor):
        self.__modelo = valor
    
    def set_preco(self,valor):
        if valor < 1000:
            raise ValueError
        else:
            self.__preco = valor

def questao_6():

    try:
        tv = Televisao("TV123ABC",1000)
        print(tv.get_modelo())
        print(tv.get_preco())
       
    except ValueError:
        print("Não é possivel instanciar a TV")
    except:
        print("Erro Generico")

#questao_6()


#Questao 7 

class Produto:
    
    def __init__(self,descricao, preco) -> None:
        self.__descricao = descricao
        self.__preco = preco

    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def preco(self):
        return self.__preco
    
    @descricao.setter
    def descricao(self,valor):
        self.__descricao = valor
    
    @preco.setter
    def preco(self,valor):
        self.__preco = valor

class ProdutoFisico(Produto):

    def __init__(self, descricao, preco,peso) -> None:
        super().__init__(descricao, preco)
        self.__peso = peso
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,valor):
        self.__peso = valor

#prod = ProdutoFisico("Teste Descricao",123,321)
#print(prod.descricao)
#print(prod.peso)

#prod = Produto("Teste Descricao",123)
#print(prod.peso)

#Questao 8

class Maquina:
    def __init__(self,peso) -> None:
        self.peso = peso

class Veiculo(Maquina):
    def __init__(self, peso, placa) -> None:
        super().__init__(peso)
        self.placa = placa

    def get_placa(self):
        return self.placa
    
    def set_placa(self,placa):
        self.placa = placa

class Carro(Veiculo):
    def __init__(self, peso, placa,qtd_portas) -> None:
        super().__init__(peso, placa)
        self.qtd_portas = qtd_portas

class Onibus(Veiculo):
    def __init__(self, peso, placa,qtd_assentos) -> None:
        super().__init__(peso, placa)
        self.qtd_assentos = qtd_assentos

#maquina = Maquina(12)
#maquina.placa

#onibus= Onibus(5000,"WE02IF",64)
#print(onibus.get_placa())
#print(onibus.set_placa("T234P03"))
#print(onibus.get_placa())

#carro= Carro(2000,"WE02IF",64)
#print(carro.get_placa())
#print(carro.set_placa("T234P03"))
#print(carro.get_placa())
#print(carro.placa)
#print(carro.peso)

class Relogio:

    def __init__(self,hora,minuto):
        self.hora = hora
        self.minuto = minuto
    
    @property
    def hora(self):
        return self.__hora
    
    @property
    def minuto(self):
        return self.__minuto
    
    @hora.setter
    def hora(self,nova_hora):
        if nova_hora >= 0 and nova_hora <=23:
            self.__hora = nova_hora
        else:
            raise ValueError
    
    @minuto.setter
    def minuto(self, novo_minuto):
        if novo_minuto >= 0 and novo_minuto <= 59:
            self.__minuto = novo_minuto
        else:
            raise ValueError
    
    def tictac(self):
        self.__minuto +=1
        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora +=1
            if self.__hora>=23:
                self.__hora=00

#r = Relogio(22,59)

#print(r.hora)
#print(r.minuto)
#print(r.tictac())
#print(r.hora)
#print(r.minuto)