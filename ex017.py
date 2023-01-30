from math import sqrt
ca = float(input('o comprimento do cateto adjacente: '))
co = float(input('e agora o comprimeito do oposto:'))
'''h = sqrt(ca ** 2 + co ** 2)
print('a hipotenusa deste triangulo é {:.2f}'.format(h))'''
print("Sabendo que o cateto oposto vale {} e o cateto adjacente vale {}"
      "\nA hypotenuse valerá {:.2f}".format(co, ca, (sqrt(co ** 2 + ca ** 2))))
