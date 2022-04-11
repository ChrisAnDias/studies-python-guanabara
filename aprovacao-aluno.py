'''verifica aprovação do aluno com notas inseridas pelo usuário
-exercita if, elsif, else, comparação'''

#cabeçalho
print('=' * 55)
print('Responde APROVADO | REPROVADO | RECUPERAÇÃO')
print('=' * 55)

#entradas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
#calculo
media = (n1+n2)/2
#condições
if media < 5.0:
    print('REPROVADO')
elif media == 5.0 or media > 5 and media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')