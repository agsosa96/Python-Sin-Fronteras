#Mejorando Calculadora

try:
    primero = int(input("Ingrese el primer numero: "))
    segundo = int(input("Ingrese el segundo numero: "))
except:
    print("Error!!! Solo se puede ingresar numero. Intente nuevamente")
    exit()

simbolo = input("Ingrese la operacion: ")

try:
    if(simbolo == "+"):
        suma = primero + segundo
        print(f"El resultado de la suma es: {suma}")
    elif(simbolo == "-"):
        resta = primero - segundo
        print(f"El resultado de la resta es: {resta}")
    elif(simbolo == "*"):
        multiplicacion = primero * segundo
        print(f"El resultado de la multiplicacion es: {multiplicacion}")
    elif(simbolo == "/"):
        division = primero / segundo
        print(f"El resultado de la division es: {division}")
    else:
        print("El simbolo ingresado no es valido")
except ZeroDivisionError:
    print("No se puede dividir por cero")
