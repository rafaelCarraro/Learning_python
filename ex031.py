d = int(input('Quantos Kilometros voce percorrerá na sua viagem? '))
v = str(input('é uma viagem de ida e volta? '))
if v == 'sim':
    dd = d * 2
    if dd > 200:
        print('A distância percorrida será de \033[4m{}km\033[m \nE o custo será de \033[1;33mR${:.2f}'.format(dd, dd * 0.45))
    else:
        print('A distância percorrida será de \033[4m{}km\033[m \nE o custo será de \033[1;33mR${:.2f}'.format(dd, dd * 0.5))
else:
    if d < 200:
        print('A distância percorrida será de \033[4m{}km\033[m \nE o custo será de \033[1;33mR${:.2f}'.format(d, d * 0.5))
    else:
        print('A distância percorrida será de \033[4m{}km\033[m \nE o custo será de \033[1;33mR${:.2f}'.format(d, d * 0.45))
