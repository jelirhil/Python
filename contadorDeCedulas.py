valor = int(input('digite o valor a pagar:') )
atual = 50
notas = 0
apagar=valor
while True:
    if atual <= apagar :
       apagar-=atual
       notas+=1
    else :
        print('%d cedulas de R$%d'%  (notas,atual))
        if apagar== 0 :
             break
        if atual == 50:
           atual = 20
        elif atual ==20:
           atual =10
        elif atual ==10 :
            atual =5
        elif atual ==5 :
            atual =1
        notas =0
