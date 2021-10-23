from random import randint

dado = randint(1,6)

while True:
    esc= int(input('escolha um numero do dado:'))
    if esc == dado:
        print('voce ganhou!')
        break
    else:
        print('voce errou')
        print('tente novamente')
        tentar= str(input('se Sim aperte S se nao aperte N:').upper())
        if tentar == 'N':
            break