from interfaces.interfaz_wordle import InterfazWordle
from interfaces.interfaz_estadisticas import InterfazEstadisticas
from wordle import Wordle
from historial import Historial
import tkinter as tk
from tkinter import ttk


def mostrar_titulo(mainframe):
    label_titulo = ttk.Label(mainframe, text="Bienvenido a Wordle")
    label_titulo['font'] = "TkHeadingFont"
    label_titulo.grid(column=0, row=0, rowspan=2, ipady=20, sticky=tk.N)


class InterfazPrincipal:

    def __init__(self, palabra_secreta, lista_palabras):
        self.palabra_secreta = palabra_secreta
        self.lista_palabras = lista_palabras
        self.historial = Historial()

        self.ventana = tk.Tk()
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.columnconfigure(0, weight=1)
        self.inicializar_ventana()

    def mostrar_ventana_estadisticas(self):
        InterfazEstadisticas(self.ventana, self.historial)

    def mostrar_ventana_juego(self):
        wordle = Wordle(self.palabra_secreta)
        InterfazWordle(self.ventana, wordle, self.lista_palabras, self.historial)

    def mostrar_botones(self, mainframe):
        button_frame = ttk.Frame(mainframe)
        button_frame.grid()
        buttons = {
            'Jugar': self.mostrar_ventana_juego,
            'Estadísticas': self.mostrar_ventana_estadisticas,
            'Salir': self.ventana.destroy
        }
        for nombre, accion in buttons.items():
            button = ttk.Button(button_frame, text=nombre, width=30, command=accion)
            button.grid(padx=5, pady=2, ipadx=10, ipady=10)

    def mostrar_menu_principal(self):
        mainframe = ttk.Frame(self.ventana)
        mainframe.grid(column=0, row=0, pady=20, padx=5)
        mostrar_titulo(mainframe)
        self.mostrar_botones(mainframe)

    def inicializar_ventana(self):
        self.ventana.title("Wordle")
        self.ventana.geometry("400x400+150+200")
        self.ventana.resizable(tk.FALSE, tk.FALSE)
        self.mostrar_menu_principal()

    def iniciar_interfaz(self):
        self.ventana.mainloop()
