num = int(input('Digite um número inteiro. e te digo se é um número primo ou não:'))
mult = 0
#primeiro laço verifica do número 2 até o número inserido se o resultado da divisão inteira entre esses números é igual a zero, acrescentando a variável mult criada para
#indicar que há múltiplos.
for i in range(2,num):
    if (num % i == 0):
        mult += 1

#if fora do laço verifica se a variável tem algum multiplo. não tendo retorna que é sim primo. Tendo retorna que não é primo.
if (mult == 0 and num >=2):
    print('É primo')
else:
    print('não é primo')