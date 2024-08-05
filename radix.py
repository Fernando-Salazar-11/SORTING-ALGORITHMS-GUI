import time
import matplotlib.pyplot as plot
import random

class Radix:
    def __init__(self, hacer_grafica_callback):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback

    def inserta_sample(self, lista):
        self.lista = lista

    def counting_sort(self, exp):
        n = len(self.lista)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = self.lista[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = self.lista[i] // exp
            output[count[index % 10] - 1] = self.lista[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            self.lista[i] = output[i]
            self.steps += 1
            self.hacer_grafica_callback(self.lista.copy())  # Use a copy to avoid modifying the original list

    def radix_sort(self):
        max_value = max(self.lista)
        exp = 1
        while max_value // exp > 0:
            self.counting_sort(exp)
            exp *= 10

    def sort(self, lista):
        self.inserta_sample(lista)
        self.radix_sort()
        return self.lista

        
# x = Radix()
# lista = random.sample(range(0, 20), 20)
# x.sort(lista, 0,)
