class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print(f"Soy un {self.tipo} y mi sonifo es el: {self.onomatopeya}")


class Gato(Animal):
    tipo = "gato"
    #Si lo extiendo de esta manera lo que el metodo padre no se ejecuta y por eso lo tengo que volver a llamar. 
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print("Metodo extendido")


class Perro(Animal):
    tipo = "perro"
    #Si lo llamo de esta manera al usar la palabra reservada super llama directamente al metodo padre
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("Otro metodo extendido")


class Canario(Animal):
    tipo = "canario"

gato = Gato("Mamba", "Maullido")
gato.saludo()

gato = Perro("Manchas", "Ladrido")
gato.saludo()

gato = Canario("Piolin", "Silvido")
gato.saludo()
