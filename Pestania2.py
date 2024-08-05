import tkinter as tk
from tkinter import ttk
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def bigO():
    def bubble_sort(lista):
        pasos = 0
        for i in range(len(lista) - 1):
            for j in range(len(lista) - 1 - i):
                pasos += 1
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return pasos
    
    
    
    def selection_sort(lista):
        pasos = 0
        for i in range(len(lista)):
            minimo = i
            for j in range(i + 1, len(lista)):
                pasos += 1
                if lista[j] < lista[minimo]:
                    minimo = j
            lista[i], lista[minimo] = lista[minimo], lista[i]
        return pasos
    
    
    def insertion_sort(lista):
        pasos = 0
        for i in range(1, len(lista)):
            key = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > key:
                lista[j + 1] = lista[j]
                j -= 1
                pasos += 1
            lista[j + 1] = key
        return pasos
    
    
    def counting_sort(lista):
        pasos = 0
        valor_maximo = max(lista)
        contar = [0] * (valor_maximo + 1)
    
        for numero in lista:
            contar[numero] += 1
            pasos += 1
    
        indice = 0
        for i in range(len(contar)):
            while contar[i] > 0:
                lista[indice] = i
                indice += 1
                contar[i] -= 1
                pasos += 1
        return pasos
    
    
    
    def shell_sort(lista):
        pasos = 0
        esp = len(lista) // 2
        while esp > 0:
            for i in range(esp, len(lista)):
                temp = lista[i]
                j = i
                while j >= esp and lista[j - esp] > temp:
                    lista[j] = lista[j - esp]
                    j -= esp
                    pasos += 1
                lista[j] = temp
            esp //= 2
        return pasos
    
    
    
    def quick_sort(lista):
        pasos = 0
    
        def partition(abajo, arriba):
            nonlocal pasos
            pivot = lista[arriba]
            i = abajo - 1
            for j in range(abajo, arriba):
                pasos += 1
                if lista[j] < pivot:
                    i += 1
                    lista[i], lista[j] = lista[j], lista[i]
            lista[i + 1], lista[arriba] = lista[arriba], lista[i + 1]
            return i + 1
    
        def Quick_rec(abajo, arriba):
            if abajo < arriba:
                pi = partition(abajo, arriba)
                Quick_rec(abajo, pi - 1)
                Quick_rec(pi + 1, arriba)
    
        Quick_rec(0, len(lista) - 1)
        return pasos
    
    
    def heap_sort(lista):
        pasos = 0
    
        def heapify(n, i):
            nonlocal pasos
            largo = i
            l = 2 * i + 1
            r = 2 * i + 2
    
            if l < n and lista[l] > lista[largo]:
                largo = l
                pasos += 1
    
            if r < n and lista[r] > lista[largo]:
                largo = r
                pasos += 1
    
            if largo != i:
                lista[i], lista[largo] = lista[largo], lista[i]
                heapify(n, i)
    
        n = len(lista)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
    
        for i in range(n - 1, 0, -1):
            lista[i], lista[0] = lista[0], lista[i]
            heapify(i, 0)
    
        return pasos
    
    
    def merge_sort(lista):
        pasos = 0
    
        def merge(izq, der):
            nonlocal pasos
            resultado = []
            i = 0
            j = 0
            while i < len(izq) and j < len(der):
                pasos += 1
                if izq[i] < der[j]:
                    resultado.append(izq[i])
                    i += 1
                else:
                    resultado.append(der[j])
                    j += 1
            resultado += izq[i:]
            resultado += der[j:]
            return resultado
    
        def merge_rec(lista):
            nonlocal pasos
            if len(lista) > 1:
                med = len(lista) // 2
                izq = lista[:med]
                der = lista[med:]
                izq = merge_rec(izq)
                der = merge_rec(der)
                return merge(izq, der)
            return lista
    
        lista_ordenada = merge_rec(lista)
        lista[:] = lista_ordenada
        return pasos
    
    
    def lista_random2k(size):
        return random.sample(range(1, size + 1), size)
    
    
    def lista_alreves(size):
        return list(range(size, 0, -1))
    
    
    
    def graficas():
        sizes = [100, 500, 1000, 1500, 2000]
    
        bubble_pasos, selection_pasos, insertion_pasos, contaring_pasos, shell_pasos, quick_pasos, heap_pasos, merge_pasos = [], [], [], [], [], [], [], []
    
        for size in sizes:
            if lista_rand.get() == "Valores Random":
                datos = lista_random2k(size)
            else:
                datos = lista_alreves(size)
    
            bubble_list = datos.copy()
            selection_list = datos.copy()
            insertion_list = datos.copy()
            contaring_list = datos.copy()
            shell_list = datos.copy()
            quick_list = datos.copy()
            heap_list = datos.copy()
            merge_list = datos.copy()
    
            bubble_pasos.append(bubble_sort(bubble_list))
            selection_pasos.append(selection_sort(selection_list))
            insertion_pasos.append(insertion_sort(insertion_list))
            contaring_pasos.append(counting_sort(contaring_list))
            shell_pasos.append(shell_sort(shell_list))
            quick_pasos.append(quick_sort(quick_list))
            heap_pasos.append(heap_sort(heap_list))
            merge_pasos.append(merge_sort(merge_list))
    
        fig, ax = plt.subplots()
        ax.plot(sizes, bubble_pasos, label="Bubble Sort")
        ax.plot(sizes, selection_pasos, label="Selection Sort")
        ax.plot(sizes, insertion_pasos, label="Insertion Sort")
        ax.plot(sizes, contaring_pasos, label="contaring Sort")
        ax.plot(sizes, shell_pasos, label="Shell Sort")
        ax.plot(sizes, quick_pasos, label="Quick Sort")
        ax.plot(sizes, heap_pasos, label="Heap Sort")
        ax.plot(sizes, merge_pasos, label="Merge Sort")
        ax.set_title("Comparación de Pasos - Algoritmos de Ordenamiento")
        ax.set_xlabel("Valores")
        ax.set_ylabel("Número de Pasos")
        ax.legend()
    
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.get_tk_widget().pack(pady=20)
        canvas.draw()
    
        tiempo_ejec = {
            "Bubble Sort": time.time(),
            "Selection Sort": time.time(),
            "Insertion Sort": time.time(),
            "contaring Sort": time.time(),
            "Shell Sort": time.time(),
            "Quick Sort": time.time(),
            "Heap Sort": time.time(),
            "Merge Sort": time.time()
        }
    
        datos = lista_random2k(2000)  
    
        bubble_sort(datos.copy())
        tiempo_ejec["Bubble Sort"] = time.time() - tiempo_ejec["Bubble Sort"]
    
    
        selection_sort(datos.copy())
        tiempo_ejec["Selection Sort"] = time.time() - tiempo_ejec["Selection Sort"]
    
        insertion_sort(datos.copy())
        tiempo_ejec["Insertion Sort"] = time.time() - tiempo_ejec["Insertion Sort"]
    
        counting_sort(datos.copy())
        tiempo_ejec["contaring Sort"] = time.time() - tiempo_ejec["contaring Sort"]
    
        shell_sort(datos.copy())
        tiempo_ejec["Shell Sort"] = time.time() - tiempo_ejec["Shell Sort"]
        
        quick_sort(datos.copy())
        tiempo_ejec["Quick Sort"] = time.time() - tiempo_ejec["Quick Sort"]
    
        heap_sort(datos.copy())
        tiempo_ejec["Heap Sort"] = time.time() - tiempo_ejec["Heap Sort"]
    
        merge_sort(datos.copy())
        tiempo_ejec["Merge Sort"] = time.time() - tiempo_ejec["Merge Sort"]
    
        text_tiiempo = "Tiempos de Ejecución (segundos):\n"
        for algo, exec_time in tiempo_ejec.items():
            text_tiiempo += f"{algo}: {exec_time:.6f} s\n"
        label_resultado.config(text=text_tiiempo)
    
    
    # GUI c
    root = tk.Tk()
    root.geometry("1000x800")
    root.title("Comparación de Algoritmos de Ordenamiento")
    
    
    frame = ttk.Frame(root)
    frame.pack(pady=20, padx=20)
    
    label_list_type = ttk.Label(frame, text="Seleccione tipo de lista:")
    label_list_type.pack(pady=5)
    
    valores_random = lista_random2k(2000)
    valores_random_str = [str(val) for val in valores_random]
    
    textocombo = "Valores Generados"
    valores_random_str.insert(0, textocombo)
    
    combobox = ttk.Combobox(frame, values=valores_random_str, state="readonly")
    combobox.pack(pady=10)
    
    combobox.set(textocombo)

    lista_rand = tk.StringVar()
    opcion_orden = ttk.Combobox(frame, textvariable=lista_rand, values=["Random", "Al revez"], state="readonly")
    opcion_orden.set("")
    opcion_orden.pack(pady=5)
    
    boton_grafica = ttk.Button(frame, text="Generar Gráficos", command=graficas)
    boton_grafica.pack(pady=10)
    
    label_resultado = ttk.Label(frame, text="Los resultados aparecerán aquí.")
    label_resultado.pack(pady=20)
    
    
    
    root.mainloop()
