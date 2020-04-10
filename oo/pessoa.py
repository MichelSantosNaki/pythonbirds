class Pessoa:
    def __init__(self, nome=None): # atributos
        self.nome=nome
    def cumprimentar(self):
        return f'Olá Mundo {self.nome}' # se verificar o id de self é o mesmo do p!

if __name__ == '__main__':
    p= Pessoa('Teste') # chama a classe pessoas mandando  a str Teste para nome
    print(p.cumprimentar() )
    #mudando atributos
    p.nome='Michel' # agora atribuindo a str Michel
    print(p.cumprimentar())



