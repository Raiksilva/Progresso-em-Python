nota_a = int(input('insira nota do primeiro bismestre: '))
while nota_a > 10:
    nota_a = int(input('insira nota do primeiro bismestre: '))
# NOTA do segundo bimestre
nota_b = int(input('insira nota do segundo bismestre: '))
while nota_b > 10:
    nota_b = int(input('insira nota do segundo bismestre: '))
nota_final = (nota_a + nota_b) / 2
# resultado final
if nota_final <= 10:
    if nota_final >= 6:
        print('você foi aprovado com {}, parabéns'. format(nota_final))
    else:
        print('você foi reprovado com {}'. format(nota_final))
# a = 0
# while a <= 10:
#     print(a)
#     a+=1

# NÚMEROS PRIMOS NO VALOR QUE O USUÁRIO DIGITAR
# a = int(input('Selecione o valor desejado: '))
# for i in range(a+1):
#     div = 0
#     for x in range(1, i+1):
#         resto = i % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(i)


#IMPRESÂO DOS NÙMEROS PRIMOS
# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo'. format(a))
# else:
#     print('Número {} não é primo'. format (a))

print('fim do programa^^')