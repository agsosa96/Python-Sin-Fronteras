#Escribir una funcion que encuentre el elemento menor de una lista

def menorNumero(listaNumero):
    menor = min(listaNumero)

    return menor


lista = [1, 3, 45, -15, 56, 7, 13, 597, 11, 59, 23, -78]

print(f"{menorNumero(lista)}")
