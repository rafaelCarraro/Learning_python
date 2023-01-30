s = 0
v = 0
for c in range(3, 500, 3):
    #print(c)
    if c % 2 == 1:
        s += c
        v += 1
        '''print('-'*5)
        print(s)
        print('-' * 5)'''
print('A soma de {} valores é de {}'.format(v, s))
