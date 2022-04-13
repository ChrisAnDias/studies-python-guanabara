'''Retorna se é possível formar um triângulo com 3 números informados pelo usuário.
Exercita condições de comparação, if e else'''

#cabeçalho
print('-'*55)
print('Vamos descobrir se é possível formar um triângulo')
print('-'*55)
#entrada
seg1 = int(input('Digite um valor inteiro que represente um segmento de reta:'))
seg2 = int(input('Digite um outro valor inteiro que represente um outro segmento de reta:'))
seg3 = int(input('Digite ainda um terceiro valor que represente um outro segmento de reta:'))
#calculos|condições|saída
if seg1 + seg2 < seg3 or seg1 + seg3 < seg2 or seg2 + seg3 < seg1:
    print('Sim. É possível formar um triângulo.')
else:
    print('Não. Infelizmente não é possível formar um triângulo')