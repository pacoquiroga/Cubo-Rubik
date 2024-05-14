
import numpy as np
import random
import os
from colorama import init, Fore, Style

init()

class CuboRubik:
    #Constructor
    def __init__(self):
        self.cubo = np.array([
            [[f"{Fore.RED}■{Fore.RESET}"] * 3 for _ in range(3)],
            [[f"{Fore.MAGENTA}■{Fore.RESET}"] * 3 for _ in range(3)],
            [['■'] * 3 for _ in range(3)],
            [[f"{Fore.YELLOW}■{Fore.RESET}"] * 3 for _ in range(3)],
            [[f"{Fore.GREEN}■{Fore.RESET}"] * 3 for _ in range(3)],
            [[f"{Fore.BLUE}■{Fore.RESET}"] * 3 for _ in range(3)]])

    movimientos = ['B', 'R', 'N', 'A', 'X', 'V']
    direccionMovimineto = ['H','AH']
    combinacionesRealizadas = []
    numCombinacionesRealizadas = 0

    ##FUNCIONES PRINCIPALES
    #ROTAR CARA
    def rotar(self, cara, direccion):
        if cara not in self.movimientos:
            print("Capa inválida")
            return
        if direccion not in self.direccionMovimineto:
            print("Dirección inválida")
            return
        # Realizar el movimiento
        if cara == 'B':
            self.moverB(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['B',direccion])
        if cara == 'R':
            self.moverR(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['R', direccion])
        if cara == 'N':
            self.moverN(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['N', direccion])
        if cara == 'A':
            self.moverA(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['A', direccion])
        if cara == 'X':
            self.moverX(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['X', direccion])
        if cara == 'V':
            self.moverV(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['V', direccion])
            #print("La cara "+cara+" se movio en sentido "+direccion)

    #DESORDENAR ALEATORIAMENTE
    def desordenar(self):
        numMovimientos = random.randrange(0, 23, 1)
        self.movimientosAleatorios(numMovimientos)

    #REALIZAR X NUMERO DE MOVIMIENTOS ALEATORIOS
    def movimientosAleatorios(self, numMovimientos):
        print("Cubo Inicial")
        self.imprimirCubo()
        os.system("pause")
        for i in range(numMovimientos):
            os.system("cls")
            movAleatorio = random.choice(self.movimientos)
            direccionAleatoria = random.choice(self.direccionMovimineto)
            self.rotar(movAleatorio, direccionAleatoria)
            print("Movimiento " + (str)(i+1))
            print("La cara: " + movAleatorio + " se movio en sentido " + direccionAleatoria)
            self.imprimirCubo()
            os.system("pause")

    def armar(self):
        os.system("cls")
        combinaciones = self.combinacionesRealizadas[::-1]
        for combinacion in combinaciones:
            if(combinacion[1] == "H"):
                self.rotar(combinacion[0], "AH")
                print("La cara: " + combinacion[0] + " se movio en sentido AH")
            if (combinacion[1] == "AH"):
                self.rotar(combinacion[0], "H")
                print("La cara: " + combinacion[0] + " se movio en sentido H")
            self.imprimirCubo()
            os.system("pause")
            print()
        self.combinacionesRealizadas = []
        self.numCombinacionesRealizadas = 0
                

    ##FUNCIONES SECUNDARIAS
    #MOVER CARA BLANCA
    def moverB(self, direccion):
        if direccion.upper() == 'H':
            self.horarioB()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioB()

    def horarioB(self):
        self.cubo[2] = np.rot90(self.cubo[2], 1)  # gira cara superior (Blanco)
        temp = np.copy(self.cubo[0][0])  # guarda la fila superior de la cara frontal (Rojo)
        self.cubo[0][0] = self.cubo[4][0]  # mueve fila superior de cara izquierda (Verde) a cara frontal
        self.cubo[4][0] = self.cubo[1][0]  # mueve fila superior de cara posterior (Naranja) a cara izquierda
        self.cubo[1][0] = self.cubo[5][0]  # mueve fila superior de cara derecha (Azul) a cara posterior
        self.cubo[5][0] = temp  # mueve fila guardada a cara derecha

    # MOVER CARA AMARILLA
    def moverA(self, direccion):
        if direccion.upper() == 'H':
            self.horarioA()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioA()

    def horarioA(self):
        self.cubo[3] = np.rot90(self.cubo[3], -1)  # gira cara superior (Blanco)
        temp = np.copy(self.cubo[0][2])  # guarda la fila superior de la cara frontal (Rojo)
        self.cubo[0][2] = self.cubo[4][2]  # mueve fila superior de cara izquierda (Verde) a cara frontal
        self.cubo[4][2] = self.cubo[1][2]  # mueve fila superior de cara posterior (Naranja) a cara izquierda
        self.cubo[1][2] = self.cubo[5][2]  # mueve fila superior de cara derecha (Azul) a cara posterior
        self.cubo[5][2] = temp  # mueve fila guardada a cara derecha

    # MOVER CARA NARANJA
    def moverN(self, direccion):
        if direccion.upper() == 'H':
            self.horarioN()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioN()

    def horarioN(self):
        self.cubo[1] = np.rot90(self.cubo[1], -1)  # gira cara posterior (Naranja)
        temp = np.copy(self.cubo[2][0])  # guarda la primera fila de la cara superior (Blanco)
        self.cubo[2][0] = self.cubo[5][:,2]  # mueve columna 2 de cara derecha (Azul) a la primera fila de cara superior
        self.cubo[5][:, 2] = self.cubo[3][2]  # mueve tercera fila de cara inferior (Amarillo) a columna 3 de cara derecha
        self.cubo[3][2] = self.cubo[4][:,0]  # mueve la primera columna de cara izquierda (Verde) a la ultima fila de cara inferior
        self.cubo[4][:, 0] = temp  # mueve fila guardada a columna izquierda de cara izquierda

    # MOVER CARA ROJA
    def moverR(self, direccion):
        if direccion.upper() == 'H':
            self.horarioR()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioR()

    def horarioR(self):
        self.cubo[0] = np.rot90(self.cubo[0], -1)  # gira cara posterior (Naranja)
        temp = np.copy(self.cubo[2][2])  # guarda la tercera fila de la cara superior (Blanco)
        self.cubo[2][2] = self.cubo[4][:, 2][::-1] # mueve columna 3 de cara izquierda a la tercera fila de cara superior
        self.cubo[4][:, 2] = self.cubo[3][0]  # mueve primera fila de cara inferior (Amarillo) a columna 3 de cara izquierda
        self.cubo[3][0] = self.cubo[5][:,0][::-1]  # mueve la primera columna de cara derecha a la primera fila de cara inferior
        self.cubo[5][:, 0] = temp  # mueve fila guardada a columna 1 de cara derecha

    # MOVER CARA AZUL
    def moverX(self, direccion):
        if direccion.upper() == 'H':
            self.horarioX()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioX()

    def horarioX(self):
            self.cubo[5] = np.rot90(self.cubo[5], -1)  # gira cara X
            temp = np.copy(self.cubo[2][:, 2])  # guarda la ultima columna de la cara B
            self.cubo[2][:, 2] = self.cubo[0][:,2]  # mueve la ultima columna de cara frontal (R) a la ultima columna de cara superior
            self.cubo[0][:, 2] = self.cubo[3][:,2]  # mueve la ultima columna de cara inferior (A) a la ultima columna de cara frontal
            self.cubo[3][:, 2] = self.cubo[1][:, 0][::-1]  # mueve la primera columna de cara posterior (N) a la ultima columna de cara inferior
            self.cubo[1][:, 0] = temp[::-1]  # mueve fila guardada a la primera columna de la cara porterior

    # MOVER CARA VERDE
    def moverV(self, direccion):
        if direccion.upper() == 'H':
            self.horarioV()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioV()

    def horarioV(self):
        self.cubo[4] = np.rot90(self.cubo[4], -1)  # gira cara posterior (Naranja)
        temp = np.copy(self.cubo[2][:, 0])  # guarda la primera columna de la cara superior (Blanco)
        self.cubo[2][:,0] = self.cubo[1][:,2][::-1]  # mueve columna 3 de cara posterior a la primera columna de cara superior
        self.cubo[1][:, 2] = self.cubo[3][:, 0][::-1]  #mueve la primera columna de cara inferior a la tercera columna de la cara posterior
        self.cubo[3][:, 0] = self.cubo[0][:,0]  # mueve la primera columna de cara frontal a la primera columna de cara inferior
        self.cubo[0][:, 0] = temp  # mueve fila guardada a columna izquierda de cara izquierda


    def imprimirCubo(self):
        self.mostrarMatriz(self.cubo[2])
        self.mostrarMatrizCaras(self.cubo[0], self.cubo[5], self.cubo[1], self.cubo[4])
        self.mostrarMatriz(self.cubo[3])


    def mostrarMatriz(self, matriz):
        fil = len(matriz)  # saber cuantas filas
        col = len(matriz[0])  # saber cuantas columnas
        for i in range(0, fil):
            for j in range(0, col):
                print(matriz[i][j], end="  ")
            print(end="|")
            print()


    def mostrarMatrizCaras(self, matriz1, matriz2, matriz3, matriz4):
        fil = len(matriz1)  # saber cuantas filas
        col = len(matriz1[0])  # saber cuantas columnas
        for i in range(0, fil):
            for j in range(0, col):
                print(matriz1[i][j], end="  ")
            print(end="|  ")
            for j in range(0, col):
                print(matriz2[i][j], end="  ")
            print(end="|  ")
            for j in range(0, col):
                print(matriz3[i][j], end="  ")
            print(end="|  ")
            for j in range(0, col):
                print(matriz4[i][j], end="  ")
            print(end="|  ")
            print()


