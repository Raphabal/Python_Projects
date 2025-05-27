from random import randint
from time import sleep
itens = ('Rock', 'Paper', 'Scissors')
pc = randint(0, 2)
#print(f'O Computador escholheu {itens[pc]}')
print('''Your options:
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSORS''')
jogador = int(input('Type your choice '))
print('ROCK')
sleep(0.5)
print('PAPER')
sleep(0.5)
print('SCISSORS!!!')
print('-=' * 11)
print(f'Computer played {itens[pc]}')
print(f'Player played {itens[jogador]}')
print('-=' * 11)
if pc == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('***TIE')
    elif jogador == 1:
        print('**Player WINS!**')
    elif jogador == 2:
        print('Computer WINS!')
    else:
        print('INVALID MOVE')
elif pc == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('Computer WINS!')
    elif jogador == 1:
        print('***TIE')
    elif jogador == 2:
        print('Player WINS!')
    else:
        print('INVALID MOVE')

elif pc == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('**Player WINS!**')
    elif jogador == 1:
        print('Computer WINS!')
    elif jogador == 2:
        print('***TIE')
    else:
        print('INVALID MOVE')

