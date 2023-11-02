class Historial:

    def __init__(self):
        self.partidas_jugadas = 0
        self.partidas_ganadas = 0
        self.partidas_perdidas = 0
        self.intentos_por_partida = []

    def agregar_partida_jugada(self):
        self.partidas_jugadas = self.partidas_jugadas + 1

    def agregar_partida_ganada(self):
        self.partidas_ganadas = self.partidas_ganadas + 1

    def agregar_partida_perdida(self):
        self.partidas_perdidas = self.partidas_perdidas + 1

    def agregar_intentos_ultima_partida(self, num_intentos):
        self.intentos_por_partida.append(num_intentos)

    def porcentaje_victorias(self):
        if self.partidas_jugadas > 0:
            return f"{self.partidas_ganadas*100/self.partidas_jugadas}%"
        return "0"

    def porcentaje_derrotas(self):
        if self.partidas_jugadas > 0:
            return f"{self.partidas_perdidas*100/self.partidas_jugadas}%"
        return "0"

    def promedio_intentos_por_partida(self):
        if len(self.intentos_por_partida) == 0:
            return 0
        return sum(self.intentos_por_partida)/len(self.intentos_por_partida)

    def __repr__(self):
        return (f" ------------------------------ \n"
                f"           Historial            \n"
                f" ------------------------------ \n"
                f"  total_partidas_jugadas: {self.partidas_jugadas}\n"
                f"  total_victorias: {self.partidas_ganadas}\n"
                f"  total_derrotas: {self.partidas_perdidas}\n"
                f"  porcentaje_victorias: {self.porcentaje_victorias()}\n"
                f"  porcentaje_derrotas: {self.porcentaje_derrotas()}\n"
                f"  promedio_intentos_por_partida: {self.promedio_intentos_por_partida()}\n"
                f" ------------------------------ ")
