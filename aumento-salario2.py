'''calcula salário do funcionário mediante condição
exercita if e else, comparação maior'''

#entrada
salario = float(input('Digite o valor (em reais) do salário do funcionário para cálculo de aumento: '))
#condições
if salario > 1250.0:
    print('O valor do aumento do funcionário será de {}'.format(salario*0.1))
else:
    print('O valor do aumento do funcionário será de {}'.format(salario*0.15))