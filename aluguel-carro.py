'''Calcula quanto usuário irá pagar pelo aluguel de carro
- exercita multiplicação, uso {}.format, delimitação de casas decimais'''

#cabeçalho
print('=' * 55)
print('Quanto custará o aluguel do carro')
print('=' * 55)

#cálculos
kmpercorrido = float(input('Digite quantos km foi percorrido pelo carro alugado: '))
diasalugados = int(input('Digite quantos dias ele ficou alugado: '))
aluguel = (60 * diasalugados) + (0.15 * kmpercorrido)
print('O alguel sairá por R$ {:.2f} reais.'.format(aluguel))