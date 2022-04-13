'''Verifica se nome inserido pelo usuário começa com a palavra 'Santo'
Exercita formatação string'''

#entrada
cidade = str(input('Digite o nome de sua cidade: ')).strip()
print('A sua cidade começa com a palavra Santo: ')
print(cidade[:5].upper() == 'SANTO')