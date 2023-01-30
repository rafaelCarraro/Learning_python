import math
a = float(input('digite um angulo: '))
r = math.radians(a)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('este são os seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(s, c, t))
