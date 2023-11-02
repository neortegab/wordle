import tkinter as tk
from historial import Historial


class InterfazEstadisticas:

    def __init__(self, ventana_padre: tk.Tk, historial: Historial):
        self.historial = historial

        self.ventana: tk.Toplevel = tk.Toplevel(ventana_padre)
        self.ventana.title("Estadísticas")
        self.ventana.geometry("500x400")
        self.ventana.resizable(tk.FALSE, tk.FALSE)

        frame = tk.Frame(self.ventana)
        frame.grid(padx=10, pady=10)
        tk.Label(frame, text="Historial Estadisticas", font="TkHeadingFont").grid(row=0, column=0)

        frame_resultados = tk.Frame(self.ventana)
        frame_resultados.grid(padx=10, pady=10)

        tk.Label(frame_resultados, text="Total de partidas jugadas").grid(row=0, column=0, sticky=tk.W)
        tk.Label(frame_resultados, text=f"{self.historial.partidas_jugadas}").grid(row=0, column=1, sticky=tk.E)

        tk.Label(frame_resultados, text="Total de victorias").grid(row=1, column=0, sticky=tk.W)
        tk.Label(frame_resultados, text=f"{self.historial.partidas_ganadas}").grid(row=1, column=1, sticky=tk.E)

        tk.Label(frame_resultados, text="Total de derrotas").grid(row=2, column=0, sticky=tk.W)
        tk.Label(frame_resultados, text=f"{self.historial.partidas_perdidas}").grid(row=2, column=1, sticky=tk.E)

        tk.Label(frame_resultados, text="Procentaje de victorias").grid(row=3, column=0, sticky=tk.W)
        tk.Label(frame_resultados, text=f"{self.historial.porcentaje_victorias()}").grid(row=3, column=1, sticky=tk.E)

        tk.Label(frame_resultados, text="Procentaje de derrotas").grid(row=4, column=0, sticky=tk.W)
        tk.Label(frame_resultados, text=f"{self.historial.porcentaje_derrotas()}").grid(row=4, column=1, sticky=tk.E)

        tk.Label(frame_resultados, text="Promedio de intentos por partida").grid(row=5, column=0, sticky=tk.W)
        (tk.Label(frame_resultados, text=f"{self.historial.promedio_intentos_por_partida()}")
         .grid(row=5, column=1, sticky=tk.E))
