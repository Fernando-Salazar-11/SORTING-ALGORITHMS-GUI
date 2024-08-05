import time
import matplotlib.pyplot as plot
import random

class Insertion:
    def __init__(self, hacer_grafica_callback):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback

    def inserta_sample(self, lista):
        self.lista = lista

    def insertion_sort(self):
        for i in range(1, len(self.lista)):
            key = self.lista[i]
            j = i - 1
            while j >= 0 and key < self.lista[j]:
                self.lista[j + 1] = self.lista[j]
                j -= 1
                self.steps += 1
                self.hacer_grafica_callback(self.lista.copy())  # Use a copy to avoid modifying the original list
            self.lista[j + 1] = key
            self.hacer_grafica_callback(self.lista.copy())  # Use a copy to avoid modifying the original list

    def sort(self, lista):
        self.inserta_sample(lista)
        self.insertion_sort()
        return self.lista

        
# x = Insertion()
# lista = random.sample(range(0, 20), 20)
# x.sort(lista, 0)