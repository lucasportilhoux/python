# In this exercise (proposed by the professor) we create a game program in which the computer guesses a number (in a range of options) and the user tries to discover what number was chosen by the machine.
# I liked this exercise because I used the library 'random' and used a very simple list to give an interesting interaction for the program. 

import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
n = int(input('Em que número eu pensei? '))  # Entrada de dados do usuário.
lista = [0, 1, 2, 3, 4, 0]
escolha = random.choice(lista)  # Faz o computador escolher um número entre 0 e 5.
print('Processando...')
sleep(3)
if escolha == n:
    print(f'Você ganhou! Eu pensei no número {n}')
else:
    print(f'Você perdeu! Eu pensei no número {escolha} e não no {n}!')
