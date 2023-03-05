import numpy as np

print('Insira o nome, idade e sexo de 4 pessoas. E te retornarei a média das idades, o nome e idade do homem mais velho, e quantas mulheres são menores de 20 anos.')

lista_idades = []
idade_velho = 0
nome_velho = ""
mulheres_menor = 0

for i in range(1,5):
    print('---- {}º Pessoa ----'.format(i))
    nome = str(input('Digite o nome da {} pessoa: '.format(i)))
    idade = int(input('Digite a idade da {} pessoa: '.format(i)))
    sexo = str(input('Digite o sexo da {} pessoa (F/M): '.format(i)))

    lista_idades.append(idade)

    if sexo in 'Mm' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        mulheres_menor += 1
print('----------------------------------------------------------')
print('A média das idades do grupo é de: ', np.mean(lista_idades))
print('O homem mais velho se chama {} e tem {} anos'.format(nome_velho,idade_velho))
print('Tem {} mulheres menores de 20 anos'.format(mulheres_menor))

