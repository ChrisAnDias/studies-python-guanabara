'''calcula descondo de 5% em produto registrado por usuário
exercita ordem de precedência'''

#cabeçalho
print('=' *55)
print('Calculando o desconto.')
print('=' *55)

valorproduto = float(input('Digite o valor do produto:'))
desconto = valorproduto - (valorproduto*0.05)
print('O produto com 5% de desconto vale {}'.format(desconto))