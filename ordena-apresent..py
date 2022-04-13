'''Ordena uma sequencia de alunos. Informação fornecida pelo usuário.
Exercita uso de biblioteca nativa pyhton, uso de lista'''

#importando biblioteca
import random

#cabeçalho
print('-'*55)
print('----------Ordem de apresentação dos alunos---------')
print('-'*55)
aluno1 = str(input('Digite o nome do aluno 1 : '))
aluno2 = str(input('Digite o nome do aluno 2 : '))
aluno3 = str(input('Digite o nome do aluno 3 : '))
aluno4 = str(input('Digite o nome do aluno 4 : '))
listaaluno = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(listaaluno)
print('A ordem de apresentação será:')
print(listaaluno)