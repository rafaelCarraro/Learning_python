aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação do aluno'] = 'Aprovado'
elif aluno['Média'] <= 4:
    aluno['Situação do aluno'] = 'Reprovado'
elif 4 < aluno['Média'] < 7:
    aluno['Situação do aluno'] = 'Em Recuperação'
for k, v in aluno.items():
    print(f'{k} : {v}')
