import socket, random
from threading import Thread
    

class Server:
    IP = "127.0.0.1"
    PORT = 12345
    CLIENTS = {}
    
    def __init__(self):
        self.start = False
        #Indica la familia, inet es IPv4 y sock_steam es TCP, DGRAM para UDP
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Para comenzar el socket y poder terminarlo
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('Socket created')
        self.soc.bind((self.IP, self.PORT))
        print('Socket bind complete')
        self.soc.listen(10)
        print('socket now listening')
        #inicia espera de juego
        self.listening_client()

    def listening_client(self):
        while True:
            if not self.start and len(self.CLIENTS.keys()) < 2:
                conn, addr = self.soc.accept()
                ip, port = str(addr[0]), str(addr[1])
                print('Accepting connection from %s' % ip)
                self.new_client(conn, ip, port)
            elif not self.start:
                self.start = True
                Thread(target=Game, args=(self.CLIENTS, self.soc)).start()
        self.soc.close()
                           

    def new_client(self, conn, ip, port):
        num_players = len(self.CLIENTS.keys())
        self.CLIENTS['O' if 'X' in self.CLIENTS else 'X'] = (conn, ip, port)
        conn.send("Conexion a 3 en raya".encode())
        conn.send("Esperando otro jugador".encode())        
        


class Game(object):

    tablero = { 0: ' ', 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ' }
    
    def __init__(self, clients, soc):
        self.clients = clients
        self.turn = random.choice(clients.keys())
        self.player_x_conn, player_x_ip = self.getPlayerInfo('X')
        self.player_o_conn, player_o_ip = self.getPlayerInfo('O')
        msg = "\tEmpieza el juego\n------------------------------------\n\t%s(Ficha 'X') Vs %s(Ficha 'O')\n\nEmpieza las '%s'" % (player_x_ip, player_o_ip, self.turn)
        self.soc = soc
        self.sendAll(msg.encode())
        self.imprime_tablero(self.player_x_conn if self.turn == 'X' else self.player_o_conn)
        self.start()

    def sendAll(self, msg):
        self.player_x_conn.send(msg.encode())
        self.player_o_conn.send(msg.encode())

    def getPlayer(self, token):
        return self.clients[token]
    
    def getPlayerInfo(self, token):
        info = self.getPlayer(token)
        return info[0], info[1]

    def imprime_tablero(self, conn):
        conn.send('%s|%s|%s\n-+-+-\n%s|%s|%s\n-+-+-\n%s|%s|%s\n'.encode() % (self.tablero[0], self.tablero[1], self.tablero[2], self.tablero[3], self.tablero[4], self.tablero[5], self.tablero[6], self.tablero[7], self.tablero[8]))
                               
    def comprueba_resultado(self):
        if self.turn == self.tablero[0] == self.tablero[1] == self.tablero[2]:
            return True
        if self.turn == self.tablero[3] == self.tablero[4] == self.tablero[5]:
            return True
        if self.turn == self.tablero[6] == self.tablero[7] == self.tablero[8]:
            return True
        if self.turn == self.tablero[0] == self.tablero[3] == self.tablero[6]:
            return True
        if self.turn == self.tablero[1] == self.tablero[4] == self.tablero[7]:
            return True
        if self.turn == self.tablero[2] == self.tablero[5] == self.tablero[8]:
            return True
        if self.turn == self.tablero[0] == self.tablero[4] == self.tablero[8]:
            return True
        if self.turn == self.tablero[2] == self.tablero[4] == self.tablero[6]:
            return True

    def start(self):
        num_turn = 0
        while True:
            player_conn = self.player_x_conn if self.turn == 'X' else self.player_o_conn
            player_conn.send("\put Proximo movimiento (0-8)".encode())
            movimiento = player_conn.recv(4096).decode()
            if movimiento.isdigit() and  -1 < int(movimiento) < 9 and self.tablero[int(movimiento)] == ' ':
                self.tablero[int(movimiento)] = self.turn
                self.imprime_tablero(self.player_x_conn)
                self.imprime_tablero(self.player_o_conn)
                if num_turn >3 and self.comprueba_resultado():
                    self.player_conn.send("Enhorabuena, %s eres el ganador!".encode() % (self.turn))
                    if self.turn == 'X':
                        self.player_o_conn.send("Has perdido, 'O', eres un gran perdedor".encode())
                    else:
                        self.player_x_conn.send("Has perdido, 'X', eres un gran perdedor".encode())
                    break
                if num_turn == 8:
                    self.sendAll("Empate!!!!")
                    break
                self.turn = 'O' if self.turn == 'X' else 'X'
                self.sendAll("Turno de '%s'".encode() % self.turn)
                num_turn += 1
            
        
server = Server()
    
