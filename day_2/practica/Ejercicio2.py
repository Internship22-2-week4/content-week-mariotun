def calcularImpuestos(edad,ingresos):
    try:
        if (edad >= 18) and (ingresos >= 1000):
            return (ingresos*(40/100))
        else:
            return 0
    except:
        return 'Invalid data'

# código de prueba
print(calcularImpuestos(18, 1000)) # 400
print(calcularImpuestos(40, 10000)) # 4000
print(calcularImpuestos(17, 5000)) # 0
print(calcularImpuestos(30, 500)) # 0
print(calcularImpuestos("", 500)) # Invalid data