lista_pesos = []
for i in range(1,6):
    peso = int(input('Digite o peso da {} pessoa: '.format(i)))
    lista_pesos.append(peso)

print('O peso máximo lido foi de: ', max(lista_pesos))
print('O peso mínimmo lido foi de: ', min(lista_pesos))

