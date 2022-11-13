#El ejercicio adivina si lo ingresado por el usuario se encuentra en la lista

dato = input("Ingrese un dato: ")

lista = ["hola", "mundo", "chanchito", "feliz", "dragones"]

if(lista.count(dato) > 0):
    print(f"El dato existe: {dato}")
else:
    print("El dato no existe: {dato}")