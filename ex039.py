a = int(input('Diga o ano de seu nascimento: '))
b = 2022 - a
if 15 <= b <= 16:
    print('Ano que vem é ano de tirar o título de Eleitor')
    print('Se liga que faltam {} anos para você se alistar'.format(18-b))
elif b < 15:
    print('Vai curtir a vida enquanto ainda pode')
    print('Ainda faltam {} anos para seu alistamento'.format(18-b))
elif 16 < b <= 18:
    s = str(input('Você se identifica com qual gênero [M/F]: ')).strip().upper()
    if s == 'M':
        print('Está na hora de se alistar, não se esqueça')
    elif s == 'F':
        print('Você não precisa se alistar, mas se quiser também pode')
else:
    print('Tu já ta velho rapá, \nmas ainda pode entrar para o exercito proletário')
    print('Já fazem {} anos que você deveria ter se alistado'.format(b-18))
