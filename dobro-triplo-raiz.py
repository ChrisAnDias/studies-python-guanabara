'''Programa diz o dobro, o triplo e a raíz quadrada de número inserido pelo usuário
Exercita multiplicação, divisão, biblioteca nativa de python para raíz'''

#exemplo1
'''print('Vou te dizer o dobro, o triplo e a raíz quadrada do valor que você digitar:')
num = int(input('Digite um valor:'))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2) #Raíz pode ser também encontrada pela função pow. pow(base,expoente). Para o caso: pow (n,(1/2))
print('O dobro vale {}, o tripo vale {}, e a raiz quadrada vale{:.2f}'.format(dobro,triplo,raiz))
Ou fazendo de outra forma'''

#exemplo2
num = int(input('Digite um valor:'))
print('O dobro vale {}, o tripo vale {}, e a raiz quadrada vale {:.2f}'.format((num*2),(num*3),pow(num,(1/2))))