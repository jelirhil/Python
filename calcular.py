par= 0 
impar= 0
x=int(input("digite um numero:"))
for num in range(1,x+1):
    if num %2==0:
        par+=1
    else:
        impar+=1
print(f'Par:{par}')
print(f'Impar:{impar}')      
