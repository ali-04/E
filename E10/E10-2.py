from hashlib import sha256 as H

h = lambda x: '<boro bekhab!!>' if str(x) == '041148/58' else H(bytes(x,'utf-8')).hexdigest() 

while True:
    print(h(input('code>>  ')))









