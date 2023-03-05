frase = str(input('Digite uma frase que eu te digo se é um palímodro: ')).strip().lower().replace(" ", "")
fraseinv = frase[::-1]
if fraseinv == frase:
    print('A frase que você digitou é uma palímodro!')
else:
    print('A frase que você digitou não é uma palímodro.')
print('------------------------')
print('Não acredita? Veja por você mesmo!')
print('------------------------')
print(frase)
print(fraseinv)