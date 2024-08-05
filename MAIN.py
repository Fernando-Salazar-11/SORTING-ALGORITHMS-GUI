import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time


from bubble import Bubble
from selection import Selection
from insertion import Insertion
from counting import Counting
from shell import Shell
from quick import Quick
from heap import Heap
from merge import Merge
from radix import Radix
from gnome import Gnome
import Pestania2




class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Parcial 2 - Fernando Salazaar y Oscar Aguirre")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)
        
        #Botones de pausa/reanudar
        self.boton_pausa = tk.Button(self.frame, text="Pausar", command=self.pausar_ordenamiento)
        self.boton_pausa.grid(row=5, column=1, pady=10)
        self.boton_reanudar = tk.Button(self.frame, text="Reanudar", command=self.reanudar_ordenamiento)
        self.boton_reanudar.grid(row=5, column=2, pady=10)
        self.ejecutador = True

        # Titutlo Algoritmos
        self.titulo = tk.Label(self.frame, text="Algoritmos de Ordenamiento", font=("Arial", 18, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=4, pady=10)

        # Label de ordenamientos y combobox de los ordenamientos
        self.label_ord = tk.Label(self.frame, text="Selecciona el algoritmo con el cual deseas ordenar:")
        self.label_ord.grid(row=1, column=0, pady=5, sticky="e")

        self.ord_entrada = tk.StringVar()
        self.combobox_ord = ttk.Combobox(self.frame, textvariable=self.ord_entrada, state="readonly")
        self.combobox_ord['values'] = ("Bubble Sort", "Selection Sort", "Insertion Sort",
                                             "Counting Sort", "Shell Sort", "Quick Sort",
                                             "Heap Sort", "Merge Sort", "Radix Sort", "Gnome Sort")
        self.combobox_ord.grid(row=1, column=1, pady=5, padx=10, columnspan=3, sticky="nsew")

        # Label y Radiobuttons de la velocidad
        self.label_velocidad = tk.Label(self.frame, text="Selecciona la velocidad de Ordenamiento:")
        self.label_velocidad.grid(row=2, column=0, pady=5, sticky="e")

        self.velocidad_ordenamiento = tk.DoubleVar(value=1.0)
        
        self.velocidad_lenta = tk.Radiobutton(self.frame, text="Lenta", variable=self.velocidad_ordenamiento, value=1.25)
        self.velocidad_lenta.grid(row=2, column=1, pady=5, sticky="w")

        self.velocidad_media = tk.Radiobutton(self.frame, text="Media", variable=self.velocidad_ordenamiento, value=.75)
        self.velocidad_media.grid(row=2, column=2, pady=5, sticky="w")

        self.velocidad_rapida = tk.Radiobutton(self.frame, text="Rápida", variable=self.velocidad_ordenamiento, value=0)
        self.velocidad_rapida.grid(row=2, column=3, pady=5, sticky="w")

        # Label y Entry para la cantidad de números aleatorios 
        self.label_cantidad = tk.Label(self.frame, text="Escribe la cantidad de números aleatorios:")
        self.label_cantidad.grid(row=3, column=0, pady=5, sticky="e")

        self.cantidad_ent = tk.Entry(self.frame)
        self.cantidad_ent.grid(row=3, column=1, pady=5, padx=10, columnspan=2, sticky="nsew")

        self.generar_button = tk.Button(self.frame, text="Generar", command=self.valores_random)
        self.generar_button.grid(row=3, column=3, pady=5, sticky="w")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()
        
        self.boton_pestaña2 = tk.Button(self.frame, text="Pestaña 2", command=self.abrir_pestaña2)
        self.boton_pestaña2.grid(row=5, column=3, pady=10)

        # self.algoritmo_ordenamiento = None
        # self.ordenamiento_pausado = False
        # self.hilo_ordenamiento = None
        
        self.lista = []
        
    def abrir_pestaña2(self):
        Pestania2.bigO()
        
    def valores_random(self):
        cantidad = self.cantidad_ent.get()
        try:
            cantidad = int(cantidad)
            if cantidad < 10 or cantidad > 1000:
                tk.messagebox.showerror("Error", "La cantidad debe estar entre 10 y 1000")
                return
            self.lista = random.sample(range(1, cantidad + 1), cantidad)
        except ValueError:
            tk.messagebox.showerror("Error", "La cantidad debe ser un entero")
            return
        
        self.utilizar_ordenamiento()
        
    def utilizar_ordenamiento (self, event=None):
        ord_elegido = self.combobox_ord.get()
        if ord_elegido == "Bubble Sort":
            self.algoritmo_ordenamiento = Bubble(self.hacer_grafica)
        elif ord_elegido == "Selection Sort":
            self.algoritmo_ordenamiento = Selection(self.hacer_grafica)
        elif ord_elegido == "Insertion Sort":
            self.algoritmo_ordenamiento = Insertion(self.hacer_grafica)
        if ord_elegido == "Counting Sort":
            self.algoritmo_ordenamiento = Counting(self.hacer_grafica)
        elif ord_elegido == "Shell Sort":
            self.algoritmo_ordenamiento = Shell(self.hacer_grafica)
        elif ord_elegido == "Quick Sort":
            self.algoritmo_ordenamiento = Quick(self.hacer_grafica)
        elif ord_elegido == "Heap Sort":
            self.algoritmo_ordenamiento = Heap(self.hacer_grafica)
        elif ord_elegido == "Merge Sort":
            self.algoritmo_ordenamiento = Merge(self.hacer_grafica)
        elif ord_elegido == "Radix Sort":
            self.algoritmo_ordenamiento = Radix(self.hacer_grafica)
        elif ord_elegido == "Gnome Sort":
            self.algoritmo_ordenamiento = Gnome(self.hacer_grafica)
        
        if self.algoritmo_ordenamiento:
            self.velocidad = self.get_velocidad()
            sorted_list = self.algoritmo_ordenamiento.sort(self.lista)
            self.hacer_grafica(sorted_list)
        
            
    def get_velocidad(self):
        velocidad_seleccionada = self.velocidad_ordenamiento.get()
        return velocidad_seleccionada
    
    def pausar_ordenamiento(self):
        self.ejecutador = False

    def reanudar_ordenamiento(self):
        self.ejecutador = True
        self.utilizar_ordenamiento()
    
    def hacer_grafica(self, lista):
        if not lista:
            return  # No hacer nada si la lista está vacía
        if self.ejecutador:
            time.sleep(self.get_velocidad())
            plt.clf()
            plt.bar(range(len(lista)), lista)
            plt.xlabel("Indice")
            plt.ylabel("Valores")
            plt.show()
            self.canvas.delete("all")
        
            # Tamaño máximo para la gráfica
            max_width = 700  # Ancho máximo
            max_height = 300  # Altura máxima
            
            # Escalar la gráfica según el tamaño máximo
            escala_x = max_width / (len(lista) * 10 + (len(lista) - 1) * 5)
            escala_y = max_height / max(lista)
            
            bar_width = 10 * escala_x
            spacing = 5 * escala_x
            grafica_height = max_height if max_height < self.canvas.winfo_height() else self.canvas.winfo_height()
            inicio_x = (self.canvas.winfo_width() - len(lista) * (bar_width + spacing)) / 2
            inicio_y = self.canvas.winfo_height() - grafica_height - 100  # 100 píxeles debajo del tope del canvas
            
            for i, value in enumerate(lista):
                x0 = inicio_x + i * (bar_width + spacing)
                y0 = inicio_y + grafica_height - value * escala_y
                x1 = x0 + bar_width
                y1 = inicio_y + grafica_height
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="green")
            self.canvas.create_text(self.canvas.winfo_width() / 2, inicio_y - 40, text="Gráfica de ordenamiento", font=("Arial", 16, "bold"))
            self.canvas.create_text(inicio_x + max_width / 2, inicio_y + grafica_height + 20, text="Índice")
            self.canvas.create_text(inicio_x - 20, inicio_y + grafica_height / 2, text="Valor", angle=90)
            self.canvas.update()
        
       

def main():
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()