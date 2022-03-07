from random import randrange

def display_board(tablero):
	'''
	Funcion para pintar el tablero
	'''
	print("+-------" * 3,"+",sep="")
	for fila in range(3):
		print("|       " * 3,"|",sep="")
		for columna in range(3):
			print("|   " + str(tablero[fila][columna]) + "   ",end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")
	
def enter_move(tablero):
	'''
	Funcion para introducir los movimientos del jugador
	'''
	ok = False	
	while not ok:
		movimiento = input("Introduzca su movimiento: ") 
		ok = len(movimiento) == 1 and movimiento >= '1' and movimiento <= '9'
		if not ok:
			print("Movimiento invalido, introduzcalo otra vez por favor ")
			continue
		movimiento = int(movimiento) - 1 	# El -1 es porque las celdas van de 1 a 9, pero en la lista no.
		fila = movimiento//3 	
		columna = movimiento%3		
		simbolo = tablero[fila][columna]	
		ok = simbolo not in ['O','X'] 
		if not ok:	
			print("La casilla esta ocupada, intentalo otra vez ")
			continue
	tablero[fila][columna] = 'O' 

def make_list_of_free_fields(tablero):
    '''
    Funcion para calcular las casillas vacias
    '''
	lista_campos_vacios = []	
	for fila in range(3): 
		for columna in range(3): 
			if tablero[fila][columna] not in ['O','X']: 
				lista_campos_vacios.append((fila,columna)) 
	return lista_campos_vacios


def victory_for(tablero,simbolo):
    '''
    Funcion para asignar quien es el ganador de la partida
    '''
	if simbolo == "X":	
		ganador = 'yo'	
	elif simbolo == "O": 
		ganador = 'tu'	
	else:
		ganador = None	
	diagonal1 = diagonal2 = True  
	for rc in range(3):
		if tablero[rc][0] == simbolo and tablero[rc][1] == simbolo and tablero[rc][2] == simbolo:
			return ganador
		if tablero[0][rc] == simbolo and tablero[1][rc] == simbolo and tablero[2][rc] == simbolo: 
			return ganador
		if tablero[rc][rc] != simbolo:
			diagonal1 = False
		if tablero[2 - rc][2 - rc] != simbolo: 
			diagonal2 = False
	if diagonal1 or diagonal2:
		return ganador
	return None

def draw_move(tablero):
    '''
    Funcion para pintar el movimiento en el tablero
    '''
	lista_campos_vacios = make_list_of_free_fields(tablero)
	cnt = len(lista_campos_vacios)
	if cnt > 0:	
		this = randrange(cnt)
		fila, columna = lista_campos_vacios[this]
		tablero[fila][columna] = 'X'

tablero = [[3 * j + i + 1 for i in range(3)] for j in range(3)] 
print("Vamos a jugar al 3 en raya!!!")
tablero[1][1] = 'X' #Empieza la maquina jugando en el centro del tablero
lista_campos_vacios = make_list_of_free_fields(tablero)
turno_jugador = True
while len(lista_campos_vacios):
		display_board(tablero)
		if turno_jugador:
			enter_move(tablero)
			vencedor = victory_for(tablero,'O')    
		else:
			draw_move(tablero)
			vencedor = victory_for(tablero,'X')
		if vencedor != None:
			break
		turno_jugador = not turno_jugador
		lista_campos_vacios = make_list_of_free_fields(tablero)
display_board(tablero)
if vencedor == 'tu':
	print("Enhorabuena, me ganaste ;( ")
elif vencedor == 'yo':
	print("Esta vez te gane yo, intentalo de nuevo:D ")
else:
	print("Ha habido empate, ninguno ha ganado!")
