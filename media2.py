'''Calcula a média de nota entre 2 valores fornecidos pelo usuário
Exercita operações matemáticas e ordem de precedência'''

#cabecalho
print('-'*55)
print('Vamos calcular sua média de notas!')
print('-'*55)
#entrada
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
#calculos
media = (nota1 + nota2)/2
#resposta
print('A sua média ficou de {:.1f}'.format(media))