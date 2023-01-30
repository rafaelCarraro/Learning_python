from time import sleep
from emoji import emojize

for f in range(10, -1, -1):
    print('\033[1:34m', f, '\033[m')
    sleep(1)
print(emojize(':fireworks:'*11, language='alias'))
print(emojize(':fireworks:'*11, language='alias'))
print('  FELIZ ANO NOVO CARAI   ')
print(emojize(':fireworks:'*11, language='alias'))
print(emojize(':fireworks:'*11, language='alias'))
