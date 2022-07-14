# Es una asociacion entre llaves (keys) y valores(values)
# Los diccionarios se inicializan con {} o con la funcion dict

rae = {}
rae['pizza'] = 'La comida mas deliciosa del mundo' 
rae['pasta'] = 'La comida mas sabrosa de italia' 

print('Diccionario: rae ---> {}'.format(rae),'\n')

print(rae['pizza'],'\n')

#print(rae['helado'],'\n')
a = rae.get('helado',None)# llave no existe
print(a,'\n')

a = rae.get('pasta',None)# llave si existe
print(a,'\n')

print('-----> rae.keys(): {}'.format(rae.keys()),'\n')
print('-----> rae.values(): {}'.format(rae.values()),'\n')
print('-----> rae.items(): {}'.format(rae.items()),'\n')

for key in rae.keys():
    print(key)
print('*'*30)

for value in rae.values():
    print(value)
print('*'*30)

for key,value in rae.items():
    print(key,value)

print('*'*30,'\n'*2)

print(dir(rae),'\n'*2)
print('-----> rae.__contains__(1): {}'.format(rae.__contains__(1)))
print('-----> rae.__sizeof__()): {}'.format(rae.__sizeof__()))