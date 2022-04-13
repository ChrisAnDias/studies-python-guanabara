'''Retorna o seno, cosseno, e tangente de um numero inserido pelo usuário.
Exercita uso de biblioteca nativa Pyhton.'''

#importando biblioteca
import math
#entrada
num = int(input('Digite um  número inteiro para saber seu seno, cosseno e tangente: '))
#calculos
rad = math.radians(num)
sen = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)
#saída
print('O seno do núm é {} \n O Cosseno do núm. é {} \n A tangente do núm. é {}'.format(sen, cos, tg))