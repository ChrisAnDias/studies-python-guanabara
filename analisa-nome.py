'''Análise de uma string.
- exercita uso de ferramentas de alteração e análise de string'''

#cabeçalho
print('=' * 55)
print('Vamos analisar seu nome completo')
print('=' * 55)

#entrada usuário
nomecompleto = str(input('Digite seu nome completo: ')).strip()

#análises
print('Seu nome escrito em letras maiúsculas é {} '.format(nomecompleto.upper()))
print('Seu nome escrito em letras minúsculas é {}'.format(nomecompleto.lower()))
print('A quantidade de letras de seu nome é {} '.format(len(nomecompleto.replace(" ", ""))))
nomesimples = nomecompleto.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomesimples[0], len(nomesimples[0])))
