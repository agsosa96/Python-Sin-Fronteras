#Calculadora

try:
    primero = int(input("Ingrese primer numero: "))
    segundo = int(input("Ingrese segundo numero: "))

    print(f"La suma es: {primero + segundo}")
    print(f"La resta es: {primero - segundo}")
    print(f"La multiplicacion es: {primero * segundo}")
    print(f"La division es: {primero / segundo}")
except ValueError:
    print("Error!!! Solo se puede ingresar numero enteros. Intente de nuevo")
except ZeroDivisionError:
    print("No se puede divir por cero!!!")