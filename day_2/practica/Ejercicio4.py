def bmi(peso,altura):
    try:
        valor_bmi = (peso/altura**2)
        if valor_bmi < 18.5:
            return 'Bajo de peso'
        elif (valor_bmi >= 18.5) and (valor_bmi <= 24.9):
            return 'Normal'
        elif (valor_bmi >=25) and (valor_bmi <=29.9):
            return 'Sobrepeso'
        else:
            return 'Obeso'
    except:
        return 'Invalid data'

# código de prueba
print(bmi(65, 1.8)) # "Normal"
print(bmi(72, 1.6)) # "Sobrepeso"
print(bmi(52, 1.75)) #  "Bajo de peso"
print(bmi(135, 1.7)) # "Obeso"
print(bmi('123', 1.7)) # "Invalid data"