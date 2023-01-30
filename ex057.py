'''s = False
n: str = ''
while s is False:
    n = str(input('Digite o sexo que você se identifica ')).strip()[0]
    if n in "mMfF":
        s = True
    else:
        s = False
if n in "fF":
    n = "Muié"
elif n in 'mM':
    n = 'Homi'
print('A milicia LGBT está contente, pode ir ja {}'.format(n))'''
n = str(input('Digite o sexo que você se identifica ')).strip()[0]
while n not in 'mMfF':
    n = str(input("Dados incorretos, tente novamnete")).strip()[0]
print('Sexo {} registrado com successo'.format(n))
