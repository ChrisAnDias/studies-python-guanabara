'''Verifica presença de letra A na frase inserida pelo usuário.
Exercita formatações de string'''

#entrada
frase = str(input('Digite uma frase qualquer: ')).strip()
#Saída
print('A letra A aparece {} vezes.'.format(frase.upper().count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.upper().find('A')+1))
print('A última vez que a letra A aparece na posição {}'.format(frase.upper().rfind('A')+1))