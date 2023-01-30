#média do aluno
m1 = float(input('Qual a média do primeiro semestre: '))
m2 = float(input('E a do segundo semestre: '))
mg = (m1 + m2) / 2
print('Sua média final é {:.1f}'.format(mg))
if mg == 7:
    print('Passou raspando, te cuida hein!!')
elif mg >= 8:
    print('Muito bem, aluno aplicado você, parabéns')
elif 5 <= mg <= 6.9:
    print('Você está em recuperação, vá estudar para sua prova')
elif mg < 5:
    print('É nisso que dá, não estudou o ano todo, REPROVADO, até ano que vem')
