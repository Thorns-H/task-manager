
import sys
import time
import random

from imports.config import load_config
from imports.terminal import display_bars, reset_color

def main() -> None:

    # Inicializamos los datos de la simulación.

    config = load_config('config/config.json')

    num_cores = config['num_cores']
    num_ram = config['num_ram']
    num_processes = config['num_processes']

    # Creamos listas con la cantidad de barras.

    core_bars = [0] * num_cores
    ram_bars = [0] * num_ram
    process_bars = [0] * num_processes

    # Iniciamos el ciclo principal.

    while True:

        # Generamos los números randoms.

        for i in range(num_cores):
            core_bars[i] = random.randint(0, 20)

        for i in range(num_ram):
            ram_bars[i] = random.randint(0, 15)

        for i in range(num_processes):
            process_bars[i] = random.randint(0, 20)

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

        for i in range(num_processes):
            display_bars(i + 1, process_bars[i], i + 6, 30)
        
        time.sleep(1)

main()