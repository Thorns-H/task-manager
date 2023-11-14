import sys

# Codigo ASNI para resetear los colores usados con otras secuencias de escape.
reset_color = '\033[0m'

#Función encargada de imprimir las barras de progreso de nucleos y memoria ram. 

def display_bars(index, value, line, column) -> None:

    # Segun el valor, el color interno de la barra puede cambiar a rojo o verde.

    color = '\033[31m' if value > 10 else '\033[32m'

    bar = f'   {index} - [' + color + '|' * value + ' ' * (20 - value) + reset_color + ']'

    sys.stdout.write(f'\033[{line};{column}H{bar}\n')
    sys.stdout.flush()