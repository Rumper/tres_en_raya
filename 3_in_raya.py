
import random

class Game(object):
    TABLERO = {}
    MAX_POSITION = 9
    VECINOS = {
                0: [(1,2), (4,8), (5,6)], 
                1: [(0,2), (4,7)],
                2: [(0,1), (3,8), (4,6)],
                3: [(2,8), (4,5)],
                4: [(0,8), (1,7), (2,6), (3,5)],
                5: [(0,6), (3,4)],
                6: [(0,5), (2,4), (7,8)],
                7: [(1,4), (6,8)],
                8: [(0,4), (2,3), (6,7)]
              }
    
    def __init__(self):
        print "Inicializando partida, Gracias por escoger el juego en 3 en raya de IEE\n\n"
        self.start_new_game()
        print "\n\nJuego finalizado, gracias por jugar Al 3 en raya de IEEE"
                        
    def game_start(self):
        self.turn_xo = random.choice(['X', 'O'])
        self.show_turn()
        while True:
            self.print_table(True)
            position = raw_input ("Seleccione lugar disponible\n")
            if position.isdigit() and  -1 < int(position) < self.MAX_POSITION and int(position) not in self.TABLERO:
                if self.check_game(int(position)):
                    break
                
	if self.empate: print "Empate\n"
	else: print "Ha ganado el jugador %s \n" % self.turn_xo
	
        while True:
            input = raw_input("Quiere volver a jugar? S/N\n")
            if input.lower() == "s":
                self.new_game = True
                break
            elif input.lower() == "n":
                break
		
        if self.new_game:
            self.start_new_game()

    def start_new_game(self):
        self.new_game = False
        self.empate = False
        self.turno = 0
        self.TABLERO = {}
        self.game_start()
	
    def show_position(self, number, is_show):
        if number in self.TABLERO:
            return self.TABLERO[number]
        else:
            return str(number) if is_show else ' '
			
    def print_table(self, is_show=False):
        print('   |   |')
        print(' ' + self.show_position(0,is_show) + ' | ' + self.show_position(1,is_show) + ' | ' + self.show_position(2,is_show))
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.show_position(5,is_show) + ' | ' + self.show_position(4,is_show) + ' | ' + self.show_position(3,is_show))
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.show_position(6,is_show) + ' | ' + self.show_position(7,is_show) + ' | ' + self.show_position(8,is_show))
        print('   |   |\n')
			
					
    def show_turn(self):
        print "Turno de %s\n" % self.turn_xo
	
    def check_game(self, position):
        is_finish = False
        self.TABLERO[position] = self.turn_xo
        self.print_table()
        
        if self.turno >= 4 :
            is_finish = self.is_winner(position)
        if not is_finish:
            self.turn_xo = 'O' if self.turn_xo is 'X' else 'X'
            self.show_turn()
        self.turno +=1
        return is_finish			

    def is_winner(self, position):
        for index0, index1 in self.VECINOS[position]:
            if index0 in self.TABLERO and index1 in self.TABLERO and self.turn_xo == self.TABLERO[index0] == self.TABLERO[index1]:
                return True
        if self.turno == 8:
            self.empate = True
            return True

Game()				
								
