class Pessoa:
    def __init__(self,*filhos, nome=None, idade=27): # atributos
        self.nome = nome
        self.idade = idade
        self.lfi=list(filhos)



    def cumprimentar(self):
        return f'Olá Mundo {self.nome}' # se verificar o id de self é o mesmo do p!

if __name__ == '__main__':
    daniele= Pessoa('livia',nome='Daniele') # chama a classe pessoas mandando  a str Teste para nome
    michel= Pessoa(daniele, nome='Michel')# daniele vai para filhos
    for i in michel.lfi: # for chama michel.lfi que contem daniele e toca pra i
        print(i.nome) #nesse momento i contem daniele e pede pra imprimir daniele.nome

    print(daniele.idade, daniele.nome, daniele.lfi[0])
    print(f'o nome é {michel.nome} o sua idade é {michel.idade} anos ')
    daniele.sobrenome='Stein'

    print(daniele.sobrenome) # adiciona um atributo que nao esta em __init__
    michel.sobrenome='Santos'
    print(michel.sobrenome)
    del michel.sobrenome
   # del michel.sobrenome apaga um atributo
    print(daniele.__dict__) # mostra todos atributos de daniele
    print(michel.__dict__)


