
passUsuario = 12345;

valor = int(input("Ingrese un numero: "))

if valor == passUsuario:
    print("El numero es correcto")
else:
    while valor != passUsuario:
        valor = int(input("Ingrese un numero: "))
