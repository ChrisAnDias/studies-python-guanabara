print('-'*55)
print('TABUADA USANDO FOR')
print('-'*55)

num = int(input('Digite um número inteiro:'))
for i in range(1,11):
    mult = num * i
    print(num, 'x', i, '=', mult)
