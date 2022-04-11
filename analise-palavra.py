'''Análise de uma string.
- exercita uso de ferramentas análise de string'''

#cabeçalho
print('=' * 55)
print('Vamos analisar uma palavra que você irá inserir')
print('=' * 55)

nome = input('Digite algo:')
print('O que está escrito é do tipo:', type(nome))
print('Em Verdadeiro ou falso vejamos se eu adivinho')
print('É uma palavra:', nome.isalpha())
print('É um número:', nome.isnumeric())
print('Todas as letras estão minúsculas: ', nome.islower())
print('Todas as letras estão em CapsLock:', nome.isupper())
print('Trata-se de algo alfa-numérico:', nome.isalnum())
print('E aí, acertei alguma?')