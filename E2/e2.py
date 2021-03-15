


n = lambda x: print ('\n'*x)

iton = lambda x : dic[int(x)] [4]
itos = lambda x : dic[int(x)] [1]
stoi = lambda x : dicq[str(x)]
ston = lambda x : dic[dicq[str(x)]][4]


Rr = lambda x : ','.join(x)


































def err (x):
    print_all('')
    print(' <%s>   ??????' % x)












#                                      ##
#                                      ##            _____
#                  |                                /     \          _____|_____
#                  |                   ||          |                      |
#                  |                   ||           \_____                |
#                  |                   ||                 \               |
#                  |                   ||                  |              |
#                  |                   ||           \_____/               |
#                  |_______            ||                                 |














def blist (lis,x):
    if len(lis) > x :
        return True 
    else:
        return False 






def alist (lis,x,y):
    for q in range (0, x - len(lis) +1 ):
        lis.append (y)














def b_list(x,y):
    for q in x:
        y.append(q)












def randlist(x):
    from random import randint
    y = x
    z = list()
    for q in range(0,len(x)):
        im = randint (0,len(y)-1)
        z.append (y[im])
        del (y[im])
    return z











def list_get (lis,x,y):
    if len(lis) > x :
        return  lis[x]
    else:
        return  y









def bin (x,y) :
    for q in y :
        if not (q in x) :
            return False
    return True




def taf_lis (x,y) :
    q = list()
    b_list (x,q)
    for q10 in y:
        if q10 in q :
            q.remove (q10)
            
    return q 

















#                _______             ______ 
#               |        \          |      \
#               |         \         |       |
#               |          |        |______/    
#               |          |        |      \
#               |         /         |       |
#               |_______ /          |______/
#

















def dbc_open (loc):
    
    #    from os import path
    from csv import reader

    
    o = open (loc,'r')
    with o as p:
        fil = list(reader(p))
        o.close()
    return fil
    










def dbc_write (loc,lis):
    with open(loc,'w+') as File:

        for line in lis:
            q = list()
            
            
            for har_chiz in line:
                q.append ( str(har_chiz) )
            File.write(Rr(q))
            
            
            File.write('\n')
        
        File.close()








def dbc (name,code) :
    
    from os import path
    from os import getcwd

    loc = str( getcwd() ) + '\\' + ('%s.csv' %name)

    if not ( path.exists(  loc  ) ) :
        q2 = open (loc,'w+')
        q2.write ('t,%s' % str  ( ','.join( dici ) ) )
        q2.close 
        print ('plese restart program')
        input('Insert Enter  ...\n\n')
        exit()


    if type(code) == str :


        if code == 'open': 

            dic = dict()
            qx = dbc_open(loc)

            for q in qx :
                dic [ q[0] ] = q[1:]

            return dic 




    elif type(code) == list :
        liscode = code[1:]
        code = code[0]
            

        if code == 'edit' :
                
            fFile = dbc_open(loc)

            lisa = dict()
            dicta = list()
            qlis = dict()


            for q in range(0,len(fFile)) :
                qa = fFile [q]
                lisa[qa [0] ] = q



            for q in range(0,len(liscode)) :
                qa = liscode [q]
                qlis[qa [0] ] = q



            for q in liscode:
                dicta.append ( q[0] )




            if  not  ( bin (  list( lisa.keys() )  , dicta ) ):
                app = taf_lis ( dicta ,  list( lisa.keys() ) )
                for aq in app :
                    fFile.append (liscode[qlis[aq]])


            qqqf = dict()    
            qqqc = dict()











            for qqqq in liscode :
                qqqc[qqqq[0]] = qqqq[1:]

            for qqqq in fFile :
                qqqf[qqqq[0]] = qqqq[1:]









            for q in qqqc :
                qqqf [ q ] = qqqc [ q ]

            fFile = []

            for q in qqqf:
                fFile.append( [ [q]   + qqqf [ q ]  ]  [0] ) 

            dbc_write(loc,fFile)






























#                _______
#               /       \         
#              |         |        |  /        ##                              
#              |         |        | /                                    _____|_____
#              |________/         |/          ||          | ______            |
#              |                  |           ||          |/      \           |
#              |                  |           ||          |        |          |
#              |                  |           ||          |        |          |
#              |                  |           ||          |        |          |      
#









def print_m (x,y):
    from time import sleep 
    for q in x.splitlines():
        print (q)
        sleep (y)





















