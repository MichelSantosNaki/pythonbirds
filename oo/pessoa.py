class Pessoa:
    def cumprimentar(self):
        return f'Olá Mundo {id(self)}' # se verificar o id de self é o mesmo do p!

if __name__ == '__main__':
    p= Pessoa()
    print(p.cumprimentar())
    print(id(p))



