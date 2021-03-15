from time import sleep

from mysql.connector import connect

from selenium import webdriver

from re import findall as find



companies = ["amd","nvidia"]
page = 1


local_db = []

d1 = 0



reg = {
    1 : [r'(\d*.\d*).','f']                                   # flaps_f
 ,  2 : [r'(.)','0']                                         # vat_f
 ,  3 : [r'\d{1,2}.','s']                                    # storage_f
 ,  4 : [r'(.{0,2}DDR\d.{0,2})','st',r'(.{0,1}HBM\d{0,1}.{0,1})']     # storage_tech_f
 ,  5 : [r'(\d+)','c']                                         # core_f  
 ,  6 : [r'(.)','0']                                       # logy_f
 ,  7 : [r'(\d+\.{0,1}\d*)','h']                                  # herts_f
 ,  8 : [r'(\d+)','b']                                      # bit_f
}

 









def list_get (lis,x,y):
    if len(lis) > x :
        return lis[x]
    else:
        return y





def b_data (data):

    if find(r'\d+\.{0,1}\d*',data['f']) == [] :
        return False 
    elif find(r'\d+\.{0,1}\d*',data['s']) == [] :
        return False 
    elif find(r'\d+\.{0,1}\d*',data['h']) == [] :
        return False 
    elif find(r'\d+',data['c']) == [] :
        return False
    elif find(r'\d+',data['b']) == [] :
        return False
    else:
        return True













def get_data (company,page,d1):

    i0 = 0
    

    elem = []

    driver.get("https://www.zoomit.ir/product/list/vga/%s/page/%i/"%(company,page))

    while  ( (page < 4 and len(elem) < 21  ) or (page == 4 and company == 'amd' and len(elem) < 10 ) or (page == 4 and company == 'nvidia' and len(elem) < 2) )  and  i0 < 15  :

        if "محصولی با این مشخصات یافت نشد" in  driver.page_source :
            break

        sleep (1)
        elem = driver.find_elements_by_class_name('col-sm-9')
        
    sleep(5)

    


    elem = driver.find_elements_by_class_name('col-sm-9')

    d1 = 1

    return elem 







def connect_db (data):
    u = input('user :')
    p = input('password :')
    h = input('host :')   
    db = input('database :')
    t = input('table :')
    

    sql = connect (
    host = h
    ,database = db
    ,password = p
    ,user = u
 )

    mydb = sql.cursor()

    for da in data:


        if da != {}:

            if b_data(da):
            
                mydb.execute('INSERT INTO %s (flaps               ,hearts             ,core            ,bit             ,storage          ,storage_tech) VALUES' %t    +
                                           ' ("%f"                ,"%f"              ,"%i"            ,"%i"            ,"%f"             ,"%s")'
                                 %    (       float(da ['f'])     ,float(da ['h'])   ,int(da ['c'])   ,int(da ['b'])   ,float(da['s'])   ,da['st']    )
             )
                sql.commit()










if d1 == 0 :

    driver = webdriver.Firefox()



data_b = ['']

ii = 0

for comp in companies :

    page = 1

    data_b = ['']

    while data_b != []:


        data_b = get_data (comp,page,d1)
        d1 = 1

        for qq in data_b :


            i = 1
            local_db.append({})
            for q in qq.text.splitlines ():


                
                ad = list_get (find (reg[i][0],q) , 0 , 'err')
                
                if reg[i][1] == 'st' and str(ad) == 'err':
                    ad = list_get (find (reg[i][2],q) , 0 , 'err')

                if ad == 'err':
                    print ('%s: err'  %q)

                local_db [ii] [reg[i][1]] = ad

                i += 1


            ii += 1
            print ('%i:'%ii)
            print ('%s\n' %str(local_db[ii-2]))
            

        page += 1    

    oo = 0



connect_db (local_db)























