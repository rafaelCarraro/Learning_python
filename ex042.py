r1 = float(input('Digite um comprimento de reta: '))
r2 = float(input('Agora outro: '))
r3 = float(input('O último: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Você pode formar um triângulo', end='. ')
    if r1 == r2 and r2 == r3:
        print('E este triângulo é Equilatero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('E este é um triângulo Isóceles')
    else:
        print('Este é um triangulo Escaleno')
else:
    print('dois comprimentos de reta nao são suficientemente grandes para formar um triângulo')
