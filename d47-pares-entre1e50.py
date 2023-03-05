#minha resolução
#uso de range e if
for i in range(1, 51):
    par = i % 2 #verifica se cada número é par (divisível por 2)
    if par == 0: #se for par, retorna na tela o número
        print(i)
        #outro jeito de printar
        #print(n, end=' ')

#resolução do professor
for n in range(2,51,2):
    print(n, end=' ')
print('Acabou')
#Quando se usa essa resolução, se economiza espaço na memória.
#O objetivo é retornar todos os números pares, entre 0 e 50. Logo, essa resolução atende aos requisito.
#Faz o range, começando de 2 indo até 50 pulando de 2 em 2.