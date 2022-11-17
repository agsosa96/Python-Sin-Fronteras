#Ingrese nombre y apellido e imprimirlo al reves

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")

nombreApellido = nombre + ' ' + apellido

print(f"El nombre y apellido al reves es: {nombreApellido[::-1]}")