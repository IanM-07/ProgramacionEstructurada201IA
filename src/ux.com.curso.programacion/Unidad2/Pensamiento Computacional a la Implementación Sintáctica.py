intentos = 0
clave_correcta = "1234"

while intentos < 3:
    contrasena = input("Ingrese clave: ")
    
    if contrasena == clave_correcta:
        print("Acceso concedido")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta")

if intentos == 3:
    print("Cuenta bloqueada")
    