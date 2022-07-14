import copy

countries = ['Guatemala','Costa Rica','Panama','Canada']
ages = [12,18,24,34,50]
print('---> Original Countries: {}'.format(countries))

print(id(countries))
print(id(ages))

weights = [12,18,24,34,50]
print(id(weights))

receta = ['Ensalada',2,'lechugas',5,'tomates']

countries[2] = 'Ecuador'
print('---> Posicion 2 cambiado: {}'.format(countries))

global_countries = countries
print('---> global sin modificar: {} ,---> contries: {}'.format(global_countries,countries))


global_countries = None
global_countries = copy.copy(countries)
print(countries,'\n')
countries [1] = 'EE.UU'
print(global_countries,countries,'\n')

for country in countries:
    print(country)