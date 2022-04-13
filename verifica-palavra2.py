'''Verifica se nome inserido pelo usuário contém Silva
Exercita formatação string'''

nomeqlqr = str(input('Digite seu nome: ')).strip()
print('Seu nome contém Silva: ')
print('silva' in nomeqlqr.lower().split())