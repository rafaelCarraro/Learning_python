lc = ('Jimo', 15, 'Kisuco Fervido', 7.5, 'Manifesto Comunista', 5, 'Coquetel Molotov', 12.5, 'Camisa do BR', 250.50, 'Conciliação de Lula', 200000, 'Filiação à UP', 0)
print('-' * 37)
for c in range(0,len(lc), 2):
   print(f'{lc[c]:.<25}R${lc[c+1]:>10.2f}')
print('-' * 37)
