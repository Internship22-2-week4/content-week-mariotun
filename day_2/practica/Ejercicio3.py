def likes(numero):
    try:
        convert = str(numero)
        if numero < 1000:
            return str(numero)
        elif (numero >= 1000) and (numero < 1000000):
            return convert[0:-3]+'K'
        elif (numero >= 1000000) and (numero < (10**12)):
            return convert[0:-6]+'M'
        else:
            return 'No scope'
    except:
        return 'Invalid data'

# código de prueba
print(likes(983)) # "983"
print(likes(1900)) # "1K"
print(likes(54000)) # "54K"
print(likes(120800)) # "120K"
print(likes(25222444)) # "25M"
print(likes('fsd')) # "Invalid data"