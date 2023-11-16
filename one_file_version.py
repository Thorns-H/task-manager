
import sys
import os
import platform

import time
import random

import threading

import tkinter as tk

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

def update_clock(label: tk.Label) -> None:
    label.config(text = f'Time: {important_refences[1]}s')
    label.after(333, lambda: update_clock(label))
def display_clock() -> None:

    clock = tk.Tk()
    clock.title("Global Time")

    # Obtener las dimensiones de la pantalla

    screen_width = clock.winfo_screenwidth()
    screen_height = clock.winfo_screenheight()

    # Configurar el tamaño de la ventana

    clock_width = 300
    clock_height = 200

    x_pos = (screen_width - clock_width) // 2
    y_pos = (screen_height - clock_height) // 2
    
    clock.geometry(f"{clock_width}x{clock_height}+{x_pos}+{y_pos}")

    # Crear el label con texto grande y centrado

    big_clock = tk.Label(clock, text = f"Time: 0s", font = ("Helvetica", 20))
    big_clock.pack(pady = 50)

    update_clock(big_clock)

    clock.mainloop()

def display_processes(processes: dict) -> None:

    for process in processes:
        display_bars(f'P{process + 1}', 0, 6 + process, 30)

    time.sleep(1)

    for process, burst in processes.items():
        fill_bars(burst[0], 6 + process, 39)

    important_refences[0] = True

threads = []

clear_screen = "clear" if platform.system() == "Linux" else "cls" if platform.system() == "Windows" else None

def usage_simulation(num_cores: int, num_ram: int, core_bars: list, ram_bars: list) -> None:

    while not important_refences[0]:

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

        time.sleep(0.5)

        # Imprimimos el label de el uso de memoria ram.

        sys.stdout.write(f'\033[{7 + num_cores};0H            \033[36mMemory Usage{reset_color}\n')
        sys.stdout.flush()

        # Imprimimos las barras que simulan el consumo de la ram.

        for i in range(num_ram):
            display_bars(i + 1, ram_bars[i], i + num_cores + 8, 0)

        time.sleep(0.5)

        sys.stdout.write(f'\033[{5};30H          \033[36m Current Processes{reset_color}\n')
        sys.stdout.flush()

    sys.stdout.write(f'\033[{0};{0}H')
    sys.stdout.flush()

def main() -> None:

    num_cores = 4
    num_ram = 2
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
                process_size = int(input(f"Ingrese el tamaño del proceso {i + 1} (máximo 20): "))
                if 0 < process_size <= 20:
                    break
                else:
                    print("Por favor, ingrese un número mayor a 0 y menor o igual a 20.")
            except ValueError:
                print("Por favor, ingrese un número entero válido para el tamaño del proceso.")

        processes[i] = [process_size]

    # Creamos listas con la cantidad de barras.

    core_bars = [0] * num_cores
    ram_bars = [0] * num_ram

    os.system(clear_screen)

    thread = threading.Thread(target = usage_simulation, args = (num_cores, num_ram, core_bars, ram_bars))
    threads.append(thread)

    thread = threading.Thread(target = display_processes, args = (processes,))
    threads.append(thread)

    thread = threading.Thread(target = display_clock)
    threads.append(thread)

    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()

main()