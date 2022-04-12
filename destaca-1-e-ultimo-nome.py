'''Programa isola nomes
Exercita fatiamento de string'''

nomecomp = str(input('Digite seu nome completo: ')).strip()
nomesing = nomecomp.split()
print('Seu primeiro nome é {}: '.format(nomesing[0]))
print('Seu último nome é {}.'.format(nomesing[len(nomesing)-1]))
