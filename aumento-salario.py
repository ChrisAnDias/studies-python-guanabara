'''cálculo de aumento de salário
-exercita ordem de precedência'''


#cabeçalho
print('=' * 55)
print('Calcula aumento de salário do funcionário em 15%')
print('=' * 55)

salario = float(input('Digite o valor correspondente ao salário do funcionário:'))
aumento = salario + (salario * 0.15)
print('O salário com o aumento de 15% corresponde á {}'.format(aumento))