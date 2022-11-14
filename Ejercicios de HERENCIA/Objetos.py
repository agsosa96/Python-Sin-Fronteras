class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print(f"Soy un {self.tipo} y mi sonifo es el: {self.onomatopeya}")


class Gato(Animal):
    tipo = "gato"

class Perro(Animal):
    tipo = "perro"

class Canario(Animal):
    tipo = "canario"

gato = Gato("Mamba", "Maullido")
gato.saludo()

gato = Perro("Manchas", "Ladrido")
gato.saludo()

gato = Canario("Piolin", "Silvido")
gato.saludo()
