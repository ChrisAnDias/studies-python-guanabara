soma = 0
for i in range (0,6):
    n = int(input('Digite um número inteiro: '))
    par = n % 2
    if par == 0:
        soma = soma + n
print(soma)