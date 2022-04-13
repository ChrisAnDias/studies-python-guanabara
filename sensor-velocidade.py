'''Retorna se determinada velocidade está acima da velocidade permitida por lei. E ainda a multa que deverá
ser paga pelo condutor.
Exercita if, ordem de precedência,operações matemáticas'''

#entrada
velc = float(input('Digite em que velocidade em km/h o automóvel passou:'))
limv = 80 #km/h
#condições
if velc >= limv:
    mult = 7.0 * (velc - limv)
    #saída
    print('Você ultrapassou o limite de velocidade que é {}; Agora terá de pagar uma multa de {}'.format(limv, mult))