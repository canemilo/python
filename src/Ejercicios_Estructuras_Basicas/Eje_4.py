lluviaUsuario = int(input("Ingrese lluvia en mm: "))

alertaAmarilla = 60;
alertaRoja = 120;

if lluviaUsuario >= alertaAmarilla:
    print("RIESGO ALERTA AMARILLA")
elif lluviaUsuario >= alertaRoja:
    print("RIESGO ALERTA ROJA")
else:
    print("NO EXISTE ALERTA")


lluvia2 = int(input("Ingrese lluvia en mm: "))

match lluvia2:
    case x if x >= alertaAmarilla:
        print("RIESGO ALERTA AMARILLA")
    case x if x >= alertaRoja:
        print("RIESGO ALERTA ROJA")
    case _:
        print("NO EXISTE ALERTA")
