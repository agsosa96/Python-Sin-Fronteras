#Escribir una funcion que duelva el volumen de una esfera por su radio

def volumenEsfera(rad):
    volumen = 4/3 * 3.14 * rad ** 3

    return volumen

radio = int(input("Ingrese el radio: "))

print(f"El volumen es: {volumenEsfera(radio):.2f}")

