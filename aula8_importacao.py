from aula7_televisao import Televisao
from aula7 import Calculadora
from aula8_contador_letras import contador_palavras, teste


if __name__ == '__main__':
    televisao = Televisao()
    print('Televisao ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisao ligada: {}'.format(televisao.ligada))
    calculadora = Calculadora(50,20)
    print(calculadora.divisao())
    lista = ['cachorro', 'gato']
    print(contador_palavras(lista))
    print(teste())