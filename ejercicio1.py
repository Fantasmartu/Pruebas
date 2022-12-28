print("=======================================================")
print(".:Sistema vacacional de Rappi:.")
print("=======================================================")
Nombre = input("Ingrese su nombre, por favor ")
print("=======================================================")
Clave = int(input("Ingrese su clave, por favor "))
print("=======================================================")
Años = int(input("Ingrese los años que lleva en la empresa, por favor "))
print("=======================================================")
#====================================================================
if Clave == 1234:
    if Años == 1:
        print(Nombre + " Usted tiene 6 días de vacaciones.")
    elif (Años >= 2 )and (Años <= 6) :
        print(Nombre + " Usted tiene 14 días de vacaciones.")
    elif Años >= 7:
        print(Nombre + " Usted tiene 20 días de vacaciones.")
    else:
        print(Nombre + " Usted no tiene derecho a vacaciones.")
#====================================================================
elif Clave == 4321:
    if Años == 1:
        print(Nombre + " Usted tiene 7 días de vacaciones.")
    elif (Años >= 2 )and (Años <= 6):
        print(Nombre + " Usted tiene 15 días de vacaciones.")
    elif Años >= 7:
        print(Nombre + " Usted tiene 22 días de vacaciones.")
    else:
        print(Nombre + " Usted no tiene derecho a vacaciones.")
#====================================================================
elif Clave == 4231:
    if Años == 1:
        print(Nombre + " Usted tiene 10 días de vacaciones.")
    elif (Años >= 2 )and (Años <= 6):
        print(Nombre + " Usted tiene 20 días de vacaciones.")
    elif Años >= 7:
        print(Nombre + " Usted tiene 30 días de vacaciones.")
    else:
        print(Nombre + " Usted no tiene derecho a vacaciones.")
#====================================================================
else:
    print ("Clave Incorrecta")
#====================================================================