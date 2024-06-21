"""
Defina uma nova classe ObjetoGráfico subclasse de object, cujos atributos são:
    cor_de_preenximento --> inteiro
    preenchida --> bool
    cor_de_contorno --> inteiro

Escreva três classes:
    Retangulo --> Atributos: base e altura
    Circulo --> Atributos: raio
    Triangulo --> Atributos: base e altura

Subclasses da classe ObjetoGráfico que possuam
todas métodos area e perimetro.
"""
from math import pi


class ObjetoGrafico(object):
    def __init__(
        self, corDePreenximento: int, preenxida: bool, corDeContorno: int
    ) -> None:
        self.corDePreenximento = corDePreenximento
        self.preenxida = preenxida
        self.corDeContorno = corDeContorno


class Retangulo(ObjetoGrafico):
    def __init__(
        self,
        corDePreenximento: int,
        preenxida: bool,
        corDeContorno: int,
        base: float,
        altura: float,
    ) -> None:

        super().__init__(corDePreenximento, preenxida, corDeContorno)
        #
        # verificando se a base e  a altura eh inteiro ou float
        if not (
            isinstance(base, (int, float)) and isinstance(altura, (int, float))
        ):
            #
            raise TypeError('A altura e a base tem que ser floats ou ints.')
        if base <= 0 or altura <= 0:
            raise Exception(
                'A altura e a base tem que ser maior que 0.\n'
                + f'base = {base} e altura = {altura}.'
            )
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return (self.base + self.altura) * 2


class Circulo(ObjetoGrafico):
    def __init__(
        self,
        corDePreenximento: int,
        preenxida: bool,
        corDeContorno: int,
        raio: float,
    ) -> None:

        super().__init__(corDePreenximento, preenxida, corDeContorno)
        # verificamos se o raio nao eh um inteiro ou um int
        if not (isinstance(raio, (int, float))):
            #
            raise TypeError('O raio tem que ser floats ou ints.')
        if raio <= 0:
            raise Exception(f'O raio tem que ser maior que 0.\nraio = {raio}.')
        self.raio = raio

    def area(self) -> float:
        return self.raio**2 * pi

    def perimetro(self) -> float:
        return 2 * pi * self.raio


class Triangulo(ObjetoGrafico):
    def __init__(
        self,
        corDePreenximento: int,
        preenxida: bool,
        corDeContorno: int,
        base: float,
        altura: float,
    ) -> None:

        super().__init__(corDePreenximento, preenxida, corDeContorno)
        self.base = base
        self.altura = altura
        #
        # verificando se a base e  a altura eh inteiro ou float
        if not (
            isinstance(base, (int, float)) and isinstance(altura, (int, float))
        ):
            #
            raise TypeError('A altura e a base tem que ser floats ou ints.')
        if base <= 0 or altura <= 0:
            raise Exception(
                'A altura e a base tem que ser maior que 0.\n'
                + f'base = {base} e altura = {altura}.'
            )

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def perimetro(self) -> TypeError:
        raise TypeError('Impossivel Saber O Perimetro Com Os Dados')
