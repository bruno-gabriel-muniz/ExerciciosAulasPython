import sys
from os import getcwd
import pytest
from math import pi


def resolveBugDeImportacao():
    sys.path.append(getcwd())
    import Exercicios.ExerAulasPython062 as aula62

    return aula62


aula62 = resolveBugDeImportacao()


@pytest.mark.Done
def test_initObjetoGraficoBasic():
    test = aula62.ObjetoGrafico(6, 0, 6)
    assert test.corDePreenximento == 6
    assert test.preenxida == 0
    assert test.corDeContorno == 6

    test = aula62.ObjetoGrafico(2, 1, 4)
    assert test.corDePreenximento == 2
    assert test.preenxida == 1
    assert test.corDeContorno == 4


@pytest.mark.Done
def test_initObjetoGraficoError():
    AssertionError(aula62.ObjetoGrafico(2, 5, 4))
    AssertionError(aula62.ObjetoGrafico(2.2, 0, 4))
    AssertionError(aula62.ObjetoGrafico(2, 0, 4.2))


@pytest.mark.Done
def test_initRetangulo():
    test = aula62.Retangulo(1, 1, 1, 5.5, 4.3)
    assert test.altura == 4.3
    assert test.base == 5.5

    test = aula62.Retangulo(1, 1, 1, 1, 3)
    assert test.altura == 3
    assert test.base == 1


@pytest.mark.Done
def test_initRetanguloError():
    with pytest.raises(Exception) as erroAssert:
        aula62.Retangulo(1, 1, 1, 0, 8)
    assert erroAssert.value.args[0] == (
        'A altura e a base tem que ser maior'
        + ' que 0.\nbase = 0 e altura = 8.'
    )
    with pytest.raises(Exception) as erroAssert:
        aula62.Retangulo(1, 1, 1, 6.9, 0)
    assert erroAssert.value.args[0] == (
        'A altura e a base tem que ser maior'
        + ' que 0.\nbase = 6.9 e altura = 0.'
    )
    with pytest.raises(TypeError) as erroAssert:
        aula62.Retangulo(1, 1, 1, '8', 8)
    assert erroAssert.value.args[0] == (
        'A altura e a base tem que' + ' ser floats ou ints.'
    )


@pytest.mark.Done
def test_initTriangulo():
    test = aula62.Triangulo(1, 1, 1, 5.5, 4.3)
    assert test.altura == 4.3
    assert test.base == 5.5

    test = aula62.Triangulo(1, 1, 1, 1, 3)
    assert test.altura == 3
    assert test.base == 1


@pytest.mark.Done
def test_initTrianguloError():
    with pytest.raises(Exception) as erroAssert:
        aula62.Triangulo(1, 1, 1, 0, 8)
    assert erroAssert.value.args[0] == (
        'A altura e a base tem que ser maior'
        + ' que 0.\nbase = 0 e altura = 8.'
    )
    with pytest.raises(Exception) as erroAssert:
        aula62.Triangulo(1, 1, 1, 6.9, 0)
    assert erroAssert.value.args[0] == (
        'A altura e a base tem que ser maior'
        + ' que 0.\nbase = 6.9 e altura = 0.'
    )
    with pytest.raises(TypeError) as erroAssert:
        aula62.Triangulo(1, 1, 1, '8', 8)
    assert erroAssert.value.args[0] == (
        'A altura e a base tem que' + ' ser floats ou ints.'
    )


@pytest.mark.Done
def test_initCirculo():
    test = aula62.Circulo(1, 1, 1, 5.5)
    assert test.raio == 5.5

    test = aula62.Circulo(1, 1, 1, 1)
    assert test.raio == 1


@pytest.mark.Done
def test_initCirculoError():
    with pytest.raises(Exception) as erroAssert:
        aula62.Circulo(1, 1, 1, 0)
    assert erroAssert.value.args[0] == (
        'O raio tem que ser maior' + ' que 0.\nraio = 0.'
    )
    with pytest.raises(TypeError) as erroAssert:
        aula62.Circulo(1, 1, 1, '6.9')
    assert erroAssert.value.args[0] == ('O raio tem que ser floats ou ints.')
    with pytest.raises(TypeError) as erroAssert:
        aula62.Circulo(1, 1, 1, '8')
    assert erroAssert.value.args[0] == ('O raio tem que ser floats ou ints.')


@pytest.mark.Done
def test_areaRetangulo():
    test1 = aula62.Retangulo(1, 1, 1, 2, 2)
    test2 = aula62.Retangulo(1, 1, 1, 5.5, 1)
    test3 = aula62.Retangulo(1, 1, 1, 2, 9)

    assert test1.area() == 4
    assert test2.area() == 5.5
    assert test3.area() == 18


@pytest.mark.Done
def test_areaTriangulo():
    test1 = aula62.Triangulo(1, 1, 1, 2, 2)
    test2 = aula62.Triangulo(1, 1, 1, 18, 20)
    test3 = aula62.Triangulo(1, 1, 1, 5.5, 1)

    assert test1.area() == 2
    assert test2.area() == 180
    assert test3.area() == 2.75


@pytest.mark.Done
def test_areaCirculo():
    test1 = aula62.Circulo(1, 1, 1, 1)
    test2 = aula62.Circulo(1, 1, 1, 9)
    test3 = aula62.Circulo(1, 1, 1, 5)

    assert test1.area() == pi
    assert test2.area() == pi * 81
    assert test3.area() == pi * 25


@pytest.mark.Done
def test_perimetroRetangulo():
    test1 = aula62.Retangulo(1, 1, 1, 2, 2)
    test2 = aula62.Retangulo(1, 1, 1, 5.5, 1)
    test3 = aula62.Retangulo(1, 1, 1, 2, 9)

    assert test1.perimetro() == 8
    assert test2.perimetro() == 13
    assert test3.perimetro() == 22


@pytest.mark.Done
def test_perimetroTriangulo():
    test1 = aula62.Triangulo(1, 1, 1, 2, 2)

    with pytest.raises(TypeError) as errorAssert:
        test1.perimetro() == 8
    assert errorAssert.value.args[0] == (
        'Impossivel Saber O Perimetro Com Os Dados'
    )


@pytest.mark.Done
def test_perimetroCirculo():
    test1 = aula62.Circulo(1, 1, 1, 2)
    test2 = aula62.Circulo(1, 1, 1, 5)
    test3 = aula62.Circulo(1, 1, 1, 1)

    assert test1.perimetro() == 4 * pi
    assert test2.perimetro() == 10 * pi
    assert test3.perimetro() == 2 * pi
