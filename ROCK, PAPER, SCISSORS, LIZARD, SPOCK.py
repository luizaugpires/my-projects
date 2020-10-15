import random
import time

escolha = ("PEDRA", "PAPEL", "TESOURA", "LAGARTO", "SPOCK")
num1 = int(input("Escolha PEDRA[0], PAPEL[1], TESOURA[2], LAGARTO[3] ou SPOCK[4]:"))
num2 = random.randint(0, 4)

print("PEDRA!")
time.sleep(1)
print("PAPEL!")
time.sleep(1)
print("TESOURA!")
time.sleep(1)
print("LAGARTO!")
time.sleep(1)
print("SPOCK!")
time.sleep(1)
if num1<0 or num1>4: #JOGADA INVÁLIDA
    print("JOGADA INVÁLIDA")
elif num1 == 0: #JOGADOR JOGOU PEDRA
    print("O jogador escolheu {} e o computador escolheu {}!".format(escolha[num1], escolha[num2]))
    if num2 == 0:
        print("HOUVE EMPATE!")
    elif num2 == 1:
        print("VOCÊ PERDEU!")
    elif num2 == 2:
        print("VOCÊ GANHOU!")
    elif num2 == 3:
        print("VOCÊ GANHOU!")
    elif num2 == 4:
        print("VOCÊ PERDEU!")
elif num1 == 1: #JOGADOR JOGOU PAPEL
    print("O jogador escolheu {} e o computador escolheu {}!".format(escolha[num1], escolha[num2]))
    if num2 == 0:
        print("VOCÊ GANHOU!")
    elif num2 == 1:
        print("HOUVE EMPATE!")
    elif num2 == 2:
        print("VOCÊ PERDEU!")
    elif num2 == 3:
        print("VOCÊ PERDEU!")
    elif num2 == 4:
        print("VOCÊ GANHOU!")
elif num1 ==  2: #JOGADOR JOGOU TESOURA
    print("O jogador escolheu {} e o computador escolheu {}!".format(escolha[num1], escolha[num2]))
    if num2 == 0:
        print("VOCÊ PERDEU!")
    elif num2 == 1:
        print("VOCÊ GANHOU!")
    elif num2 == 2:
        print("HOUVE EMPATE!")
    elif num2 == 3:
        print("VOCÊ GANHOU!")
    elif num2 == 4:
        print("VOCÊ PERDEU!")
elif num1 == 3: #JOGADOR JOGOU LAGARTO
    print("O jogador escolheu {} e o computador escolheu {}!".format(escolha[num1], escolha[num2]))
    if num2 == 0:
        print("VOCÊ PERDEU!")
    elif num2 == 1:
        print("VOCÊ GANHOU!")
    elif num2 == 2:
        print("VOCÊ PERDEU!")
    elif num2 == 3:
        print("HOUVE EMPATE!")
    elif num2 == 4:
        print("VOCÊ GANHOU!")
elif num1 == 4: #JOGADOR JOGOU SPOCK
    print("O jogador escolheu {} e o computador escolheu {}!".format(escolha[num1], escolha[num2]))
    if num2 == 0:
        print("VOCÊ GANHOU!")
    elif num2 == 1:
        print("VOCÊ PERDEU!")
    elif num2 == 2:
        print("VOCÊ GANHOU!")
    elif num2 == 3:
        print("VOCÊ PERDEU!")
    elif num2 == 4:
        print("HOUVE EMPATE!")
