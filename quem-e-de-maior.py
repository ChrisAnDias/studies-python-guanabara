lista_maior = []
lista_menor = []
for i in range(1,8):
    ano_nascimento = int(input('Digite o ano de nascimento da {} pessoa: '.format(i)))
    calc_idade = 2023 - ano_nascimento
    if calc_idade >= 21:
        lista_maior.append(i)
    else:
        lista_menor.append(i)

print('{} pessoas já atingiram a maior idade.'.format(len(lista_maior)))
print('{} pessoas ainda não atingiram a menor idade'.format(len(lista_menor)))


#posição das datas inseridas que são de maior
# print('Segue a posição das pessoas que são de maior: ', lista_maior)
# print('Segue a posição das pessoas que são de menor: ', lista_menor)