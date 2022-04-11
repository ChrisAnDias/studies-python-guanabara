'''Responde o antecessor e sucessor do número inserido pelo usuário
- exercita operações matemáticas'''

#exemplo1
'''
print('Vou te dizer o antecessor e sucessor do valor que você digitar:')
n1 = int(input('Digite um valor:'))
antec = n1 - 1
suc = n1 + 1
print('O antecessor vale {}, e o sucessor vale {}'.format(antec,suc))
'''

#exemplo2. economizando mais memória.pois tem menos linhas de código
n1 = int(input('Digite um valor:'))
print('O antecessor vale {}, e o sucessor vale {}'.format((n1-1),(n1+1)))

#Caso eu precisasse da variável no futoro, seria melhor trabalhar com o 1ºmodo de fazer o exercício