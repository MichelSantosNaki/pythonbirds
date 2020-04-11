class Pessoa:
    def __init__(self,*filhos, nome=None, idade=27): # atributos
        self.nome = nome
        self.idade = idade
        self.lfi=list(filhos)



    def cumprimentar(self):
        return f'Olá Mundo {self.nome}' # se verificar o id de self é o mesmo do p!

if __name__ == '__main__':
    daniele= Pessoa(nome='Daniele') # chama a classe pessoas mandando  a str Teste para nome
    michel= Pessoa(daniele, nome='Michel')
    for i in michel.lfi:
        print(i.nome)
   # print(cadastro.cumprimentar())
    #mudando atributos
    #cadastro.nome= 'Michel' # agora atribuindo a str Michel.
   # print(cadastro.cumprimentar(), cadastro.idade)

