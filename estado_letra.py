class EstadoLetra:

    def __init__(self, letra):
        self.letra = letra
        self.esta_en_posicion = False
        self.esta_en_palabra = False

    def __repr__(self):
        return f"[{self.letra}: esta en posicion: {self.esta_en_posicion}, esta en la palabra: {self.esta_en_palabra}]"