def print_all (m):
    mo1 = 1
    mm = []
    if type(m) == list:
        mm = m[1]+m[0]
    if m == 'a' or type(m) == list :
        mo1 = 0
    w = list()
    for t in ac :
        for tt in range(1,19) :
            #tt = list(t.keys()) [t1]
            qqq = t.get(tt,'')
            if qqq != '':
                if type(m) == list and qqq[0] in mm:
                    aaq =  str ( qqq[ 1 ] )
                else:
                    aaq = str ( qqq[ mo1 ] )
            else :
                aaq = ''
            if len(aaq) == 1:
                aaq += ' '

            w.append (aaq)
        w.append('!?')
    if m == 'r':
        return print_j(w,m)
    print_j(w,m)
        








        
def print_une (x):
    a = int()
    b = int()
    c = int()
    lis = ['',''] + print_l ([x , dicq[x]])

    if list_get(dic[dicq[x]],5,'') == '':
        a = 3
        b = 4
        c = 0
    else:
        a = 3
        b = 4
        c = 0
        




    lis[5] += '    ' + list_get(dic[dicq[x]],5,'') 
    
    lis[a] += ("    tanavob = %i" % (dic[dicq[x]] [2] [0]))
    
    lis[b] += ("    gorop = %i" % (dic[dicq[x]] [2] [1])) 
    
    lis[a] += '    ' + (dic[dicq[x]][3]) 
    
    lis[c] += (dic[dicq[x]][4]) + ':' 
    
    lis[4].split()






    wwwe = len(lis[3])+1
    lis[1] += ('_'*(wwwe)) + '.'
    
    #lis [3] += ' '*4
    
   
    for q in range(2,len(lis)):
        lis[q] += (' '* (wwwe-len(lis[q]))) 
    

    lis [4] += ' '*9
    lis [3] += ' '*9


    for q in range(2,len(lis)):
        lis[q] += '|'


    lis.append(("_"*wwwe) + '|' )
    


    print_m ('\n\n'+('\n'.join(lis)),0.05)












def print_j(x,m):



    from termcolor import colored
    wer = 0
    n = 0
    vaz = 1
    dicl = list()
    dic = {1:'+',2:'|',3:'|'}
    while x[n] != '!?':
        if x[n] == '':
            dic[1] += '_'*3
            wer += 3
        else:
            rty = len(x[n])+1
            dic[1] += '_'*(rty)
            wer += rty
        n += 1
    n = 2
    for q in x :
        if q != '!?':
            if q == '':
                dic[n] += ('   ')
                dic[n+1] += ('   ')
                vaz = 0
            else:
                if vaz == 0:
                    dic[n] += '|'
                    dic[n+1] += '|'

                if q.strip() in list_get(m,1,[]) :
                    dic[n] += (colored (q  ,'blue' )+'|')           
                elif q.strip() in dici :
                    dic[n] += (colored (q  ,'red' )+'|')
                else:  
                    dic[n] += (colored (q  ,'green' )+'|')
                
                dic[n+1] += (('-'*2)+'|')
                vaz = 1
        else:
            n += 2
            dic[n] = '|'
            dic[n+1] = '|'
    qwe = 0
    for q in x:
        if q == '!?':
            qwe += 2
    for q in range(1,int((len(dic)-1)/2)):
        r = (q*2) + 1
        #dic[r] += '-'q
        # * int(len (dic.get(r+1,0)) - len (dic.get(r-1,100000)))) 
    dic[1] += '+'
    for q1 in range(0,qwe):
        q = list(dic.keys()) [q1]
        dicl.append(dic[q])
    dicl.append('+' + str('_'*(wer))+'+')
    dicl[len(dicl)-2] = dicl[len(dicl)-2] [:len(dicl[len(dicl)-2])] + '|'
    if m == 'r':
        return ('\n'.join(dicl))
    print_m ('\n'.join(dicl),0.015)














