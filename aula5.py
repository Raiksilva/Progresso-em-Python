lista = [50,6,5,7]
lista_animal = ['cachorro', 'gato', 'elefante']

tupla = (1, 10, 12, 14, 1, 2, 3)
print(len(tupla))
print(len(lista_animal))
tuple_animal = tuple(lista_animal)
print(type(tuple_animal))
print(tuple_animal)
lista = list(tupla)
print(type(lista))
lista[0] = 100
print(lista)
# lista_animal[0]= 'macaco'
# print(lista_animal)
# print(lista_animal)
# nova_lista =  lista_animal * 3
# print(nova_lista)
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)
# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista, incluir lobo')
#     lista_animal.append('lobo')
#     print(lista_animal)