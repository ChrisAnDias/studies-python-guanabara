'''calcula custo de passagem para uma viagem
exercita if e else, comparação'''

#entrada
distancia = float(input('Digite a distância em Km da sua viagem e eu te direi quanto pagarás pela passagem: '))
#condicões
if distancia <= 200:
    precocusto = distancia * 0.50
    print('A passagem custará {} reais'.format(precocusto))
else:
    precocusto2 = distancia * 0.45
    print('A passagem custará {} reais'.format(precocusto2))