from random import randint
n= int (randint(1, 9))
p=0
t=0
while n != p:
    p=int(input('chute um numero:'))
    t+=1
    if p==n:
        print('ufa acertou! Placar %i'%t)
    elif p <n :
        print  ('tente um valor maior')
    else  :
        print  ('tente um valor menor')
print ('fim de jogo')

