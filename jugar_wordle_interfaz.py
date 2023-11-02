from interfaces.interfaz_principal import InterfazPrincipal
import random


def cargar_banco_de_palabras():
    lista_de_palabras = []
    with open("./data/banco_de_palabras_crudo.txt", "r") as archivo:
        palabra = archivo.readline()
        while palabra:
            lista_de_palabras.append(palabra.strip())
            palabra = archivo.readline()
    return lista_de_palabras


def main():
    palabras = cargar_banco_de_palabras()
    palabra_secreta = random.choice(palabras)
    interfaz_principal = InterfazPrincipal(palabra_secreta.upper(), palabras)
    interfaz_principal.iniciar_interfaz()


if __name__ == "__main__":
    main()
