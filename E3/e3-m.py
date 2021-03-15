0

from sklearn import tree

from mysql.connector import connect

from re import findall as find


x = []
y = []


pro_dict = lambda o1 : pro_dict[o1] if o1 in pro_dic else o1

pro_dic = {
    'DDR3':   '3',
    'DDR4':   '4',
    'DDR5':   '5',
    'DDR6':   '6',
    'GDDR3':   '4.5',
    'GDDR4':   '5.5',
    'GDDR5':  '6.5',
    'GDDR6':  '7.5',
    'GDDR4X':  '6',
    'GDDR5X': '8',
    'GDDR6X':  '10',
    'HBM':    '6.5',
    'HBM2':   '8.5',



}




def import_data ():
    print ('insert your sql connection information :\n')
    u = input('user :')
    if u == '':
        u = 'root'
    p = input('password :')
    h = input('host :')
    if h == '':
        h = 'localhost'
    db = input('database :')
    if db == '' :
        db = 'vga_db'
    t = input('table :')
    if t == '':
        t = 'vga'

    sql = connect (
    host = h
    ,database = db
    ,password = p
    ,user = u
 )

    mydb = sql.cursor()




    ee = 0
            
    mydb.execute("SELECT * FROM %s" %t)

    data = mydb.fetchall()

    data.remove ((1.66,520,64,16,512,'DDR3'))
    data.remove ((3.8,1000,160,1280,512,'GDDR5X'))
    data.append ((1.5,1000,160,1280,7,'DDR3'))
    data.append ((3.5,1000,160,1280,7,'DDR4'))
    data.append ((7.1,1000,160,1280,8,'DDR5'))
    for q in data :
        if '/' in q[5]:
            qqq = find(r"([\d,\w]+)[\s,\\]",q[5]) [0]
        else:
            qqq =  q[5]
        y.append ( str(q[0]) )
        x.append ([])
        
        for qq in q[1:5]:
            x[ee].append ( str(qq) )
        x[ee].append(pro_dic[qqq])
        ee += 1
    





import_data()




def input_data () :
    z1 = input('hearts : ')
    z2 = input('storage : ')
    z3 = input('storage_tech : ').upper()
    z4 = input('core : ')
    z5 = input('bit : ')
    return [z1,z5,z4,z2,pro_dic[z3]]









print ('we are creating a moshine learning')



moshine = tree.DecisionTreeClassifier()

print ('.')

moshine.fit(x,y)

print ('completed !!')

in2 = []
while True  :
    in2 = input_data()
    
    if ';' in in2 :
    
        break

    for q in range(0,len(in2)) :
    
        in2[q] = str(in2[q])
    
    out = moshine.predict([in2])[0]
    print ('flaps = %s' %out) 

