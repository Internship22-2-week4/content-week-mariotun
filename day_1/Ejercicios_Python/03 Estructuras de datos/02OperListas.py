# (append): Para añadir un elemento al final de la lista
# (pop): Para eliminar un elemento de la lista (pueder regresar ese valor)
# (sort): Para ordenar una lista
# (del): Para eliminar elementos
# (remove): Si se sabe que elemento eliminar

# a = list() o []

import random

a = list(range(0,15,2))
print('-----> a: {}'.format(a),'\n')

b = list(range(0,10))
print('-----> b: {}'.format(b),'\n')

print('-----> a+b: {}'.format(a+b),'\n')

print('-----> b*2: {}'.format(b*2),'\n')

fruits = []

fruits.append('apple')
print('-----> fruits: {}'.format(fruits))
print('---> len: {}'.format(len(fruits)))

fruits.append('orange')
print('-----> fruits: {}'.format(fruits))
print('---> len: {}'.format(len(fruits)))

fruits.append('kiwi')
print('-----> fruits: {}'.format(fruits))
print('---> len: {}'.format(len(fruits)),'\n')

some_fruit = fruits.pop()
print('---> some_fruit: {}'.format(some_fruit),)
print('-----> fruits: {}'.format(fruits),'\n')

some_fruit = fruits.pop(0)
print('---> some_fruit: {}'.format(some_fruit))
print('-----> fruits: {}'.format(fruits),'\n')

'''ddel = del fruits[0]
print(ddel)'''

random_numbers = []
for i in range(0,10): #(10)
    random_numbers.append(random.randint(0,15))

print('-----> random_numbers: {}'.format(random_numbers))

ordered_numbers = sorted(random_numbers)
print('-----> sorted: {}'.format(ordered_numbers))
print('-----> random_numbers: {}'.format(random_numbers))
random_numbers.sort()
print('-----> random_numbers .sort(): {}'.format(random_numbers),'\n'*3)

print(dir(random_numbers))