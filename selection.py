import time
import matplotlib.pyplot as plot
import random

class Selection:
    def __init__(self, hacer_grafica_callback):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback

    def inserta_sample(self, lista):
        self.lista = lista

    def selection_sort(self):
        n = len(self.lista)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.lista[j] < self.lista[min_index]:
                    min_index = j
            if min_index != i:
                self.lista[i], self.lista[min_index] = self.lista[min_index], self.lista[i]
                self.steps += 1
                self.hacer_grafica_callback(self.lista.copy())  # Use a copy to avoid modifying the original list

    def sort(self, lista):
        self.inserta_sample(lista)
        self.selection_sort()
        return self.lista


        
# x = Selection()
# lista = random.sample(range(0, 20), 20)
# x.sort(lista, 0,)
        