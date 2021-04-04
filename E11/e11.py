from selenium import webdriver as wd
from json import loads
from os import getcwd
global _students
_students = {}


with open(getcwd()+'setting.json' ,'r') as F:
    setting = loads(F.read())


ostad = input("ostad?  ")

global url
url = 'https://www.skyroom.online/ch/mr_sedaghat/ostad-%s'%ostad




class stu :
    _names    = {} 
    _students = []
    def __init__ (self,name,password):
        self.name = name
        self.password = password
        stu._students[len(stu._students)] = self
        stu._names[name] = self


    def __str__ (self):
        return self.name


    def print ():
        l = []
        q0 = 0
        for q in stu._students:
            q0 += 1
            l.append(str(q0)+"_"+str(q))
        return("\n".join(l))

    def _apend (self):
        self.driver = wd.Firefox()
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('stu_' + self.name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="btn_login"]').click()


    def delete (self):
        try: del self.driver
        except: pass
        stu._students.remove(self)
        del stu._names[self.name]
        del self
        
        

    def delete_all():
     #  print(stu._students)
        for q in stu._students:
            
            q.delete()
        stu._students = {}
        stu._names = []

    def dast(self):
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/button[7]').click()






for q in setting['students']: stu(q,setting['students'][q])

def loading(m=None):

    
   
    

    with open(getcwd()+'setting.json' ,'r') as F:
        setting = loads(F.read())

    for q in setting['students']: 
        if q not in list(stu._names):
            stu(q,setting['students'][q])
    
    
    for q in stu._names:
        if q not in setting['students']:
            stu._names[q].delete()








print (stu.print())








_code = {
    'append' : lambda x : stu._students[int(x)]._apend()   ,
    'reload' : lambda q : loading() ,
    'print'  : lambda x : print(stu.print()) ,
    'dast'   : lambda x : stu._students[int(x)].dast()
}

while True:
    code = input('code>> ').split()
    try:en = ' '.join(code[1:])
    except:en = None
    try:_code[code[0]] (en)
    except:pass


