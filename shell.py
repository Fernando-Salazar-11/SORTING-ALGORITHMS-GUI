import time
import matplotlib.pyplot as plot
import random

class Shell:
    def __init__(self, hacer_grafica_callback):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback

    def inserta_sample(self, lista):
        self.lista = lista

    def shell_sort(self): #Shell sort Knuth
        n = len(self.lista)
        gap = 1
        while gap <= n // 3:
            gap = gap * 3 + 1

        while gap > 0:
            for i in range(gap, n):
                temp = self.lista[i]
                j = i
                while j >= gap and self.lista[j - gap] > temp:
                    self.lista[j] = self.lista[j - gap]
                    j -= gap
                self.lista[j] = temp
                self.steps += 1
                self.hacer_grafica_callback(self.lista.copy())  # Use a copy to avoid modifying the original list
            gap //= 3

    def sort(self, lista):
        self.inserta_sample(lista)
        self.shell_sort()
        return self.lista
        
# x = Shell()
# lista = random.sample(range(0, 20), 20)
# x.sort(lista, 0,)
        