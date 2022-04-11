'''#Tentando adivinhar o número que a máquina sorteou
exercita importação de bibliotecas de aleatoriedade e tempo, if | else'''

#importando bibliotecas de ação aleatória e de tempo
from random import randint
from time import sleep

#ação do PC
sorteio = randint(0,5)

#Cabeçalho - Explicação ao usuário
print('=' * 55)
print('Vou pensar em um númedo enre 0 e 5 e você tenta adivinhar')
print('=' * 55)

#entrada
tentativa = int(input('Em que número eu pensei?'))
print('Processando...')
sleep(3)

#resposta
if tentativa == sorteio:
    print('Parabéns! Você acertou!')
else:
    print('Errou! Eu pensei no número {} e não no número {}'.format(sorteio,tentativa))
