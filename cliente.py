import socket

class Client:

    def __init__(self):
        self.ip = raw_input('IP: ')
        self.port = raw_input('PORT: ')
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.soc.connect((self.ip, int(self.port)))
        self.run()

    def run(self):
        while True:
            msg = self.soc.recv(4096).decode()
            if '\put' in msg:
                entrada = True
                msg = msg.split('\put ')[1]
            else:
                entrada = False
            print(msg)
            if entrada:
                data = raw_input()
                self.soc.send(data.encode())


client = Client()
