import turtle, time

print("==============BIENVENIDO A Flow Free Automatizado==============")
print("A continuación por favor elija uno de los 3 tableros de prueba establecidos.")
print("1. Tablero 8x7 con colores posicionados únicamente en la primera y ultima fila.")
print("2. Tablero 5x5")
print("3. Tablero 7x7.")
print("4. Tablero 5x5.")
valid = False

while valid==False:
    try:
        opcion = int(input("Ingresar opcion: "))
    except:
        print("Por favor ingresar digitos y no letras, el digito debe indicar el tablero a jugar\n")
    else:
        if isinstance(opcion, int) and opcion > 0 and opcion <= 4:
            print(f"Tablero {opcion} elegido!")
            print("Por favor abrir la ventana generada de Python Turtle Graphics ")
            valid = True
        else:
            print("Por favor ingresar una opcion de las indicadas posibles\n")

if opcion == 1:
    VELOCIDAD = 1
    tablero = []
    tablero = [[1, 1, 1, 1, 1, 1, 1, 1, 1]]
    tablero.append([1, 2, 3, 4, 5, 6, 7, 8, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 2, 3, 4, 5, 6, 7, 8, 1])
    tablero.append([1, 1, 1, 1, 1, 1, 1, 1, 1])
elif opcion == 2:
    VELOCIDAD = 1
    tablero = []
    tablero = [[1, 1, 1, 1, 1, 1, 1]]
    tablero.append([1, 0, 0, 0, 0, 4, 1])
    tablero.append([1, 0, 3, 0, 2, 0, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 2, 0, 4, 3, 0, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 1, 1, 1, 1, 1, 1])
elif opcion == 3:
    VELOCIDAD = 1
    tablero = []
    tablero = [[1, 1, 1, 1, 1, 1, 1, 1, 1]]
    tablero.append([1, 2, 0, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 3, 7, 8, 0, 0, 0, 0, 1])
    tablero.append([1, 0, 0, 0, 0, 4, 0, 0, 1])
    tablero.append([1, 3, 0, 0, 0, 0, 8, 0, 1])
    tablero.append([1, 4, 0, 5, 0, 0, 7, 0, 1])
    tablero.append([1, 2, 5, 0, 6, 0, 6, 0, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 1, 1, 1, 1, 1, 1, 1, 1])

elif opcion == 4:
    VELOCIDAD = 0
    tablero = []
    tablero = [[1, 1, 1, 1, 1, 1, 1]]
    tablero.append([1, 2, 0, 3, 0, 6, 1])
    tablero.append([1, 0, 0, 4, 0, 5, 1])
    tablero.append([1, 0, 0, 0, 0, 0, 1])
    tablero.append([1, 0, 3, 0, 6, 0, 1])
    tablero.append([1, 0, 2, 4, 5, 0, 1])
    tablero.append([1, 1, 1, 1, 1, 1, 1])

#Inicializamos parametros de Turtle
turtle.tracer(0)
turtle.speed(0)
turtle.hideturtle()
screen = turtle.Screen()
screen.bgcolor("#444444")
turtle.color("#222222")

topeIzquierdo_x = -150
topeIzquierdo_y = 150

#Colores para identificar los puntos y lineas
colores = ["#222222", "#000000", "red", "yellow", "blue", "green", "orange", "magenta", "purple", "bfilan", "darkgreen"]
colores_de_puntos = ["#222222", "#000000", "darkred", "orange", "darkblue", "darkgreen", "red", "purple", "magenta",
              "chocolate", "green"]

# Workout the size of the tablero
FILAS = len(tablero)
COLUMNAS = len(tablero[0])

nodosIniciales = {}
nodosFinales = {}
allNodes = []
distancias = {}

#Inicialmente empezamos por identificar los colores o nodos tanto iniciales como finales, esto con el fin de entender cuales debemos conectar
for fila in range(1, FILAS - 1):
    for columnas in range(1, COLUMNAS - 1):
        color = tablero[fila][columnas]
        if color > 0:
            if color in nodosIniciales:
                nodosFinales[color] = [fila, columnas]
                distancias[color] = abs(fila - nodosIniciales[color][0]) + abs(columnas - nodosIniciales[color][1])
            else:
                nodosIniciales[color] = [fila, columnas]
            allNodes.append([fila, columnas, color])

# Ordenamos los nodos basados en la distancia de Manhattan.
#La idea es conectar nodos que estan cercanos unos de otros

nodosOrdenados = []
keys = list(distancias)
for i in range(0, len(distancias)):
    min = distancias[keys[0]]
    for key in distancias:
        if distancias[key] < min:
            min = distancias[key]
            minKey = key
    nodosOrdenados.append(key)
    distancias.pop(key)


# Los nodos almacenados en "nodosOrdenados" estan ordenados basado en la distancia de Manhattan entre ellos
# Esta es un funcion que mediante Python Turtle permitira graficar el tablero en 2D en donde se vera el juego.

