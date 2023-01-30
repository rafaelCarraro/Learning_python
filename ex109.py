from modulos import moeda

n = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.moeda(n)} é: {moeda.metade(n)}')
print(f'O dobro de {moeda.moeda(n)} é: {moeda.dobro(n)}')
print(f'Com acréscimo de 10% o valor é: {moeda.aumentar(n, 10)}')
print(f'Com desconto de 13% o valor fica: R${moeda.diminuir(n, 13)}')
