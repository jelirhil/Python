n=1 #int (input('valor inicial:'))
y = int (input('tabuada do :'))
s= y * n
while s <=  (y*10):
    print ('tabuada do {a} x {b} = {c}.'.format(a=y,b=n,c=s))
    s= (s+y)
    n+=1