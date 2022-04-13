'''Sorteia um aluno dentro de uma lista de alunos informada pelo usuário.
Exercita uso de biblioteca pyhton, lista'''

#importação
import random

#cabeçalho
print('-'*55)
print('-----------Sorteio do aluno que apagará o quadro---------')
print('-'*55)
#entradas
aluno1 = str(input('Digite o nome do 1º aluno: '))
aluno2 = str(input('Digite o nome do 2º aluno: '))
aluno3 = str(input('Digite o nome do 3º aluno: '))
aluno4 = str(input('Digite o nome do 4º aluno: '))
#calculos
listalunos = [aluno1, aluno2, aluno3, aluno4]
escolha = random.choice(listalunos)
#saída
print('O aluno que apagará o quadro hoje será o {}'.format(escolha))