#simulador de dados
#Objetivo: Tentar vencer a máquina em um jogo de dados

from random import randint
from time import sleep
print(f'{"<----A BATALHA PELA TERRA---->":>35}')
print(f'\n{"LANÇAMENTO DE DADOS":>30}')
print(f'Regras:'
      f'\n-Serão 3 jogadas de dado'
      f'\n-Vence quem tirar a maior pontuação'
      f'\nImpeça a Skynet de dominar o mundo'
      f'\n{"VAMOS COMEÇAR":>25}')
try:
    jogador = str(input('Insira o nome do campeão dos humanos: '))
except:
    print('Error')
else:
    print(f'\n{"VAMOS COMEÇAR":>25}')
sleep(1)

def lan_jog(msg):
    print('-'*40)
    print(msg)
    print('-'*40)

lan_jog(f"           \033[01;36m{jogador}\033[m X \033[01;35mSKYNET\033[m")

cont=jog=sky=0
for c in range(0,3):
    print('-='*20)
    d = str(input('Aperte uma tecla para fazer seu  lançamento: '))
    lan_jog('\033[01;36mJogador realiza seu lançamento de dado\033[m')
    j = randint(1,6)
    jog += j
    sleep(0.5)
    lan_jog("\033[01;35mSkynet realiza seu lançamento de dado\033[m")
    print('Processando...')
    sleep(1.5)
    s = randint(1,6)
    sky+=s
    print(f'Pontuação da rodada:\n\033[01;34mJOGADOR TIROU {j} E ESTA COM UM TOTAL DE {jog} '
          f'\n\033[01;35mSKYNET TIROU {s} E ESTA COM UM TOTAL DE {sky}\033[m\n')
sleep(1)
if jog > sky:
    print(f'Parabens \033[33m{"jogador"}\033[m você derrotou as máquina e salvou o mundo')
elif sky > jog:
    print(f"\033[01;31mA Raça humana foi subjulgada...acabou\033[m")
else:
    print("A batalha não teve seu destino, ambos os lados recuaram para lutar mais um dia...")

print(f"\n\n\033[1;32m{'THE END':>25}")