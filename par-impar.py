'''Retorna se um número é par ou ímpar.
Exercita if e else, propriedades matemáticas'''

num = int(input('Digite um número inteiro e vou te dizer se ele é par ou ímpar: '))
resto = num % 2 #importante
if resto == 0:
    print('O número {} é par'.format(num))
else:
    print('O númetro {} é ímpar'.format(num))