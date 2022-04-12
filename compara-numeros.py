'''Programa que compara 3 números inserido pelo usuário
Exercita comparação, if and'''

#entrada
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite ainda outro número: '))
#condições
if n1 > n2 and n1 > n3:
    print('{} é o maior número'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior número'.format(n2))
if n3 > n2 and n3 > n1:
    print('{} é o maior número'.format(n3))
if n1 < n2 and n1 < n3:
    print('{} é o menor número'.format(n1))
if n2 < n2 and n2 < n3:
    print('{} é o menor número'.format(n2))
if n3 < n2 and n3 < n1:
    print('{} é o menor número'.format(n3))