'''Calcula a hipotenusa de um triênagulo baseado em 2 valores fornecidos pelo usuário
Exercita biblioteca math nativa do python'''

#exemplo1
'''from math import sqrt, pow
print('Vou te dá a hipotenusa')
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = sqrt(pow(co,2) + pow(ca, 2))
print('O valor da hipotenusa é {}' .format(hp))'''

#exemplo2

#importando biblioteca
from math import hypot

#cabecalho
print('-'*55)
print('Vou te dá a hipotenusa de 2 catetos.')
print('-'*55)

#calculos
catoposto = float(input('Digite o valor do cateto oposto: '))
catadjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(catoposto, catadjacente)

#resposta
print('O valor da hipotenusa é {:.2f} '.format(hipotenusa))