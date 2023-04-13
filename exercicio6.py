notas=[]
media=[]
alunos_aprovados = 0

for i in range (3):
    print(f'notas do aluno {i+1}:')
    nota1 = float(input('Digite a primeira nota:'))
    nota2 = float(input('Digite a segunda nota:'))
    nota3 = float(input('Digite a terceira nota:'))
    nota4 = float(input('Digite a quarta nota:'))
    notas.append([nota1, nota2, nota3, nota4])
    media_aluno = (nota1 + nota2 + nota3 + nota4) / 4
    media.append(media_aluno)

    if media_aluno >7.0:
        alunos_aprovados += 1
print(f'numero de alunos com media maior ou igual a 7.0: {alunos_aprovados}')