def print_l (a):
    
    from termcolor import colored

    color1 = 'blue'
    color2 = 'blue'



    lis = list()
    x = list()
    for q in a:
        x.append(str(q))
    m = 0
    for t in x :
        if len(t) > m:
            m = len(t)
    lis.append('_'*(m+2))
    for t in x:
        if( m - len(t)) > 0 :
            if ( m - len(t))%2 == 0:
                zzz = str(' '*int( (m - len(t))/2))
                zzx = str(' '*int( (m - len(t))/2))
                #lis.append('|' + zzz + str(t) + zzz + '|')
            else :
                zzz = str(' '*int( (m - len(t))/2))
                zzx = str(' '  + str(' '*int( (m - len(t))/2)))

            

            if t in dici :
                lis.append('|' + zzx + colored(t,color1) + zzz + '|')
            else:
                lis.append('|' + zzx + colored(t,color2) + zzz + '|') 

        else:
            if t in dici :
                lis.append('|'+colored(t,color1)+'|')
            else:
                lis.append('|'+colored(t,color2)+'|')
    lis.append('#'*(m+2))
    return(lis)

























#          _________            
#         |
#         |                            _____            ____   ____
#         |_________         \  /       ____\         |/    \ /    \
#         |                   \/       /    |         |      |      |
#         |                   /\      |     |         |      |      |
#         |_________         /  \      \____|         |      |      |
#
#









def wr_db (x) :
    base = dbc ('edata','open') ['t']
    notb = taf_lis (base,x)
    dbc ('edata' ,['edit', ['t'] + notb ])
















def Exam(m):


    from termcolor import colored
    from time import sleep

    

    t = randlist ( dbc ('edata','open') ['t'] )
    
    iqd = Qd [m]


    
    if t != []:
        print ( colored (  "%s:"    % iqd['en']     ,'red')  )
    
    vv = 1
        
    
    ttt = []


    oo = []
    ooo = []

    while t != [] :


        tt = []


        for q1 in range(0,len(t)):
            
            
            q = t[q1]
            b = 0

            examer = iqd ['examer'] (q)
            
            #aj = ston(examer)
            
            #jas = str(stoi(examer))




          
            n(1)

            print ('|    %s:'    % colored (examer , 'blue') )
            sleep (0.05)
            print ('_'*len('|   ' + examer + ':'))
 


            for q3 in iqd ['j']:

                print ('|   insert '+'It'+"'"+'s %s.' % colored( q3 [1] , 'green') )
                sleep(0.06)
                j = input ('       ?^' +  colored('>> ' , 'blue')   )
            
                if j == 'exit' or j == 'back':
                    b = 0
                    vv = 0
                    t = []
                    wr_db (ttt)

                    break
            
                if j == 'a' and q3 [1] == 'Number' :
        
                    print_all([oo,ooo])
                    n(3)
                    j = input('       ^??' + colored ('>>' , 'red'))
        
        
                    if j == 'coex':
                        
                        
                        qer = co_exam('c',[oo,ooo])
                        oo += qer [0]
                        ooo += qer [1]
                        
                        n(2)
                        print ('|    %s:'    % colored (examer , 'blue') )
                        sleep (0.01)
                        print ('_'*len('|   ' + examer + ':'))
                        sleep (0.01)
                        print ('|   insert '+'It'+"'"+'s %s.' % colored( q3 [1] , 'green') )
                        sleep (0.01)
                        j = input('       ^??' + colored ('>>' , 'red'))
                        



                if j == q3 [0] (q) :
                    print_m (ok,0.04)
                else :
                    print_m (ooh,0.04)
                    b = 1
            
            if b == 1:
                print_une( itos (q) )
                tt.append(q)
                if input('are you ok?') == 'no':
                    n(3)
                    sleep (1)
                    n(3)
                    print ("Not important !")
                    
                    n(1)

                    sleep (2.5)

                    n(2)


                    
            elif vv == 1 :
                oo.append (int(q))
                ttt.append (q)
                print_m (ook,0.04)


            if vv == 0 :
                break


        t = []
            

        b_list (tt,t)


        if vv == 1 and t == []:
            wr_db (ttt)
            print_m(oook,0.04)
        
        if vv == 0 :
            break 
    

    
    if vv == 1 and t == []:
        wr_db (ttt)
        print_m(gre,0.04)



    
























