import sys
import time

# Codigo ASNI para resetear los colores usados con otras secuencias de escape.

reset_color = '\033[0m'
important_refences = [False, 0]

# Función encargada de imprimir las barras de progreso de nucleos y memoria ram. 

def display_bars(index: str | int, value: int, line: int, column: int) -> None:

    # Segun el valor, el color interno de la barra puede cambiar a rojo o verde.

    color = '\033[31m' if value > 10 else '\033[32m'

    bar = f'   {index} - [' + color + '|' * value + ' ' * (20 - value) + reset_color + ']'

    sys.stdout.write(f'\033[{line};{column}H{bar}\n')
    sys.stdout.flush()

def fill_bars(burst: int, line: int, column: int) -> None:

    # Segun el valor, el color interno de la barra puede cambiar a rojo o verde.

    color = '\033[32m'

    for i in range(burst):
        fill = color + '|' * (i + 1) + ' ' * (20 - burst) + reset_color
        sys.stdout.write(f'\033[{line};{column}H{fill}\n')
        sys.stdout.flush()

        time.sleep(0.3)

        important_refences[1] += 1
        sys.stdout.write(f'\033[{5};{68}H\033[36mGlobal Time:\033[0m \033[92m{important_refences[1]}s\033[0m\n')
        sys.stdout.flush()

    sys.stdout.write(f'\033[{line};{61}H\033[32mDone{reset_color}\n')

def display_processes(processes: dict) -> None:

    for process in processes:
        display_bars(f'P{process + 1}', 0, 6 + process, 30)

    time.sleep(1)

    for process, burst in processes.items():
        fill_bars(burst[0], 6 + process, 39)

    important_refences[0] = True