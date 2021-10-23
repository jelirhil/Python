a = int (input('valor inicial:'))
j = float(input('taxa de juros:'))
jr=j/100
t=0
tx=1
x=0
while t <= 15:
    tx=jr *a
    t=t+1
    a=tx+a
    print  ('rendimento mensal: %6.2f' %a)  