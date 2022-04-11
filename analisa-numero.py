'''Análise de um número.
- exercita uso de ferramentas de análise de números'''

#cabeçalho
print('=' * 55)
print('Vamos analisar o número que você colocar')
print('=' * 55)

#entrada
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {} temos que:'.format(num))
print('Unidade: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))