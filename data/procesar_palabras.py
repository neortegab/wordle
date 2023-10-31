direccion_banco_palabras_crudo = "./banco_de_palabras_crudo.txt"


def main():
    archivo_destino = open("banco_palabras.txt", "w")
    with open(direccion_banco_palabras_crudo, "r") as archivo_origen:
        palabra = archivo_origen.readline()
        while palabra:
            archivo_destino.write(palabra.upper())
            palabra = archivo_origen.readline()
    archivo_destino.close()


if __name__ == "__main__":
    main()
