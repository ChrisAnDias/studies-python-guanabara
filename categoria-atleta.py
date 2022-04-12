'''retorna qual categoria se enquadra atleta.
exercita comparação, if, elsif e else'''

#cabeçalho
print('=' * 55)
print('-----Categoria de atletas-----')
print('=' * 55)
#entrada
ano = int(input('Digite o ano de nascimento do atleta: '))
if (2021 - ano) == 9 or (2021 - ano) < 9:
    print('A categoria do atleta é MIRIM')
elif (2021 - ano) > 9 and (2021 - ano) < 14 or (2021 - ano) == 14:
    print('A categoria do atleta é INFANTIL')
elif (2021 - ano) > 14 and (2021 - ano) < 19 or (2021 - ano) == 19:
    print('A categoria do atleta é JÚNIOR')
elif  (2021 - ano) > 19 and (2021 - ano) < 20 or (2021 - ano) == 20:
    print('A categoria do atleta é SÊNIOR')
else:
    print('A categoria do atleta é MASTER')