import time
import matplotlib.pyplot as plot
import random

class Gnome:
    def __init__(self, hacer_grafica_callback):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback

    def inserta_sample(self, lista):
        self.lista = lista

    def gnome_sort(self):
        self.steps = 0
        pos = 0
        while pos < len(self.lista):
            if pos == 0 or self.lista[pos] >= self.lista[pos - 1]:
                pos += 1
            else:
                self.lista[pos], self.lista[pos - 1] = self.lista[pos - 1], self.lista[pos]
                pos -= 1
                self.steps += 1
                self.hacer_grafica_callback(self.lista.copy())  # Use a copy to avoid modifying the original list

    def sort(self, lista):
        self.inserta_sample(lista)
        self.gnome_sort()
        return self.lista

# x = Gnome()
# lista = random.sample(range(0, 20), 20)
# x.sort(lista, 0)