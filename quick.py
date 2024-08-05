import time
import random
import matplotlib.pyplot as plot


class Quick:
    def __init__(self, hacer_grafica_callback):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback

    def inserta_sample(self, lista):
        self.lista = lista

    def partition(self, arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.steps += 1
                self.hacer_grafica_callback(arr.copy())  # Use a copy to avoid modifying the original list

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.steps += 1
        self.hacer_grafica_callback(arr.copy())  # Use a copy to avoid modifying the original list
        return i + 1

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def sort(self, lista):
        self.inserta_sample(lista)
        self.quick_sort(self.lista, 0, len(self.lista) - 1)
        return self.lista

        
# x = Quick()
# lista = random.sample(range(0, 20), 20)
# x.sort(lista, 0,)
        