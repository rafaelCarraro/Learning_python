from modulos import moeda

n = float(input('Digite o Preço: R$'))
print(f'A metade de R${n} é: R${moeda.metade(n):.2f}')
print(f'O dobro de R% {n} é: R${moeda.dobro(n):.2f}')
print(f'Com acréscimo de 10% o valor é: R${moeda.aumentar(n, 10):.2f}')
print(f'Com desconto de 13% o valor fica: R${moeda.diminuir(n, 13):.2f}')
