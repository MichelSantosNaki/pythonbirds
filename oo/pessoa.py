from builtins import classmethod


class Pessoa:
    olhos=2
    def __init__(self,*filhos, nome=None, idade=27): # atributos
        self.nome = nome
        self.idade = idade
        self.lfi=list(filhos)



    def cumprimentar(self):
        return f'Olá Mundo {self.nome}'                             # se verificar o id de self é o mesmo do p!

    @staticmethod
    def metodo_estatico():
        return  42
    @classmethod
    def nomes_e_atributos_de_classes(cls):
        return f'{cls}, olhos {cls.olhos}, '
if __name__ == '__main__':
    daniele= Pessoa('livia',nome='Daniele')                         # chama a classe pessoas mandando  a str Teste para nome
    michel= Pessoa(daniele, nome='Michel')                          # daniele vai para filhos
    for i in michel.lfi:                                            # for chama michel.lfi que contem daniele e toca pra i
        print(i.nome)                                               #nesse momento i contem daniele e pede pra imprimir daniele.nome

    print(daniele.idade, daniele.nome, daniele.lfi[0])
    print(f'o nome é {michel.nome} o sua idade é {michel.idade} anos ')
    daniele.sobrenome='Stein'

    print(daniele.sobrenome)                                        # adiciona um atributo que nao esta em __init__
    michel.sobrenome='Santos'
    print(michel.sobrenome)
    del michel.sobrenome
    print(f' O id:{id(michel)} ',michel.olhos,f'id de ohos michel{michel.olhos}')
    print(f' O id:{id(daniele)} ',daniele.olhos,f'id de ohos michel{daniele.olhos}')
    print(michel.olhos)
    print(Pessoa.olhos)
    # del michel.sobrenome apaga um atributo
    print(daniele.__dict__)                                          # mostra todos atributos de daniele
    print(michel.__dict__)
    print(Pessoa.metodo_estatico(), michel.metodo_estatico())       #posso chamar direto da classe ou do objeto da classe
    print(Pessoa.nomes_e_atributos_de_classes(), michel.nomes_e_atributos_de_classes())       #posso chamar direto da classe ou do objeto da classe

