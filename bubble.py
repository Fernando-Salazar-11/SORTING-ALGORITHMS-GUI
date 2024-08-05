import time
import matplotlib.pyplot as plot
import random
#from matplotlib.backends.banked_tkagg import FigureCanvasTkgg


class Bubble:
    
    def __init__(self, hacer_grafica_callback):
        self.lista = []
        self.steps = 0
        self.hacer_grafica_callback = hacer_grafica_callback
        
    def inserta_sample(self, lista):      
        self.lista = lista

    def orden_burbuja(self):
        self.steps = 0
        for i in range(len(self.lista)-1):
            for j in range(len(self.lista)-1-i):
                self.steps += 1
                if self.lista[j] > self.lista[j+1]:
                    tempo = self.lista[j]
                    self.lista[j] = self.lista[j+1]
                    self.lista[j+1] = tempo
                    self.hacer_grafica_callback(self.lista)
                
    def sort(self, lista):
        self.inserta_sample(lista)
        self.orden_burbuja()
        return self.lista
    
    def sort_bigO(self, lista):
        self.inserta_sample(lista)
        self.orden_burbuja()
        return self.steps