def contrasenaValida (constrasena):
    if (constrasena=='2Fj(jjbFsuj') or (constrasena=='eoZiugBf&g9'):
        return True
    else:
        return False
 
# código de prueba
print(contrasenaValida("2Fj(jjbFsuj")) # true
print(contrasenaValida("eoZiugBf&g9")) # true
print(contrasenaValida("hola")) # false
print(contrasenaValida("")) # false
print(contrasenaValida(345)) # false
print(contrasenaValida(234.45)) # false


