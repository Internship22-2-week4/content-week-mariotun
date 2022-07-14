# Las tuplas son similares a las listas ,solo que las tuplas son inmutables
# Sus valores estan separados por comas
# tup=1,2,3 o tup=(1,2,3)
# Se utiliza comunmente para regresar mas de un valor en una funcion return(a,b)

# Los conjuntos(sets) son una coleccion sin orden que no permiten elementos duplicados

a = 1,2,3
print(type(a),'\n')

a = (1,2,3)
print(a[0])
print(a[1])
print(a[2])

# a[0] = 10 # error porque no podemos modificar la estructura

a = (1,1,1,2,3,4)
print('-----> Tupla a: {}'.format(a),'\n')
print(dir(a),'\n'*2)

print('-----> a.count(1): {}'.format(a.count(1)),'\n')
print('-----> a.count(2): {}'.format(a.count(2)),'\n')
print('-----> a.index(1): {}'.format(a.index(1)),'\n')
print('-----> a.index(3): {}'.format(a.index(3)),'\n')


print('*'*15,' Conjuntos ','*'*15)

a = set([1,2,3])
b = {3,4,6}
print('-----> a: {} , b: {}'.format(type(a),type(b)),'\n')
print('-----> a: {}'.format(a))
print('-----> b: {}'.format(b),'\n')

a.add(3) # no lo ingresa , porque no pueden tener valores duplicados
print('-----> a.add(3): {}'.format(a))

a.add(20)
print('-----> a.add(20): {}'.format(a))

print('-----> a.intersection(b): {}'.format(a.intersection(b)))
print('-----> a.union(b): {}'.format(a.union(b)))
print('-----> a.difference(b): {}'.format(a.difference(b)))
print('-----> b.difference(a): {}'.format(b.difference(a)))
print('-----> a.remove(20): a = {aa}'.format(a.remove(20),aa=a),'\n'*2)

print(dir(a))