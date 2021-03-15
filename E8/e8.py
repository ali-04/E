from datetime import date
from time import sleep
from csv import reader
from sys import argv



def fos ():
    from platform import system as si
    ba = {'Windows':'\\','Linux':r'/'}
    b = ba[si()]
    return b

S = fos()

global tlis , clis , dlis ,file
tlis , clis ,dlis = {} , {} ,{0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
file=str(S.join(argv[-1].split(S)[:-1]))+'data.d'









class tm :
    def __init__ (self,h=0,m=0,st='00:00'):
        if  st != '00:00:0' and d==0 and h==0 and m==0 :         
            self.h = st.split(':')[0]
            self.m = st.split(':')[1]
        else:
            self.h = str(h)
            self.m = str(m)
            

    
    
    def __str__  (self):
        return '%s:%s'%(self.h,self.m)

    

    def now():
        from datetime import now
        return tm(h=now().hour ,m=now().minute)

    def __le__(self,other):
        i = self
        o = other
        if i.h > o.h :
            return True
        elif i.h == o.h:
            if i.m > o.m:
                return True
            elif i.m == o.m:
                return False
            else: return False
        else: return False

    def __lt__(self,other):
        i = self
        o = other
        if i.h > o.h :
            return True
        elif i.h == o.h:
            if i.m > o.m:
                return True
            elif i.m == o.m:
                return True
            else: return False
        else: return False

    def __sub__(self,other):
        sm = int(self.m)
        sh = int(self.h)
        om = int(other.m)
        oh = int(other.h)

        nm = sm-om
        if nm<0 :
            sh -= 1
            nm += 60
        
        nh = sh-oh

        if nh<0: nh += 24

        return tm(h=nh ,m=nm)






def sync():
    try: open(file,'r').close()
    except: 
        open(file,'w+').close()
        sleep(0.5)
    
    with open(file,'r') as F:
        r = reader(F.read())
        for q in r :
            try: Class(q[0],q[1],q[2],tm(st=q[3]),tm(st=q[4]),q[5])
            except: ...











class Class :
    def __init__ (self,name,ostad,link,day,stime,etime):
        self.etim = etime
        self.stim = stime
        self.ostad= ostad
        self.name = name
        self.link = link
        self.day  = day
        tlis[day,stime,etime] = self
        clis[name] = self
        dlis[date.today().weekday()].append(self)
        dlis[date.today().weekday()].sort()


    def __str__ (self):
        return "%s ;;; %s ::: %s" %(str(self.stim),str(self.etim),str(self.name))

    def append(name,ostad,link,stime,etime,day):
        with open (file,'r') as F0:
            f = F0.read()
            with open(file,'w+') as F1:
                f1 = F1.read()
                f1.append('\n%s,%s,%s,%s,%s'%(name,ostad,link,stime,etime,day))
                F1.write(f1)
                F1.close
                sleep(0.5)
                Class(name,ostad,link,tm(st=stime),tm(st=etime),day)

    def v(self):
        if tm.now() >= self.stim and tm.now() <= self.etim: return 'start' ,tm.now()-self.stim
        elif tm.now() < self.stim : return 'nostart' ,self.stim-tm.now()
        elif tm.now() > self.etim : return 'end'     ,tm.now()-self.etim 

    
    def __le__(self,other):
        i = self
        o = other
        return i.stim > o.stim


    def __lt__(self,other):
        i = self
        o = other
        return i.stim >= o.stim


sync()











def run() :  
    drint = lambda x : print('',end=str(x))
















cod= {
    "-run":run,
    'run' :run,
}


ex = ['exit' ,'quit']
global In
In = ''
while In not in ex:
    In = input('(@)>>>  ')
    b = lambda x : x == In

    if len(argv) == 0:
        if b('add'): 
            n  = input('(name) >  ')
            l  = input('(link) >  ')
            st = input('(stime)>  ')
            et = input('(etime)>  ')
            d  = input('(day)  >  ')

            Class.append(n,l,tm(st=st),tm(st=et))

        elif b('run'): run()

    else : cod[argv[1]]()