def co_exam (m,ss) :
    

    from termcolor import colored
    from time import sleep

    

    t = dici
    
    iqd = Qd [m]


    
    if t != []:
        print ( "%s:"    % iqd['en'])
    
    vv = 1
        
    
    ttt = ss[1]


    tt = ss[0]


    while t != [] :


    


            
            
        
        b = 0


        print_all([tt,ttt])

        
        

        n(2)

        print ("%s it! " %iqd['j'] [0] [1])

        n(1)


        try:
            j = input ('       ?^' + colored ('>> '  , 'green') ).split()

            
        #jas = str(stoi(examer))

        


          
        #n(1)

        #print ('|   ' + examer + ':')
        #sleep (0.05)
        #print ('_'*len('|   ' + examer + ':'))
 


        #for q3 in iqd ['j']:

        #print ('|   insert '+'It'+"'"+'s %s.' % ( q3 [1] ) )
        #sleep(0.06)
        #j = input ('       ?^>> ')
        
            if j[0] == 'exit' or j[0] == 'back':
                b = 0
                vv = 0
                t = []
                tt = []
                ttt = []
        #    wr_db (ttt)

                return [tt,ttt]
        

            if len (j) == 1:
                if j[0] in dici :
                    print_une (  itos ( j[0] )  )
                    n(2)
                    input()
                    j.append ( itos ( j[0] ) )
                    ttt.append( j [1] )
                else:
                    j.append (' ')





            examer = iqd ['examer'] (j[0])

            if list_get( j,1,'' ) == 'j':
                aj = itos (j[0])
            else :
                aj = iqd ['j'] [0] [0] (examer)







        #if examer == aj :
        #    print_all('a')
        #    n(3)
        #    j = input('       ^??>>')



            if aj == list_get(j,1,'') :
                print_m (ok,0.015)
                tt.append (int(j[0]))
                t.remove (j[0])
            else :
                print_m (ooh,0.015)
                b = 1
        
        #if b == 1:
        #    print_une( itos (q) )
        #    if input('are you ok?') == 'no':
        #        n(3)
        #        sleep (1)
        #        n(3)
        #        print ("Not important !")
                
        #        n(1)
        #        sleep (2.5)exit

        #        n(2)
                
        #elif vv == 1 :
                ttt.append (q)
                print_m (ook,0.015)
            if vv == 0 :
                break

        #t = []
            

        #b_list (tt,t)


        #if vv == 1 and t == []:
        #    wr_db (ttt)
        #    print_m(oook,0.04)
        
            if vv == 0 :
                break 
        except : ...
        

    return [tt,ttt]
    
    #if vv == 1 and t == []:
    #    wr_db (ttt)
    #    print_m(gre,0.04)


 














def quese(ms):
    
    for m in ms:
        if m[0] == 'f':
            if m[1:] == 'na':
                Exam('n')
            elif m[1:] == 'nu':
                Exam('u')
            elif m[1:] == 'sy':
                Exam('s')
        elif m == 'co':
            return co_exam('c',[[],[]])
#        elif m[0] == 'm':
#            if m[1:] == 'na':
#                q_name('m')
#            elif m[1:] == 'nu':
#                q_number('m')
#            elif m[1:] == 'sy':
#                q_sambol('m')
        



















































































































































































































Qd = {
         "s"  :{ 'en'  :'Symbol Exam'        ,   'examer'   : lambda x : itos(x) ,  'j'    : [ [lambda x : x , 'Number' ] ] }    
,        "u"  :{ 'en'  : 'Number Exam'       ,   'examer'   : lambda x : x       ,  'j'    : [ [lambda x : itos(x) , 'Number'] ] } 
,        "n"  :{ 'en'  : 'Name Exam'         ,   'examer'   : lambda x : iton(x) ,  'j'    : [ [lambda x : x , 'Number' ] , [lambda x : itos (x) , 'Symbol' ] ] }   
,        "c"  :{ 'en'  : 'Complator Exam'    ,   'examer'   : lambda x : x       ,  'j'    : [ [lambda x : itos(x) , 'Compelate'] ]}
}








