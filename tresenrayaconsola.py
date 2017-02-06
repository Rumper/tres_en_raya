#! /usr/bin/env python3
# Uso: 

from random import choice

class partida(object):

    tablero = { 0: ' ', 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ' }
    
    def __init__(self):
        self.turno = choice(['X', 'O'])
        print('El juego ha comenzado es el turno de %s' % (self.turno))
        self.imprime_tablero()
        print('Donde quieres mover?')
        self.run()
        

    def imprime_tablero(self):
        print('%s|%s|%s' % (self.tablero[0], self.tablero[1], self.tablero[2]))
        print('-+-+-')
        print('%s|%s|%s' % (self.tablero[3], self.tablero[4], self.tablero[5]))
        print('-+-+-')
        print('%s|%s|%s' % (self.tablero[6], self.tablero[7], self.tablero[8]))

#    def comprueba_resultado(self):
#        for i in range(3):
#            if((self.tablero[(i * 3)] == self.tablero[(i * 3) + 1]) & (self.tablero[(i * 3)] == self.tablero[(i * 3) + 2])):
#                existeGanador = True
#            elif((self.tablero[i] == self.tablero[i + 3]) & (self.tablero[i] == self.tablero[i + 6])):
#                existeGanador = True
#        
#        if((self.tablero[0] == self.tablero[4]) & (self.tablero[0] == self.tablero[8])):
#            existeGanador = True
#        elif((self.tablero[2] == self.tablero[4]) & (self.tablero[2] == self.tablero[6])):
#            existeGanador = True
#
#        return existeGanador

    def comprueba_resultado(self):
        if self.turno == self.tablero[0] == self.tablero[1] == self.tablero[2]:
            return True
        if self.turno == self.tablero[3] == self.tablero[4] == self.tablero[5]:
            return True
        if self.turno == self.tablero[6] == self.tablero[7] == self.tablero[8]:
            return True
        if self.turno == self.tablero[0] == self.tablero[3] == self.tablero[6]:
            return True
        if self.turno == self.tablero[1] == self.tablero[4] == self.tablero[7]:
            return True
        if self.turno == self.tablero[2] == self.tablero[5] == self.tablero[8]:
            return True
        if self.turno == self.tablero[0] == self.tablero[4] == self.tablero[8]:
            return True
        if self.turno == self.tablero[2] == self.tablero[4] == self.tablero[6]:
            return True

    def run(self):
        for i in range(9):

            while True:
                print("Proximo movimiento (0-8)")
                movimiento = input()
                if movimiento.isdigit() and  -1 < int(movimiento) < 9 and self.tablero[int(movimiento)] == ' ':
                   self.tablero[int(movimiento)] = self.turno
                   break

            self.imprime_tablero()
            
            if(i > 3):
                if(self.comprueba_resultado()):
                    print('Enhorabuena, %s eres el ganador!' % (self.turno))
                    break

            if(self.turno == 'X'):
                self.turno = 'O'
            else:
                self.turno = 'X'

            print('Es el turno de %s, a donde mueves?' % (self.turno))

partida()
