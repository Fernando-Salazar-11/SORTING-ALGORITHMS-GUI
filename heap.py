import time
import random
import matplotlib.pyplot as plot

class Heap:
    def __init__(self, hacer_grafica_callback):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback

    def inserta_sample(self, lista):
        self.lista = lista

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.lista[i] < self.lista[l]:
            largest = l

        if r < n and self.lista[largest] < self.lista[r]:
            largest = r

        if largest != i:
            self.lista[i], self.lista[largest] = self.lista[largest], self.lista[i]
            self.steps += 1
            self.hacer_grafica_callback(self.lista.copy())  # Use a copy to avoid modifying the original list

            self.heapify(n, largest)

    def heap_sort(self):
        n = len(self.lista)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.lista[i], self.lista[0] = self.lista[0], self.lista[i]
            self.steps += 1
            self.hacer_grafica_callback(self.lista.copy())  # Use a copy to avoid modifying the original list

            self.heapify(i, 0)

    def sort(self, lista):
        self.inserta_sample(lista)
        self.heap_sort()
        return self.lista

        
# x = Heap()
# lista = random.sample(range(0, 20), 20)
# x.sort(lista, 0)
