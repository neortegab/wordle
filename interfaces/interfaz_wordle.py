import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class InterfazWordle:

    INSTRUCCIONES = (
        "Escriba una palabra en español de máximo 5 letras y presione el botón adivinar para hacer un "
        "intento."
    )

    def __init__(self, ventana_padre, wordle, lista_palabras, historial):
        self.wordle = wordle
        self.historial = historial
        self.lista_palabras = lista_palabras
        self.lista_labels_por_palabra = []
        self.num_intentos = tk.StringVar()

        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Jugar Wordle")
        self.ventana.geometry("720x710+185+10")
        self.ventana.resizable(tk.FALSE, tk.FALSE)
        self.imprimir_contenido()

    def imprimir_contenido(self):
        panel_principal = ttk.Frame(self.ventana)
        self.imprimir_cabecera(panel_principal)
        self.imprimir_tablero(panel_principal)
        self.imprimir_pie(panel_principal)

    def imprimir_cabecera(self, panel):
        instrucciones = ttk.Label(panel, text=self.INSTRUCCIONES)

        label_intentos_restantes = tk.Label(panel, textvariable=self.num_intentos)
        self.actualizar_intentos()
        panel.grid(row=0, column=0, padx=15, pady=15)
        (tk.Label(panel, text="Instrucciones", font="TkHeadingFont")
         .grid(row=0, pady=15))
        instrucciones.grid(row=1, column=0)
        label_intentos_restantes.grid(row=2, column=0, pady=10, sticky=tk.W)
        ttk.Separator(panel, orient=tk.HORIZONTAL).grid(sticky=(tk.W, tk.E))

    def actualizar_intentos(self):
        self.num_intentos.set(f"Intentos restantes: {self.wordle.intentos_restantes()}")

    def imprimir_tablero(self, panel):
        frame_palabras = tk.Frame(panel)
        frame_palabras.grid(padx=10, pady=10)

        for filas in range(self.wordle.MAX_INTENTOS):
            lista_labels_por_letra = []
            for columnas in range(self.wordle.MAX_LONGITUD_PALABRA):
                label = tk.Label(
                    frame_palabras,
                    bg="white",
                    borderwidth=1,
                    relief="solid"
                )
                label.grid(row=filas, column=columnas, ipadx=45, ipady=25)
                lista_labels_por_letra.append(label)
            self.lista_labels_por_palabra.append(lista_labels_por_letra)

        ttk.Separator(panel, orient=tk.HORIZONTAL).grid(sticky=(tk.W, tk.E))

    def imprimir_pie(self, panel):
        frame_entrada = tk.Frame(panel)
        frame_entrada.grid(padx=10, pady=10)

        tk.Label(frame_entrada, text="Ingrese su palabra en el siguiente recuadro:").grid(row=0, column=0, padx=10)
        palabra_ingresada = tk.StringVar()
        campo_entrada_palabra = ttk.Entry(
            frame_entrada,
            textvariable=palabra_ingresada,
            width=30
        )
        campo_entrada_palabra.grid(row=0, column=1)
        (ttk.Button(
            frame_entrada,
            text="Adivinar",
            command=lambda:self.agregar_palabra(palabra_ingresada.get())
        ).grid(column=1, pady=5))

    def agregar_palabra(self, palabra):
        if not self.es_palabra_valida(palabra):
            return
        self.wordle.agregar_intento(palabra.upper())
        resultados = self.wordle.adivinar(palabra.upper())
        self.imprimir_palabra_en_tablero(resultados)
        self.verificar_victoria_o_derrota()
        self.actualizar_intentos()

    def verificar_victoria_o_derrota(self):
        if not self.wordle.puede_continuar():
            if not self.wordle.esta_resuelto():
                messagebox.showinfo(message=f"¡Incorrecto! La palabra secreta era: {self.wordle.palabra_secreta}")
                self.ventana.destroy()
                return
            messagebox.showinfo(message=f"¡Correcto! La palabra secreta era: {self.wordle.palabra_secreta}")
            self.ventana.destroy()
            return

    def imprimir_palabra_en_tablero(self, resultados):
        for indice, resultado_letra in enumerate(resultados):
            labels = self.lista_labels_por_palabra[len(self.wordle.palabras_ingresadas)-1]
            if resultado_letra.esta_en_palabra:
                labels[indice].config(fg="yellow")
            elif resultado_letra.esta_en_posicion:
                labels[indice].config(fg="green")
            else:
                labels[indice].config(fg="gray")
            labels[indice].config(text=resultado_letra.letra)

    def es_palabra_valida(self, palabra):
        if len(palabra) is not self.wordle.MAX_LONGITUD_PALABRA:
            messagebox.showerror(
                message=f"La palabra ingresada debe contener {self.wordle.MAX_LONGITUD_PALABRA} caracteres"
            )
            return False
        if palabra not in self.lista_palabras:
            messagebox.showerror(message=f"La palabra ingresada no es una palabra válida")
            return False
        return True
