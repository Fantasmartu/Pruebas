#==================================================
print("===========================")
print("=.:Comparador de numeros:.=")
print("===========================")
num1 = int(input("Ingresa el primer numero, por favor. "))
num2 = int(input("Ingresa el segundo numero, por favor. "))
num3 = int(input("Ingresa el tercer numero, por favor. "))


if (num1>num2) and (num1>num3):
    print("El primero es más grande.")
elif num2 > num3:
    print("El segundo es más grande.")
else:
    print("El tercero es el más grande.")