def drawtablero(ancho):

    global FILAS, COLUMNAS
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(topeIzquierdo_x, topeIzquierdo_y - ancho)

    for fila in range(1, FILAS - 1):
        for columnas in range(1, COLUMNAS - 1):
            cuadrado(ancho, tablero[fila][columnas])
            turtle.forward(ancho)
        turtle.setheading(270)
        turtle.forward(ancho)
        turtle.setheading(180)
        turtle.forward(ancho * (COLUMNAS - 2))
        turtle.setheading(0)

    # Add Starting and Ending Nodes to the tablero...
    for nodo in allNodes:
        turtle.setheading(0)
        turtle.goto(topeIzquierdo_x + nodo[1] * ancho - ancho // 2, topeIzquierdo_y - nodo[0] * ancho + ancho // 4)
        turtle.fillcolor(colores_de_puntos[nodo[2]])
        turtle.begin_fill()
        turtle.circle(ancho // 4)
        turtle.end_fill()

# La funcion cuadrado permite dibujar una caja al construir cada lado del cuadrado.
def cuadrado(ancho, index):
    turtle.fillcolor(colores[index])
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(ancho)
        turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)


# Permite revisar si el tablero es valido
def validartablero(tablero):
    global FILAS, COLUMNAS
    for fila in range(1, FILAS - 1):
        for columnas in range(1, COLUMNAS - 1):
            if tablero[fila][columnas] > 0:
                color = tablero[fila][columnas]

                if tablero[fila + 1][columnas] > 0 and tablero[fila + 1][columnas] != color:
                    if tablero[fila - 1][columnas] > 0 and tablero[fila - 1][columnas] != color:
                        if tablero[fila][columnas + 1] > 0 and tablero[fila][columnas + 1] != color:
                            if tablero[fila][columnas - 1] > 0 and tablero[fila][columnas - 1] != color:
                                return False
                if tablero[fila + 1][columnas] == color and tablero[fila - 1][columnas] == color and tablero[fila][columnas + 1] == color:
                    return False
                elif tablero[fila + 1][columnas] == color and tablero[fila - 1][columnas] == color and tablero[fila][
                    columnas - 1] == color:
                    return False
                elif tablero[fila + 1][columnas] == color and tablero[fila][columnas + 1] == color and tablero[fila][
                    columnas - 1] == color:
                    return False
                elif tablero[fila - 1][columnas] == color and tablero[fila][columnas + 1] == color and tablero[fila][
                    columnas - 1] == color:
                    return False
    return True


#Una funcion que simplemente indica si el tablero ha sido resulto
def resuelto(tablero):
    global FILAS, COLUMNAS
    for fila in range(1, FILAS - 1):
        for columnas in range(1, COLUMNAS - 1):
            if tablero[fila][columnas] == 0:
                return False
    return True

def abs(a, b):
    if a > b:
        return a - b
    else:
        return b - a


# Esta es una funcion de backtracking que tiene el fin de revisar todos los movimientos posibles y descartar tableros que no llevan
# a una solucion posible.

def resolverTablero(tablero):
    drawtablero(30)
    turtle.getscreen().update()
    time.sleep(1 - VELOCIDAD)

    if validartablero(tablero) == False:
        return False

    # Se revisa si el tablero esta completamente resuelto
    if resuelto(tablero):
        return True

    # De lo contrario se revisa el siguiente movimiento
    for color in nodosOrdenados:
        startNode = nodosIniciales[color]
        endNode = nodosFinales[color]

        # Se revisa si los puntos de este color ya fueron conectados
        if (abs(endNode[0], startNode[0]) + abs(endNode[1], startNode[1]) > 1):
            # Si no, se revisa en cual direccion seguir.
            direcciones = []
            if tablero[startNode[0]][startNode[1] + 1] == 0:
                if endNode[1] > startNode[1]:
                    direcciones.insert(0, "derecha")  # Prioridad Alta
                else:
                    direcciones.append("derecha")  # Prioridad Baja!
            if tablero[startNode[0]][startNode[1] - 1] == 0:
                if endNode[1] < startNode[1]:
                    direcciones.insert(0, "izquierda")  # Prioridad Alta
                else:
                    direcciones.append("izquierda")  # Prioridad Baja!
            if tablero[startNode[0] + 1][startNode[1]] == 0:
                if endNode[0] > startNode[0]:
                    direcciones.insert(0, "abajo")  # Prioridad Alta
                else:
                    direcciones.append("abajo")  # Prioridad Baja!
            if tablero[startNode[0] - 1][startNode[1]] == 0:
                if endNode[0] < startNode[0]:
                    direcciones.insert(0, "arriba")  # Prioridad Alta
                else:
                    direcciones.append("arriba")  # Prioridad Baja!

            if len(direcciones) == 0:
                return False

            for direccion in direcciones:
                if direccion == "derecha":
                    startNode[1] += 1
                    tablero[startNode[0]][startNode[1]] = color
                    if resolverTablero(tablero) == True:
                        return True
                    else:
                        # Backtracking
                        tablero[startNode[0]][startNode[1]] = 0
                        startNode[1] -= 1

                elif direccion == "izquierda":
                    startNode[1] -= 1
                    tablero[startNode[0]][startNode[1]] = color
                    if resolverTablero(tablero) == True:
                        return True
                    else:
                        # Backtracking
                        tablero[startNode[0]][startNode[1]] = 0
                        startNode[1] += 1
                elif direccion == "arriba":
                    startNode[0] -= 1
                    tablero[startNode[0]][startNode[1]] = color
                    if resolverTablero(tablero) == True:
                        return True
                    else:
                        # Backtracking
                        tablero[startNode[0]][startNode[1]] = 0
                        startNode[0] += 1
                elif direccion == "abajo":
                    startNode[0] += 1
                    tablero[startNode[0]][startNode[1]] = color
                    if resolverTablero(tablero) == True:
                        return True
                    else:
                        # Backtracking
                        tablero[startNode[0]][startNode[1]] = 0
                        startNode[0] -= 1
            return False


drawtablero(30)
turtle.getscreen().update()
time.sleep(3)

if resolverTablero(tablero):
    print("=====El tablero ha sido resuelto=====")
else:
    print("=====El tablero no pudo ser resuelto :( =====")
