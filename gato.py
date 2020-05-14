"""
Simple implementacion del juego de Gato
en linea de comando para dos jugadores humanos

Autor: Julio Arriaga
"""

def crear_tablero():
    """Crea el tablero inicial de 3x3, conteniendo '-' en cada casilla (casilla disponible)"""
    tablero = []
    for i in range(3):
        tablero.append(['-'] * 3)
    return tablero

def marcar_casilla(ren, col, tablero, simbolo):
    """Marca la casilla en el renglon ren, columna col del tablero con el simbolo dado"""
    if tablero[ren][col] == '-':
        tablero[ren][col] = simbolo

def imprimir_tablero(tablero):
    """Imprime el tablero"""
    print(' ', 0, 1, 2, sep='\t')
    for i in range(len(tablero)):
        print(i, end='\t')
        for j in tablero[i]:
            print(j, end='\t')
        print()

def ganador(tablero):
    """Revisa el tablero para determinar si esta en condicion de triunfo (existen 3 simbolos iguales en linea)"""
    for i in range(len(tablero)):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != '-':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != '-':
            return True
    if tablero[1][1] != '-' and (tablero[0][0] == tablero[1][1] == tablero[2][2] or
                                 tablero[2][0] == tablero[1][1] == tablero[0][2]):
        return True
    return False

def lleno(tablero):
    """Revisa el tablero para determinar si aun existen espacios disponibles"""
    for ren in tablero:
        for casilla in ren:
            if casilla == '-':
                return False
    return True

def juego():
    """Loop principal del juego"""
    turno = 0
    simbolo = ['X', 'O']
    tablero = crear_tablero()
    imprimir_tablero(tablero)
    while True:
        print(f'Jugador {turno+1}:')
        ren = int(input('Renglon: '))
        col = int(input('Columna: '))
        marcar_casilla(ren, col, tablero, simbolo[turno])
        imprimir_tablero(tablero)
        if ganador(tablero):
            print(f'Felicidades Jugador {turno+1}!')
            break
        if lleno(tablero):
            print('Gana el gato, todos pierden')
            break
        turno = (turno + 1) % 2

juego()
