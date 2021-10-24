valor_casa = float(input("Valor do imovel desejado?:"))
salario = float(input("Salario:"))
tempo_pagando = int(input("numero de mensalidade:"))
valor_mensalidade = valor_casa/tempo_pagando
print("Valor mensalidade:R$%6.2f" % valor_mensalidade )
if valor_mensalidade > salario*0.3:
    print("recusado")
else:
    print("aprovado")
