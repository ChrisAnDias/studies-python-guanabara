'''Retorna se é possível um usuário pedir emprétimo no banco ou não
Exercita comparação, if e else, ordem de precedência'''

#entradas
valorcasa = float(input('Digite o valor, em reais, da casa: '))
salario = float(input('Digite o valor, em reais, do salário do comprador: '))
anospagar = float(input('Digite o valor, em anos, de quantos anos gostaria de pagar o financiamento: '))
#cálculos
parcela = valorcasa // anospagar
#condições
if (salario*0.3)>parcela:
    print('O financiamento foi APROVADO! E o valor da parcela será de {}'.format(parcela))
else:
    print('Infelizmente o financiamento foi RECUSADO. Pois o valor da parcela na quantidade de anos você deseja pagar '
          'excede 30% de seu salário.')
print('Obrigada por nos consultar.')