H = [1,'H',[1,1],'Gas','Hydrogen']
He = [2,'He',[1,18],'Gas','Helium']
Li = [3,'Li',[2,1],'Solid','Lithium']
Be = [4,'Be',[2,2],'Solid','Beryllium']
B = [5,'B',[2,13],'Solid','Boron']
C = [6,'C',[2,14],'ُSolid','Carbon']
N = [7,'N',[2,15],'Gas','Nitrogen']
O = [8,'O',[2,16],'Gas','Oxygen']
F = [9,'F',[2,17],'Gas','Fluorine']
Ne = [10,'Ne',[2,18],'Gas','Neon']
Na = [11,'Na',[3,1],'Solid','Sodium']
Mg = [12,'Mg',[3,2],'Solid','Magnesium']
Al = [13,'Al',[3,13],'Solid','Aluminum']
Si = [14,'Si',[3,14],'Solid','Silicon']
P = [15,'P',[3,15],'ُSolid','Phosphorus']
S = [16,'S',[3,16],'Solid','Sulfur']
Cl = [17,'Cl',[3,17],'Solid','Chlorine']
Ar = [18,'Ar',[3,18],'Gas','Argon']
K = [19,'K',[4,1],'Solid','Potassium']
Ca = [20,'Ca',[4,2],'Solid','Calcium']
Ga = [31,'Ga',[4,13],'Solid','Gallium']
Ge = [32,'Ge',[4,14],'Solid','Germanium']
As = [33,'As',[4,15],'Solid','Arsenic']
Se = [34,'Se',[4,16],'Solid','Selenium']
Br = [35,'Br',[4,17],'Liquid','Barium']
Kr = [36,'Kr',[4,18],'Gas','Krypton']
Rb = [37,'Rb',[5,1],'Solid','Rubidium']
Sr = [38,'Sr',[5,2],'Solid','Strontium']
In = [49,'In',[5,13],'Solid','Indium']
Sn = [50,'Sn',[5,14],'Solid','Tin']
Sb = [51,'Sb',[5,15],'Solid','Antimony']
Te = [52,'Te',[5,16],'Solid','Tellurium']
I = [53,'I',[5,17],'Solid','Iodine']
Xe = [54,'Xe',[5,18],'Gas','Xenon','radio active !!!!!']
Cs = [55,'Cs',[6,1],'Solid','Cesium']
Ba = [56,'Ba',[6,2],'Solid','Barium']
Tl = [81,'Tl',[6,13],'Solid','Thallium']
Pb = [82,'Pb',[6,14],'Solid','Lead']
Bi = [83,'Bi',[6,15],'Solid','Bismuth','radio active !!!!!']
Po = [84,'Po',[6,16],'Solid','Polonium','radio active !!!!!']
At = [85,'At',[6,17],'Solid','Astatine','radio active !!!!!']
Rn = [86,'Rn',[6,18],'Gas','Radon','radio active !!!!!']
Fr = [87,'Fr',[7,1],'Liquid','Francium','radio active !!!!!']
Ra = [88,'Ra',[7,2],'Solid','Radium','radio active !!!!!']
Ni = [28,'Ni',[4,10],'Solid','Nickel']
Cu = [29,'Cu',[4,11],'Solid','Copper']
Zn = [30,'Zn',[4,12],'Solid','Zinc']
Cd = [48,'Cd',[5,10],'Solid','Cadmium']
Ag = [47,'Ag',[5,11],'Solid','Silver']
Au = [79,'Au',[5,12],'Solid','Gold']
Pd = [46,'Pd',[6,10],'Solid','Palladium']
Pt = [78,'Pt',[6,11],'Solid','Platinum']
Hg = [80,'Hg',[6,12],'Liquid','Mercury']


















ok = '''


                   /
                  /
                \/



                
'''


ook = '''                       

                           ______                _________
                |\   |     |           \   /         |
                | \  |     |_____       \ /          | 
                |  \ |     |            / \          |
                |   \|     |_____      /   \         |



'''



ooh = '''
                
                 \  /
                  \/
                  /\ 
                 /  \ 




'''



oook = '''

            __                      
           |  |    | /    __      __    ---|--- 
           |__|    |/    /  \     __\      |
              |    |     \__/    /  |      |  
            __/    |      \__    \__|      |
                                  


'''          






bye = '''






            _______                                 ________           
           |       \           \     /             |                   
           |        \           \   /              |                   
           |        /            \ /               |                   
           |_______/              V                |________           
           |       \              |                |                   
           |        \             |                |                   
           |        /             |                |                   
           |_______/              |                |________           
                                                                       


'''


















