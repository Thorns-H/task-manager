
import sys
import time
import random

import threading

from imports.config import load_config
from imports.terminal import display_bars, display_processes, reset_color

threads = []

def main() -> None:

    # Inicializamos los datos de la simulación.

    config = load_config('config/config.json')

    num_cores = config['num_cores']
    num_ram = config['num_ram']
    num_processes = 0

    # Pedimos al usuario la cantidad de procesos

    while True:
        try:
            num_processes = int(input("Ingrese la cantidad de procesos: "))
            if num_processes >= 1:
                break
            else:
                print("Por favor, ingrese un número mayor o igual a 1.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    # Creamos un diccionario para almacenar la información de cada proceso

    processes = {}

    # Por cada proceso, solicitamos el tamaño y lo agregamos al diccionario

    for i in range(num_processes):
        while True:
            try:
                process_size = int(input(f"Ingrese el tamaño del proceso {i + 1}: "))
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido para el tamaño del proceso.")

        processes[i] = [process_size]

    # Creamos listas con la cantidad de barras.

    core_bars = [0] * num_cores
    ram_bars = [0] * num_ram

    # Iniciamos el ciclo principal.

    while True:

        # Generamos los números randoms.

        for i in range(num_cores):
            core_bars[i] = random.randint(0, 20)

        for i in range(num_ram):
            ram_bars[i] = random.randint(0, 15)

        # Imprimimos el label de los nucleos del procesador.

        sys.stdout.write(f'\033[{5};0H          \033[36mProcessor Cores{reset_color}\n')
        sys.stdout.flush()

        # Imprimimos las barras que simulan el uso de los nucleos.

        for i in range(num_cores):
            display_bars(i + 1, core_bars[i], i + 6, 0)

        # Imprimimos el label de el uso de memoria ram.

        sys.stdout.write(f'\033[{7 + num_cores};0H            \033[36mMemory Usage{reset_color}\n')
        sys.stdout.flush()

        # Imprimimos las barras que simulan el consumo de la ram.

        for i in range(num_ram):
            display_bars(i + 1, ram_bars[i], i + num_cores + 8, 0)

        # Movemos a la altura del primer label y movemos 30 columnas a la derecha.
        # Después imprimimos un label de procesos.

        sys.stdout.write(f'\033[5;30H            \033[36m Processes{reset_color}\n')
        sys.stdout.flush()

        # Imprimimos las barras de procesos.

        # TODO: Falta agregar una función que siga la lógica de 'display_bars' pero
        # no tome un número random, sino un algoritmo como FCFS, RR o Queues.

        input()

main()