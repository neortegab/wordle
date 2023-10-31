from estado_letra import EstadoLetra


class Wordle:

    INSTRUCCIONES = (f"Escriba una palabra en español de máximo 5 letras y presione 'enter' para adivinar la palabra "
                     f"oculta.")
    MAX_INTENTOS = 6
    MAX_LONGITUD_PALABRA = 5

    def __init__(self, palabra_secreta):
        self.palabra_secreta = palabra_secreta.upper()
        self.palabras_ingresadas = []

    def agregar_intento(self, palabra_ingresada):
        self.palabras_ingresadas.append(palabra_ingresada)

    def esta_resuelto(self):
        return (len(self.palabras_ingresadas) > 0 and
                self.palabras_ingresadas[len(self.palabras_ingresadas)-1] == self.palabra_secreta)

    def intentos_restantes(self):
        return self.MAX_INTENTOS - len(self.palabras_ingresadas)

    def puede_continuar(self):
        return self.intentos_restantes() > 0 and not self.esta_resuelto()

    def adivinar(self, palabra):
        resultados = []
        for posicion, letra in enumerate(palabra):
            resultado_letra = EstadoLetra(letra)
            resultado_letra.esta_en_palabra = letra in self.palabra_secreta
            resultado_letra.esta_en_posicion = self.palabra_secreta[posicion] == letra
            resultados.append(resultado_letra)
        return resultados
