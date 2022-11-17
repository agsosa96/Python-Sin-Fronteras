#Ingresar dos numeros sin usar el simbolo de multiplicacion

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

resultado = 0

for i in range(numero2):
    resultado = resultado + numero1

print(f"El resultado de la multiplicacion entre {numero1} y {numero2} es: {resultado}")