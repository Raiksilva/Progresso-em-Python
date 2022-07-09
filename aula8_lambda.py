contatador_letras = lambda lista: [len(x) for x in lista]

lista_a = ['cachorro', 'japiti', 'gato']
print(contatador_letras(lista_a))

soma = lambda a,b: a + b
subtracao = lambda a, b: a - b
print(soma(5,4))
print(subtracao(5,8))

calculadora = {
    'soma': lambda  a,b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda  a, b: a / b,
}

soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print('A soma é:{}'.format(soma(5, 8)))
print('A multiplicacao é: {}'.format(multiplicacao(5, 6)))