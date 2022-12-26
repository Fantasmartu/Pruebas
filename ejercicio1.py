print("Sistema vacacional de Rapi")


Nombre = input("Ingrese su nombre, por favor")

Clave = int(input("Ingrese su clave, por favor"))

Años = int(input("Ingrese los años que lleva en la empresa, por favor"))


if Clave == 1234:
    if Años == 1:
        print(Nombre + " Usted tiene 6 días de vacaciones.")
    elif (Años >= 2 )and (Años <= 6) :
        print(Nombre + " Usted tiene 14 días de vacaciones.")
    elif Años >= 7:
        print(Nombre + " Usted tiene 20 días de vacaciones.")
    else:
        print(Nombre + " Usted no tiene derecho a vacaciones.")