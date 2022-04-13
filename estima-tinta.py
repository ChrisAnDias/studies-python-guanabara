'''Retorna a quantidade de tinta necessária para pintar uma parede nos dados forneciso pelo usuário
Exercita operações matemáticas'''

print('-'*55)
print('Calcula quantitativo de tinta necessário para pintar sua parede')
print('-'*55)

largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:)'))
area = largura*altura
quantidadel = area / 2
print('A área de sua parede é {}. Então você precisará de {} litros de tinta'.format(area,quantidadel))