gre = '''


######################################################################################################################################
######################################################################################################################################
#########################################################...      ...############################################################################
###############################################+...                        ...+########################################################################
######################################=...                                      ....+###############################################################
##################################+....                                             ...++##########################################################
#################################+..                                                  ...++#####################################################
###############################++..                                                     ...+#######################################################
###############################=...                                                      ...=###############################################
############################..                                                           ...=############################################## 
#########################..                                        .==.                 ...==################################################              
######################.              .=... .....                ....####..             ....==###################################################
################=...            .   .=... ...=====......=====######======...         ....==################################################    
####=..                         .  ./           \.....==##########==.....          ....===##################################################     
###.                             ..|              \....====#####======..            ...====##################################################     
##=                              =...\            |../             \...".              ....==###########################################
                                .=##====..  .====.##.|              \..."                 ...=############################################       
                                 .=######==.=== /##\...\            /."                    ....=#################################
                                  .=########= =/###\ ..===... ....==.."                     ....=######################################
                                   .=##==    .\####/ ..####====##=.                            ...-=#############################################
                                    ..               .=========                                  ...-=#############################
                                  .         ..         .======                                   ....-###############################
                                 .        .==..         ..===                                      ..--################################
                                           ..          ..===                                        ----###############################                       
                                                                                                    ---=##################################
                                                                                                    ....#####################################
                                                                                                     ....#######################################
                                                                                                     ....################################
                                                                                                      ....#######################################
                                                                                                      ....################################
                                                                                                      ....#######################################
                                                                                                      ....################################


'''



all1 = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Ga','Ge','As','Se','Br','Kr','Rb','Sr','In','Sn','Sb','Te','I','Xe','Cs','Ba','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ni','Cu','Zn','Cd','Ag','Au','Pd','Pt','Hg']

dic = {1:H,2:He,3:Li,4:Be,5:B,6:C,7:N,8:O,9:F,10:Ne,11:Na,12:Mg,13:Al,14:Si,15:P,16:S,17:Cl,18:Ar,19:K,20:Ca,28:Ni,29:Cu,30:Zn,31:Ga,32:Ge,33:As,34:Se,35:Br,36:Kr,37:Rb,38:Sr,46:Pd,47:Ag,48:Cd,49:In,50:Sn,51:Sb,52:Te,53:I,54:Xe,55:Cs,56:Ba,78:Pt,79:Au,80:Hg,81:Tl,82:Pb,83:Bi,84:Po,85:At,86:Rn,87:Fr,88:Ra}

dicq = dict()
dici = list()
dicn = list()

for q in dic :
    dicq[dic[q][1]] = dic[q][0]

for q in all1 :
    dici.append(str(dicq[q]))

for q in all1 :
    dicn.append(dic[dicq[q]][4])



ac = [{1:H,18:He},{1:Li,2:Be,13:B,14:C,15:N,16:O,17:F,18:Ne},{1:Na,2:Mg,13:Al,14:Si,15:P,16:S,17:Cl,18:Ar},{1:K,2:Ca,10:Ni,11:Cu,12:Zn,13:Ga,14:Ge,15:As,16:Se,17:Br,18:Kr},{1:Rb,2:Sr,10:Pd,11:Ag,12:Cd,13:In,14:Sn,15:Sb,16:Te,17:I,18:Xe},{1:Cs,2:Ba,10:Pt,11:Au,12:Hg,13:Tl,14:Pb,15:Bi,16:Po,17:At,18:Rn},{1:Fr,2:Ra}]





































n(30)



from termcolor import colored
from time import  sleep 



code = colored("\n\n\n   &>"    , 'red')   + '>> '
print_all('')
in2 = input(code)
while in2 != "exit" and in2 != "quit" :
    if in2 != '' and  in2[0] == 'p':
        if len (in2) == 1:
            q2 = input('mode:'+"      %s> "   % colored ('^>' , 'blue')  )
        else:
            q2 = in2[2:]
        if q2 == 'tan':
            print_all('')
        elif q2 in all1 :
            print_une (q2)
        elif q2 in dici :
            print_une (dic[int(q2)][1])
        else:
            err ('p.%s' %q2)
    elif  in2 == 'q' or in2 == 'quese' :
        sssq = 1

        rrr = input ('mode:'+colored("   ^>",'blue') + '> ').split()
        for rq in rrr :
            if not (rq in ['fna','fnu','fsy','mna','mnu','msy','co']):
                err('quese.%s' %rrr)
                sssq = 0
                break
        if sssq == 1 :
            quese (rrr)
    elif in2 in all1 :
        print_une (in2)
    elif in2 == 'tan':
        print_all('')
    elif in2 == 'mo':
        print_m (gre,0.1)
    elif in2 in dici :
        print_une (dic[int(in2)][1])
    else:
        err(in2)        

    in2 = input(code)
    code = colored("\n\n\n   &>"    , 'red')   + '>> '
    


print(bye)



sleep (3)










