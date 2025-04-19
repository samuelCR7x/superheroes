class Personaje:
    def __init__(self, nombre, poder, universo):
        self._nombre = nombre
        self._poder = poder
        self._universo = universo

    def __str__(self):
        return f"{self._nombre} del universo {self._universo} con el poder de {self._poder}"

class Heroe(Personaje):
    def __init__(self, nombre, poder, universo, equipo):
        super().__init__(nombre, poder, universo)
        self._equipo = equipo

    def __str__(self):
        return f"Héroe: {super().__str__()} - Miembro de: {self._equipo}"

class Villano(Personaje):
    def __init__(self, nombre, poder, universo, nivel_maldad):
        super().__init__(nombre, poder, universo)
        self._nivel_maldad = nivel_maldad

    def __str__(self):
        return f"Villano: {super().__str__()} - Nivel de Maldad: {self._nivel_maldad}"
