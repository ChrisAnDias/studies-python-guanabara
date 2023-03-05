#primeiro: fazer uma lista vazia
lista = []
#percorrer os números de 1 a 500. Fazer dentro desse percorrer o teste se é multiplo de 3. Sendo, adicionar a lista vazia criada fora do for.
for i in range(1, 501):
    multiplo_tres = i % 3
    if multiplo_tres == 0:
        lista.append(i)
print(lista) #teste
#fora do laço, guardo em uma variável o somatório da lista que foi acrescida de elementos dentro do laço. No print, peço o retorno do somatório.
total = sum(lista)
print(total)
