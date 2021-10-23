par = []
impar =[]

for i in range(20):
    if i % 2 ==0:
        par.append(i)
    else:
        impar.append(i)
print(f'Números Pares: {par}')
print(f'Números Ímpares:{impar}')
