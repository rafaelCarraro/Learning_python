from random import choice
a1 = str(input('digite um nome: '))
a2 = str(input('digite o segunto nome: '))
a3 = str(input('mais um: '))
a4 = str(input('agora o ultimo: '))
lista = [a1, a2, a3, a4]
e = choice(lista)
print("o nome escolhido foi de {}".format(e))
