from datetime import datetime
saporra = {}

saporra['Nome'] = str(input('Nome: '))
i = int(input('Data de nascimento: '))
saporra['Idade'] = datetime.now().year - i
saporra['CPTS'] = int(input('Carteira de trabalho (0 não tem): '))
if saporra['CPTS'] != 0:
    saporra['Contratação'] = int(input('Ano de contratação: '))
    saporra['Salário'] = float(input('Salário: '))
    saporra['Aposentadoria'] = (saporra['Contratação'] - i) + 35
print('-=' * 40)
for k, v in saporra.items():
    print(f'{k} tem o valor {v}')

