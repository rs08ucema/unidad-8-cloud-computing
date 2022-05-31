import random

class Novela:

    def __init__(self, titulo, origen):
        self.__id = random.randint(0, 1000000)
        self.titulo = titulo
        self.origen = origen

    def __str__(self):
        return f"\n\t|| Novela ||\n" \
               f"\tTitulo: {self.titulo}\n" \
               f"\tOrigen: {self.origen}\n"