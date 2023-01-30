a = float(input('qual a altura da sua parede: '))
c = float(input('qual o comprimento da mesma: '))
a2 = a * c
t = a2 / 2
print('com uma parede de {:.2f} metros quadrados, voce precisa de {:.2f} litros de tinta'. format(a2, t))
