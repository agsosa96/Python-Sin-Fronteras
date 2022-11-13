#Validacion de Variable

primero = input("Ingrese el primer numero: ")

try:
    primero = int(primero)
except:
    primero = "Erroneo"

if(primero == 'Erroneo'):
    print("El valor ingresado no es un entero")
    exit()

segundo = input("Ingrese el segundo numero: ")

try:
    segundo = int(segundo)
except:
    segundo = "Erroneo"

if(segundo == 'Erroneo'):
    print("El valor ingresado no es un entero")
    exit()


print(primero + segundo)