'''Programa irá verificar se é permitido ou não o alistamento no exército
- exercita uso de if, else e elsif'''


#Cabeçalho
print('-------Verificação de alistamento-------')

#Entrada pelo usuário
ano = int(input('Digite o ano que o jovem nasceu: '))
idade = (2021-ano)

#respostas condicionais
if idade < 18:
    print('Ainda faltam {} anos para você se alsitar'.format(18-idade))
elif idade == 18:
    print('Está na hora de você se apresentar à junta militar de sua cidade! Aliste-se!')
else:
    print('Já passou {} anos do tempo de você se alistar. Se você ainda não se alistou, procure uma junta militar.'.format(idade-18))