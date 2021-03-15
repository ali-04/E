from random import randint as ran

j = ran(0,400)

i = 1100



inp = 'adad'


Input = lambda x : int(input(x))

while i != j:
    i = Input('\n%s:>  '%inp)
    if i > j: inp = 'koochaktar'
    elif i< j: inp = 'bozorgtar'
    else: inp = '<<lebase erfan>>'
    
print('\n\n\n',inp)

