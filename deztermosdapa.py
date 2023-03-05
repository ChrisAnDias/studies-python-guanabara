print('---------- Me digas o primeiro termo e a razão de uma PA que eu te retorno os 10 primeiros termos desta PA ----------')

#Uma PA vai acrescer a razão ao termo. Pensando nisso
termo1 = int(input('Digite o Termo 1 da PA: '))
razao = int(input('Digite a Razão da PA: '))
termo11 = termo1 + (10*razao)
print('Os 10 primeiros termos da PA são: ')
for i in range(termo1, termo11, razao):
    print(i)
