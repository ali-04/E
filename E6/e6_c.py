from os import getcwd
from csv import reader
from time import sleep
from re import search
import socket
from platform import system as si


def fos ():
    ba = {'Windows':'\\','Linux':r'/'}
    b = ba[si()]
    return b


def gsc():
    return input('>>> ')




class connection :
    def __init__(self,name,port=8546):
        self.name = name
        if search(r"/d+/./d+/./d+/./d+",name) == None:
            self.ip = socket.gethostbyname(name)
        else: self.ip = name

        self.port = port


    def send(self,msg):
        s = socket.socket()
        s.connect((self.ip, self.port))
        s.send(msg.encode())
        print(s.recv(1024).decode())
        s.close()
        del s


    def trytoc (self):
        try:
            s = socket.socket()
            s.connect((self.ip, self.port))
            s.send('///test'.encode())
            if s.recv(1024).decode() == 'ok!':
                ret = True 
            else : ret = False
        except: ret = False

        try : 
            s.close()
            del s 
        except : ...
        return ret



    def start (self):
        if self.trytoc():
            ms = gsc()
            while ms != '^Dis':
                self.send(ms)
                ms = gsc()
        else: print('ops!')



    def __str__(self):
        return '%s:%i  ==   %s' %(self.ip,self.port,self.name)





global dbloc ,file
dbloc = getcwd()
file  = 'WindowsNT.dle'



def fl(): return dbloc + fos() + file


def get (n,p):
    try:
        with open (dbloc + fos() + file,'r') as f:
            F = f.read()
            f.close()
            with open (fl(),'w') as f:
                f.write(F+'\n'+'%s,%s'%(n,p))
                f.close()
                sleep(1)
    except:
        with open (fl(),'w') as f: 
            f.close()
            sleep(1)
            with open (fl(),'w') as f:
                f.write('%s,%s'%(n,p))
                f.close()
                sleep(1)



def giv ():

    global _cash ,__cash

    _cash = []
    __cash = {}

    try :


        with open(fl() , 'r') as f:
            F = list(reader(f))
            for q in F :
                try:
                    cc = connection(q[0])
                    try:
                        cc.port = int(q[1])
                    except:...
                except:cc = None
                if cc != None: 
                    _cash.append(cc)
                    __cash[cc.name] = cc
    except:...



giv()





pr0 = '''
ip        : port        ==  name
____________________________________________
'''
pr1 = '''
____________________________________________
'''

def join (l):
    r = 0
    y = ''
    for q in l:
        y += '%i) %s                  |'%(r,str(q))
    return y


global g

b = lambda x : g == x

while True :
    g = input('<>> ')
    if b('/list'):
        
        print (pr0)
        print (join(_cash))
        print (pr1)
    
    if b('/c'):
        try:
            _cash[int(input('^>> '))].start()
        except:...
    

    if b('/add'):
        try:
            n = input('name>> ')
            p = input('port>> ')
            if p == '': p = 8546
            else : p = int(p)
            get(n,p)
            giv()
            print('added')
        except:...









        

