
lista = [1, 10]
try:
    arquivo = open('isso.txt', 'r')
    texto = arquivo.read()
    divisao = 7 / 0
    numero = lista[1]
    # x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Erro ao acessar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('executa quando não ocorre exceção')
finally:
    print('fechando arquivo')
    arquivo.close()