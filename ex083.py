lis = []
c: int = 0
e = str(input('Digite uma expressão com parenteses: ')).strip()
for x in range(0, len(e)):
    if e[x] == '(':
        lis.append(e[x])
    elif e[x] == ')':
        if len(lis) > 0:
            lis.pop()
        else:
            lis.append(')')
            break
if len(lis) == 0:
    print("Sua expressão está correta!")
else:
    print('Sua expressão está incorreta! \nExistem estes parenteses abertos: ', end=' ')
    for x, v in enumerate(lis):
        print(lis[x], end=' ')
