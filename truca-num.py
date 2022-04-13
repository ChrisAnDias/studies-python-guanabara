'''Retorna número truncado fornecido pelo usuário
Exercíta uso de biblioteca nativa python'''

#importação
from math import  trunc
#entrada
numqualquer = float(input('Digite um número qualquer. Poder ser com ponto ou sem ponto:'))
#saída
print('O número inteiro do que você digitou vale {}'.format(trunc(numqualquer)))