r1 = float(input('Digite um comprimento de reta: '))
r2 = float(input('Agora outro: '))
r3 = float(input('O último: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Você pode formar um triângulo')
else:
    print('dois comprimentos de reta nao são suficientemente grandes para formar um triângulo')