def menu_sentido(rubik, cara):
    print("1. Sentido Horario")
    print("2. Sentido Antihorario")
    print("3. Regresar")
    opcion = int(input("Ingrese una opción (1 o 2): "))

    if opcion == 1:
        sentido = 'H'
        rubik.rotar(cara, sentido)
        os.system('cls')
    elif opcion == 2:
        sentido = 'AH'
        rubik.rotar(cara, sentido)
        os.system('cls')
    elif opcion == 3:
        print("Regresando al menú rotaciones")
        os.system('cls')
    else:
        os.system('cls')
        print("Opción no válida")


def menu_rotar(rubik):
    while True:
        rubik.imprimirCubo()
        print("--------Menú Rotaciones------------")
        print("1. Rotar cara frontal")
        print("2. Rotar cara posterior")
        print("3. Rotar cara superior")
        print("4. Rotar cara inferior")
        print("5. Rotar cara izquierda")
        print("6. Rotar cara derecha")
        print("7. Salir")
        opcion = int(input("Ingrese una opción (del 1 al 7): "))

        if opcion == 1:
            print("Rotar cara frontal: ")
            menu_sentido(rubik, 'R')
        elif opcion == 2:
            print("Rotar cara posterior: ")
            menu_sentido(rubik, 'N')
        elif opcion == 3:
            print("Rotar cara superior: ")
            menu_sentido(rubik, 'B')
        elif opcion == 4:
            print("Rotar cara inferior: ")
            menu_sentido(rubik, 'A')
        elif opcion == 5:
            print("Rotar cara izquierda: ")
            menu_sentido(rubik, 'V')
        elif opcion == 6:
            print("Rotar cara derecha: ")
            menu_sentido(rubik, 'X')
        elif opcion == 7:
            print("Saliendo...")
            break
        else:
            os.system('cls')
            print("Opción no válida")


