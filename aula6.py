# conjunto = {1, 2, 5, 9}
# conjunto2 = {2, 9, 8, 9}
# conjunto_uniao = conjunto.union(conjunto2)
# print('união: {}'.format(conjunto_uniao))
# conjunto_interseccao = conjunto.intersection(conjunto2)
# print('intersecção: {}'.format(conjunto_interseccao))
# conjunto_diferenca1 = conjunto.difference(conjunto2)
# conjunto_diferenca2 = conjunto2.difference(conjunto)
# print('diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
# print('diferença entre 1 e 2: {}'.format(conjunto_diferenca2))
# conjunto_diff_simetrica =  conjunto.symmetric_difference(conjunto2)
# print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))
# conjunto_a = {1, 2, 3}
# conjunto_b = {1, 2, 3, 4}
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# print('A é subconjunto de B: {}'.format(conjunto_subset))
# conjunto_superset = conjunto_b.issuperset(conjunto_a)
# print('B é superconjunto de A: {}'.format(conjunto_superset))


lista = ['cachorro', 'gato', 'elefante', 'gato', 'lobo', 'leão', 'leão']
print(lista)
conjunto_animal = set(lista)
print(conjunto_animal)
lista = list(conjunto_animal)
print(lista)

# conjunto = {1, 2, 3, 4, 5}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)
# print(type(conjunto))