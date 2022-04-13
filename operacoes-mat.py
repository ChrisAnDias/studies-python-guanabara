'''Retorna resultado de operações matemáticas
Exercita: uso de {} e .format() | espeficação das casas decimais | operações matemáticas'''

#entrada
num1 = int(input('Digite um valor:'))
num2 = int(input('Digite outro valor:'))

#cálculos
soma = num1 + num2
multip = num1 * num2
div2 = num1 / num2
divint = num1 // num2
potencia = num1 ** num2

#saída
print('A soma vale {}, a multiplicação vale {}, a divisão vale {:.3f}'.format(soma,multip,div2), end=' ')
print('A divisão inteira vale {}, a potencia vale {}'.format(divint,potencia))