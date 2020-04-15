


'''

Você deve criar uma classe carro que deve conter 2 atributos compostos
por outras duas classes

1)Motor
2)Direção

O motor terá a responsabilidade de controlar a velocidade, ele oferece os seguintes atributos:
1) atributo de dado
2)metodo acelerar,  que deverá incrementar  a velocidade de  uma unidade
3)Método freia que deverá decrementar a velocidade em duas unidades

A direção terá a responsabildiade de controlar a direção, ela oferece o seguintes atributos:
1) Valor de direção com valores possiveis  : Norte , sul, leste , oeste
2)Método girar a direita direita, método dirar a esquerda

  N
O   l
  S


    Exemplo:

    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
'''
NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'


class Direcao:
    rotacao_direira_dct={NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE}
    rotacao_esquerda_dct={NORTE:OESTE,LESTE:NORTE,SUL:LESTE,OESTE:SUL}


    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor=self.rotacao_direira_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor=self.rotacao_esquerda_dct[self.valor]









class Carro():
    def __init__(self,direcao,motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


class Motor:
    def __init__(self):
        self.velocidade = 0

    pass

    def acelerar(self):
        self.velocidade+=1

    def frear(self):
        self.velocidade-=2
        self.velocidade=max(0,self.velocidade)


