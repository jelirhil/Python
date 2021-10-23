import random

def jogar():
    print('')
print('********************************')
print('***BEM VINDO AO JOGO DA FORCA***')
print('********************************')

arquivo = open('palavras.txt', 'r')
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

numero=random.randrange(0, len(palavras))

palavra_secreta = palavras[numero].upper()
letras_acertadas = ['_' for letra in palavra_secreta]

enforcou = False
acertou = False
erros = 0

print(letras_acertadas)

while(not enforcou and not acertou):
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    if (chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
    else:
        erros += 1
    enforcou = erros == 6
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)
if(acertou):
    print("Voce ganhou!!")
else:
    print("Voce perdeu!!")
    print('A fruta era',  format(palavra_secreta) )
print("FIM DE JOGO!!")