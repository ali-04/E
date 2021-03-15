import ctypes
from time import sleep
from playsound import playsound as p
from os import getcwd as l
from platform import system as si



def fos ():
    ba = {'Windows':'\\','Linux':r'/'}
    b = ba[si()]
    return b



global time ,wtime , lo ,S
time = 20 
wtime = time *60
S = fos()
lo = 'E'+S+'e7'+S+'1.mp3'


def sl():
    p(l()+S+lo)
    ctypes.windll.user32.MessageBoxW(0, "it'sleep time", 'alarm', 1)
    

while True :
    sleep (wtime)
    sl()



