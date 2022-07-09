class Error (Exception):
    pass

class  InputError (Error):
    def __init__(self, menssage):
        self.message = menssage
while True:
    try:
        a = int(input('Primeiro bimestre: '))
        if a > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif a < 0:
            raise InputError('Nota não pode ser menor que 10')
        b = int(input('Segundo bimestre: '))
        if b > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif b < 0:
            raise InputError('Nota não pode ser menor que 10')
        c = int(input('Terceiro bimestre: '))
        if c > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif c < 0:
            raise InputError('Nota não pode ser menor que 10')
        d = int(input('Quarto bimestre: '))
        if d > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif d < 0:
            raise InputError('Nota não pode ser menor que 10')
        media = (a + b + c + d) / 4
        if a <= 10 and b <= 10 and c <= 10 and d <= 10:
            print('media: {med}'.format(med=media))
            if media >= 6:
                print('Você passou')
            elif media < 6:
                print('Você reprovou')
        break

    except ValueError:
        print('Valor incorreto, por favor insira um numero de 0 a 10')
    except InputError as ex:
        print(ex)




# a = int(input('Primeiro bimestre: '))
# while a > 10:
#     a = int(input('Você digitou errado a nota do Primeiro bimestre: '))
# b = int(input('Segundo bimestre: '))
# while b > 10:
#     b = int(input('Você digitou errado a nota do Segundo bimestre: '))
# c = int(input('Terceiro bimestre: '))
# while c > 10:
#     c = int(input('Você digitou errado a nota do Terceiro bimestre: '))
# d = int(input('Quarto bimestre: '))
# while d > 10:
#     d = int(input('Você digitou errado a nota do Quarto bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {med}'. format (med=media))
#     if media >= 6:
#         print('Você passou')
#     elif media < 6:
#         print('Você reprovou')




# a = int(input('selecione um valor: '))
# b = int(input('selecione um valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('esse valor é par')
# else:
#     print('nenhum valor par foi digitado')


# a = int(input('selecione um valor: '))
# resto = a % 2
# if resto == 0:
#     print('esse número é par')
#     soma = int(a) + 2
#     print(soma)
# elif resto != 0:
#     print('esse número é impar')
#     dividir = float(a) / 2
#     print(dividir)


# a = int (input('primeiro valor: '))
# b = int (input('segundo valor: '))
# c = int (input('terceiro valor: '))
# if a > b and a > c:
#     print('o maior é o primeiro valor {}'.format(a))
# elif b > a and b > c:
#     print('o maior é o segundo valor {}'.format(b))
# else:
#     print('o maior é o terceiro valor {}'. format(c))
# print('acabouu vlw')