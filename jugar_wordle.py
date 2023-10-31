from historial import Historial
from wordle import Wordle
import random

# Entradas de Usuario
JUGAR = "1"
SALIR = "2"
ESTADISTICAS = "3"

# Colores en terminal
COLOR_ERROR_ANSI = "\033[1;31;49m"
COLOR_EN_PALABRA_ANSI = "\033[1;33;49m"
COLOR_NO_EN_PALABRA_ANSI = "\033[1;37;49m"
COLOR_EXITO_ANSI = "\033[1;32;49m"
COLOR_PREDETERMINADO = "\033[1;0m"


def palabra_es_longitud_correcta(palabra):
    return len(palabra) == Wordle.MAX_LONGITUD_PALABRA


def asignar_color_a_letras(resultados):
    resultados_a_color = ""
    for letra in resultados:
        color = ""
        if letra.esta_en_posicion:
            color = COLOR_EXITO_ANSI
        elif letra.esta_en_palabra:
            color = COLOR_EN_PALABRA_ANSI
        else:
            color = COLOR_NO_EN_PALABRA_ANSI
        resultados_a_color += f" {color}{letra.letra}{COLOR_PREDETERMINADO} "
    return resultados_a_color


def imprimir_adivinanza(wordle):
    for palabra in wordle.palabras_ingresadas:
        resultado = wordle.adivinar(palabra)
        letras_a_colores = asignar_color_a_letras(resultado)
        print(f"│{letras_a_colores}│")


def imprimir_intentos_restantes(wordle):
    for _ in range(wordle.intentos_restantes()):
        print(f"│{' _ ' * wordle.MAX_LONGITUD_PALABRA}│")


def imprimir_tablero(wordle):
    cantidad_lineas = Wordle.MAX_LONGITUD_PALABRA * 2 + Wordle.MAX_LONGITUD_PALABRA
    borde_superior = "┍" + "━" * cantidad_lineas + "┑"
    borde_inferior = "┕" + "━" * cantidad_lineas + "┙"
    print(borde_superior)
    imprimir_adivinanza(wordle)
    imprimir_intentos_restantes(wordle)
    print(borde_inferior)


def agregar_victoria_o_derrota(historial, wordle):
    if wordle.esta_resuelto():
        historial.agregar_partida_ganada()
        print(f"{COLOR_EXITO_ANSI}Victoria. La palabra secreta es {wordle.palabra_secreta}{COLOR_PREDETERMINADO}")
    else:
        historial.agregar_partida_perdida()
        print(
            f"{COLOR_ERROR_ANSI}Derrota. Intente nuevamente. "
            f"La palabra secreta era {wordle.palabra_secreta}{COLOR_PREDETERMINADO}"
        )
    historial.agregar_intentos_ultima_partida(len(wordle.palabras_ingresadas))


def realizar_intentos(wordle, lista_de_palabras):
    while wordle.puede_continuar():
        print(wordle.INSTRUCCIONES)
        print(f"Intentos restantes: {wordle.intentos_restantes()}")
        palabra = input("Escriba su intento: ")
        if palabra not in lista_de_palabras:
            print("La palabra escrita no es una palabra válida.")
        if not palabra_es_longitud_correcta(palabra):
            print(
                f"{COLOR_ERROR_ANSI}La palabra a ingresar solo puede tener una longitud de máximo "
                f"{Wordle.MAX_LONGITUD_PALABRA} letras."
                f"{COLOR_PREDETERMINADO}"
            )
            continue
        wordle.agregar_intento(palabra.upper())
        imprimir_tablero(wordle)


def jugar_wordle(historial, palabra_secreta, lista_de_palabras):
    historial.agregar_partida_jugada()
    wordle = Wordle(palabra_secreta)
    realizar_intentos(wordle, lista_de_palabras)
    agregar_victoria_o_derrota(historial, wordle)


def imprimir_menu_principal():
    print(
        f"Escriba la opción y presione enter.\n"
        f"{JUGAR}. Jugar.\n"
        f"{SALIR}. Salir.\n"
        f"{ESTADISTICAS}. Estadísticas."
    )


def cargar_banco_de_palabras():
    lista_de_palabras = []
    with open("./data/banco_palabras.txt", "r") as archivo:
        palabra = archivo.readline()
        while palabra:
            lista_de_palabras.append(palabra.strip())
            palabra = archivo.readline()
    return lista_de_palabras


def main():
    esta_jugando = True
    lista_de_palabras = cargar_banco_de_palabras()
    palabra_secreta = random.choice(lista_de_palabras)
    historial = Historial()
    print(f"Bienvenido a Wordle.")
    while esta_jugando:
        imprimir_menu_principal()
        opcion = input()
        if opcion == JUGAR:
            jugar_wordle(historial, palabra_secreta, lista_de_palabras)
        elif opcion == SALIR:
            esta_jugando = False
        elif opcion == ESTADISTICAS:
            print(historial)


if __name__ == "__main__":
    main()
