print("=================")
print("=.:Calculadora:.=")
print("=================\n")

print("1 Suma")
print("2 Resta")
print("3 Multiplicacion")
print("4 Division")
print("5 Division entera")
print("6 Exponente")
print("7 Modulo o resto")

opcion = int(input("Ingresa tu opcion deseada "))

if opcion == 1:
    num = int(input("ingrese el primer numero "))
    num += int(input("ingrese el segundo numero "))
    
    print("El resultado es: ", num)

elif opcion == 2:
    num = int(input("ingrese el primer numero "))
    num -= int(input("ingrese el segundo numero "))
    
    print("El resultado es: ", num)
    
elif opcion == 3:
    num = int(input("ingrese el primer numero "))
    num *= int(input("ingrese el segundo numero "))
    
    print("El resultado es: ", num)
elif opcion == 4:
    num = float(input("ingrese el primer numero "))
    num /= float(input("ingrese el segundo numero "))
    
    print("El resultado es: ", num)
elif opcion == 5:
    num = (input("ingrese el primer numero "))
    num //= int(input("ingrese el segundo numero "))
    
    print("El resultado es: ", num)
elif opcion == 6:
    num = int(input("ingrese el primer numero "))
    num **= int(input("ingrese el segundo numero "))
    
    print("El resultado es: ", num)
    
elif opcion == 7:
    num = int(input("ingrese el primer numero "))
    num %= int(input("ingrese el segundo numero "))
    
    print("El resultado es: ", num)
else:
    print("La opcion no es correcta")