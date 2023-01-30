n1 = float(input('Nota do primeiro trimestre: '))
n2 = float(input('Nota do segundo trimestre: '))
m = (n1 + n2)/2
f = 21 - (n1 + n2)
print('A média do aluno é {}{:.3}{}, o meliante precisa de {}{:.3}{} pra passar de ano'.format('\033[4m',m, '\033[m', '\033[31m' if m < 7 else '\033[32m',f ,'\033[m' ))
