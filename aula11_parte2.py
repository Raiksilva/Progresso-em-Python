class Error (Exception):
    pass

class  InputError (Error):
    def __init__(self, menssage):
        self.message = menssage
while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 10')
        break
    except ValueError:
        print('Valor incorreto, por favor insira um numero de 0 a 10')
    except InputError as ex:
        print(ex)