class z :
    def __init__(self,z1,z2) :
        self.z1 = int(z1)
        self.z2 = int(z2)
        self.j  = int(self.z1*self.z2)
        self.v  = str(self)
    
    def __str__ (self):
        return "%sx%s"%(self.z1,self.z2)
    
    def b (self,a):
        return a == self.j


class list(list):
    def co (self):
        c = []
        for q in self :
            c.append(q)
        return list(c)

    def g (self,a:int):
        r = self[a]
        del self[a]
        return r


    def rand(self):
        from random import randint as ran
        l = []
        la = self.co()
        for q in range(0,len(self)) :
            b = ran(0,len(la)-1)
            l.append(la.g(b))
        return l


def c (a):
    if a == 'a':
        l = list()
        for q in range(0,11):
            for qq in range(0,q+1):
                l.append(z(q,qq))
    else:
        l = list()
        for q in range(0,11):
            l.append(z(a,q))
    return l.rand()



while True:
    try:

        i = c(input ('''
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10 
        a
        '''))









        for q in i:
            try:
                i = int(input('%s= '%q.v))
            except: ...
            while not q.b(i):
                try:
                    i = int(input('%s= '%q.v))
                except:
                    continue
            print ('ok!\n')
        print('True.......\n\n\n')
    except:
        continue










