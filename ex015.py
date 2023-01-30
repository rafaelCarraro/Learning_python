km = float(input('kilometragem percorrida: '))
d = int(input('diárias utilizadas: '))
v = (d * 60) + (km * 0.15)
print('percorrendo {} durante {} dias, o total a pagar é de R${:.2f}. \nObrigado, volte sempre'.format(km, d, v))
