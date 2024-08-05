import time
import matplotlib.pyplot as plot
import random

class Counting:
    def __init__(self, hacer_grafica_callback=None):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback

    def inserta_sample(self, lista):
        self.lista = lista

    def counting_sort(self):
        max_val = max(self.lista)
        count_list = [0] * (max_val + 1)

        for num in self.lista:
            count_list[num] += 1

        sorted_list = []
        for i in range(len(count_list)):
            sorted_list.extend([i] * count_list[i])

            # Call the hacer_grafica_callback to update the graph
            if self.hacer_grafica_callback:
                self.hacer_grafica_callback(sorted_list.copy())  # Use a copy to avoid modifying the original list

        return sorted_list

    def sort(self, lista):
        self.inserta_sample(lista)
        return self.counting_sort()


        
# x = Counting()
# lista = random.sample(range(0, 20), 20)
# x.sort(lista, 0)