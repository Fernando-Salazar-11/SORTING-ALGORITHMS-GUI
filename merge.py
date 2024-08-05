import time
import random
import matplotlib.pyplot as plot

class Merge:
    def __init__(self, hacer_grafica_callback):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback

    def inserta_sample(self, lista):
        self.lista = lista

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
                self.steps += 1
                self.hacer_grafica_callback(arr.copy())  # Use a copy to avoid modifying the original list

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                self.steps += 1
                self.hacer_grafica_callback(arr.copy())  # Use a copy to avoid modifying the original list

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                self.steps += 1
                self.hacer_grafica_callback(arr.copy())  # Use a copy to avoid modifying the original list

    def sort(self, lista):
        self.inserta_sample(lista)
        self.merge_sort(self.lista)
        return self.lista

        
# x = Merge()
# lista = random.sample(range(0, 20), 20)
# x.sort(lista, 0)
