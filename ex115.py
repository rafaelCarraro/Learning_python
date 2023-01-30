from x115.lib.interface import *
from x115.lib.arquivo import *
from time import sleep

a = 'arq'
if not arqEx(a):
    criararq(a)

while True:
    o = options(['Ver pessoas cadastradas;', 'Cadastrar nova Pessoa;', 'Sair do Sistema.'])
    if o == 1:
        lerarq(a)
    elif o == 2:
        addpers(a)
    elif o == 3:
        menu('Fim do programa! Até logo!!')
        break
    sleep(0.5)
