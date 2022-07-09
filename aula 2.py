a = int (input('digite o primeiro valor:'))
b = int (input('digite o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('soma:{soma}. '
      '\nmultiplicação: {vezes}.  '
      '\ndivisão: {div}.'
      ' \nresto: {resto}. '
      '\nsubtração: {sub}.'
      . format(soma=soma, sub=subtracao,vezes=multiplicacao, div= (divisao),resto=resto))
# x = '1'
# soma2 = int (x) + 2
# print('soma2 = ',soma2)
print(type(divisao))