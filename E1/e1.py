




def adad_avval (y) :
    qwe = list()
    for zx in range (2,y):
        vb = 0
        for zzx in range (2,zx):
            if zx % zzx == 0 :
                vb += 1
        if vb == 0 :
            qwe.append (zx)
    
    return qwe
    


def taj(y) :
    wer = []
    oi = y
    if y == 2 :
        return [2]
    elif y == 3:
        return [3]
    elif y == 4:
        return [2,2]
    if y == 1:
        return [1]
    qp = adad_avval (round(y/2)+2)
    qp.append (y)
    for not1 in qp:
        
        while oi % not1 == 0 :
            wer.append (not1)
            oi = int (oi / not1)
        

    return wer 

        





def tt1 (x,xx,xxx):   # در این دف دنباله تفاضلات و دنباله تفاضل تفاضلات محاسبه و ذخیره میشود
    xx.clear()
    xxx.clear()
    for q in range (0,len(x)):
        xx.append(int())
        xxx.append(int())

    
    for q in range (1,len(x)):
        xx[q] = x[q] - x[q-1]
    
    xx[0] = xx[1] - (xx[2]-xx[1])

    for q in range(1,len(x)):
        xxx[q] = xx [q] - xx [q-1]

    xxx [0] = xxx[1]




def tt2 (x,xx,xxx):   # در این دف دنباله تفاضلات و دنباله تفاضل تفاضلات محاسبه و ذخیره میشود
    xx.clear()
    xxx.clear()

    xx.append (int())
    for NHT in range(0,len(x)):
        xxx.append(taj(x[NHT]))
    #yt = 0
    #for jyjh in x:
    #    xxx[yt] = 
    #    yt += 1
    
    
    xx [0] = x[4] / x[3]




def mo1 (x,xx): # در این یکی جمله عمومی درجه یک ها محاسبه میشود
    xx [0] = xx [1]
    d = xx [0]
    b = x[0] - xx[0]
    if b < 0 :
        return ("t.n = %in - %i" %(d,abs(b)) )  
    elif b == 0 :
        return ("t.n = %in" %(d))
    else:  
        return ("t.n = %in + %i" %(d,b) )


def mo2 (x,xx,xxx) :      # در این فانکشن جمله عمومی جملات درجه دو محاسبه میشود
    out = str('t.n = ')
    a = xxx[0]/2       #   ضریب توان دو
    d = xx[0] - a    # متغیر توان یک
    b = x[0] - xx[0]    # عددی که هر دور با دنباله جمع میشود

            # t.n = a(n^2) + dn + b

    if a > 0:

        if a % 1 != 0:
            if a == 0.5:
                d -= 0.5
                out += ("((n.(n + 1)) /2) ")
            else:
                d -= 0.5
                out += ("%sn^2 + ((n.(n + 1)) /2) " %str(a//1))
        else:
            if a == 1:
                out += ("n^2 ")
            else :
                out += ("%s(n^2) " %str(int(a)))
    
        if round(d,0) == d:
            d = int(d)


        if round(b,0) == b:
            b = int(b)

    
        if d > 0 :
            out += ("+%sn " %str(d))
        elif d < 0 :
            out += ("-%sn " %str(abs(d)))
    
        if b > 0 :
            out += ("+%s" %str(b))
        elif b < 0 :
            out += ("-%s" %str(abs(b)))
    else:
        a *= -1
        if a % 1 != 0:
            if a == 0.5:
                d -= 0.5
                out += ("-((n.(n + 1)) /2) ")
            else:
                d -= 0.5
                out += ("-%s(n^2) - ((n.(n + 1)) /2) " %str(a//1))
        else:
            if a == 1 :
                out += ("-(n^2) ")
            else:
                out += ("-(%sn^2) " %str(int(a)))
    
        if round(d,0) == d:
            d = int(d)


        if round(b,0) == b:
            b = int(b)

    
        if d > 0 :
            out += ("+%sn " %str(d))
        elif d < 0 :
            out += ("-%sn " %str(abs(d)))
    
        if b > 0 :
            out += ("+%s" %str(b))
        elif b < 0 :
            out += ("-%s" %str(abs(b)))

    return out



def mo3(x,xx) :
    asd = str('t.n = ')
    a = x[1] / xx[0] ** 2
    wwe = taj (a)
 
    if a == xx[0] ** len(wwe):
        zxzx = len(wwe)
        asd += ("%i^(n+%i)" %(xx[0],zxzx))
    else:
        if a == 1 :
            asd += ("(%i^n)" %(xx[0]))
        else:    
            asd += ("%i(%i^n)" %(a,xx[0]))
     
    return  asd








t = [int(input('t.1   ')),int(input('t.2   ')),int(input('t.3   '))] #دریافت 3 جمله اول از کاربر
tt = list()  # این لیستی است که در آن دنباله تفاضلات ذخیره میشود
ttt = list()  # در این یکی دنباله تفاضل تفاضلات ذخیره میشود
tt1 (t,tt,ttt) 


if ttt[2] == 0 :          # بررسی وضعیت دنباله (درجه دنباله)
    print (mo1 (t,tt))   # حالت اول :درجه یک
else:      # حالت دوم:درجه دو
    t.append(int(input('t.4   ')))   # گرفتن جمله چهارم
    tt1(t,tt,ttt)
    if ttt[3] == ttt[2] :
        if ttt[2] < 0:
            print (mo2 (t,tt,ttt))
        else:
            print (mo2 (t,tt,ttt))
    else :     # حالت سوم :دنباله هندسی
        #t.append(int(input('t.4   ')))    گرفتن جمله چهارم
        t.append(int(input('t.5   ')))
        tt2(t,tt,ttt)
        print (mo3(t,tt))





















#q =1











