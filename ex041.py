a = int(input('Nos diga sua data de nascimento: '))
i = 2022 - a
c = ['mirim', 'infantil', 'junior', 'sênior', 'master']
if i <=9:
    print('Com {} a sua classificação é {}'. format(i, c[0]))
elif 9 < i <= 14:
    print('Com {} a sua classificação é {}'. format(i, c[1]))
elif 14 < i <=19:
    print('Com {} a sua classificação é {}'.format(i, c[2]))
elif i > 20:
    print('Com {} a sua classificação é {}'.format(i, c[4]))
else:
    print('Com {} a sua classificação é {}'.format(i, c[3]))