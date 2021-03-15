from random import randint

oo  = 0
t   = {}
me = 0
my = {}

while True :
    q = randint(0,100000)
    print ('%s:%s%s'%(oo,(10-len(str(oo)))*' ',q))
    oo += 1
    if oo ==  100005:
        print('ok  %i'%oo)
        break
    else:
        t[q] = t.get(q,0) + 1


for q0 in t:
    q = t[q0]
    
    me = q
    my[q] = my.get(q,[]) 
    my[q].append(q0)

for q0 in my :
    q = my[q0]
    print ({q0:q})
