'''Programa converte temperatura de celcius para farenheit
Exercita divisão variável por constante'''

tempcelsius = float(input('Digite a temperatura em Celcis (Cº) que vocÊ quer saber em Farenheit (F): '))
tempfarenheit = (tempcelsius * 9/5) + 32
print('A temperatura {}ºC em Farenheit é {} F.'.format(tempcelsius,tempfarenheit))