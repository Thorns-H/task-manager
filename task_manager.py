import os
import time

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

class Task:
    key = 0
    start = 0
    length = 0

class Manager:
    tasks = []
    
    def shellSort(self):
    
        gapSeries= [510774,227011,100894,44842,19930,8858,3937,1750,701,301,132,57,23,10,4,1,0]
        gapPos = 0 
        gap = int(gapSeries[gapPos])
        newarray = self.tasks.copy()

        while gap>0:
            i = gap
            while i <= len(newarray)-1:
                j = i
                while j>= gap and newarray[j - gap].start > newarray[j].start:
                    aux = newarray[j - gap]
                    newarray[j - gap] = newarray[j]
                    newarray[j] = aux
                    j-=gap
                i+=1
            gapPos+=1
            gap=gapSeries[gapPos]

        return newarray
    
    def addTasks(self):
        os.system("cls")
        print("CAPTURA DE TAREAS")
        while True:
            t = Task()
            t.key = len(self.tasks) + 1
            print(f"\nTAREA NO. {t.key}")
            t.start = int(input(" INGRESA   INICIO: "))
            t.length =   int(input(" INGRESA DURACION: "))
            self.tasks.append(t)
            print("¿DESEA AGREGAR OTRA TAREA?")
            while True:
                s = input("(S/N)-> ")
                s = s.upper()
                if s[0] == 'S':
                    break
                if s[0] == 'N':
                    return
                
    def tasksMonitor(self):
        if len(self.tasks) == 0:
            print("NO HAY TAREAS.")
            input("PRESIONA UNA TECLA PARA REGRESAR AL MENU")
            return
        
        total = 0
        elapsed = 0
        orderByStart = self.shellSort()
        os.system("cls")
        print("MONITOR DE TAREAS\n")
        print("DATOS DE LAS TAREAS:")
        print("TAREA\tINICIO\tDURACION")
        for t in self.tasks:
            print(f"T{t.key}\t{t.start}\t{t.length}")
            end = t.start + t.length
            if end > total:
                total = end
        input("PRESIONA UNA TECLA PARA INICIAR")
        print("\nORDEN DE EJECUCION:")
        print("TAREA\tEJECUCION")
        while True:
            for t in orderByStart:
                if t.start > elapsed:
                    current = t.start 
                elif (t.start + t.length) > elapsed:
                    current = elapsed
                else:
                    current = t.start + t.length
                print(f"T{t.key}\t{current}")  
            print(f"TIEMPO GLOBAL: {elapsed}")
            if elapsed == total:
                break
            else:
                for i in range((len(orderByStart) + 1)):
                    print(LINE_UP, end=LINE_CLEAR)
                elapsed += 1
                time.sleep(0.5)
        input("\nPRESIONA UNA TECLA PARA REGRESAR AL MENU")
        
def menu():
    os.system("cls")
    print("ADMINISTRADOR DE TAREAS\n")
    print("MENU PRINCIPAL")
    print("  1.- AGREGAR TAREAS")
    print("  2.- INICIAR TAREAS")
    print("  3.- SALIR")
    while True:
        x = int(input("ELIGE UNA OPCION: "))
        if x > 0 and x < 4:
            break
    return x
            
def main():
    m = Manager()
    while True:
        x = menu()
        if x == 1:
            m.addTasks()
        elif x == 2:
            m.tasksMonitor()
        else:
            break

main()
