'''Verifica se o ano é bissexto
- exercita uso de if | else, resto de uma divisão'''

ano = int(input('Digite um ano que queira saber se é bissexto: '))
if ano % 4 == 0:
    print('Sim! Esse ano é bissexto!')
else:
    print('Não. Esse ano não é bissexto.')