def maior(lista):
    maior_item = lista[0]
    for item in lista:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(lista):
    menor_item = lista[0]
    for item in lista:
        if item < menor_item:
            menor_item = item
    return menor_item

print(menor([21,356,1,6]))
print(maior([1,4,5,67,-73]))
