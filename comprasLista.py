compras=[]
while True:
    produto=input("produto:")
    if produto =="fim":
        break
    quantidade = int(input("quantidade:"))
    preco=float(input("preco:"))
    compras.append([produto,quantidade,preco])
soma= 0.0
for e in compras:
    print("%20s x%5d %5.2f %6.2f" %(e[0],e[1],e[2],e[1]*e[2]))
    soma+= e[1]*e[2]
print ("total:%7.2f" %soma) 