def main():
    rubik = CuboRubik()

    while True:
        os.system('cls')
        print("--------CUBO RUBIK--------")
        rubik.imprimirCubo()
        print("Numero de combinaciones realizadas: ", rubik.numCombinacionesRealizadas)
        print("Combinaciones Realizadas: ", rubik.combinacionesRealizadas)
        print()
        print("Menu de Opciones")
        print("1. Rotar una cara.")
        print("2. Desordenar aleatoriamente.")
        print("3. Realizar n movimientos aleatorios.")
        print("4. Armar CuboRubik.")
        print("5. Salir.")

        opcion = int(input("Ingrese una opción (del 1 al 4): "))
        if opcion == 1:
            os.system('cls')
            menu_rotar(rubik)
            print()
        elif opcion == 2:
            os.system("cls")
            rubik.desordenar()
        elif opcion == 3:
            os.system("cls")
            numMovimientos = 0
            while numMovimientos < 1:
                numMovimientos = int(
                    input("Ingrese el número de movimientos aleatorios que desea realizar (entero positivo): "))
            rubik.movimientosAleatorios(numMovimientos)
        elif opcion == 4:
            rubik.armar()
        elif opcion == 5:
            pass
        else:
            print('Error, opción inválida')
            os.system('pause')


if __name__ == "__main__":
    main()


