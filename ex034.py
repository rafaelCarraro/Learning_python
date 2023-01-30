s = float(input('digite o seu salário: '))
a = int(input('A quantos anos trablha na empresa? '))
if s > 1250:
    sn = s * 1.1
else:
    sn = (s * 1.15)
if a >= 5:
    b = 800 * a
else:
    b = 975 * a
print(f'Seu novo salário sera R${sn:.2f}, e você receberá um bonus de R${b}')
