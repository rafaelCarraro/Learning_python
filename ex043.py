p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))
imc = p / ((a * 0.01) ** 2)
if imc > 40:
    print('seu IMC é de {:.2f}, ou seja, Obesidade mórbida'. format(imc))
elif imc < 18.5:
    print('Seu IMC é de {:.2f}, ou seja, Abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.2f}, ou seja, voce está no peso ideal'.format(imc))
elif 25 <= imc < 30:
    print(' Seu IMC é de {:.2f}, portanto, voce está em sobrepeso'.format(imc))
else:
    print('Seu IMC é de {:.2f}, portanto você está em Obesidade'.format(imc))

