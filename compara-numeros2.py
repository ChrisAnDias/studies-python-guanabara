'''Programa que compara 2 números inserido pelo usuário
Exercita comparação, if elsif else'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um outro número inteiro: '))
if n1>n2:
    print('O primeiro valor é maior.')
elif n2>n1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior. Os dois são iguais.')