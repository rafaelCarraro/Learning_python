from x115.lib.interface import *


def arqEx(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print('Arquivo criado')


def lerarq(nome):
    global a
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('Erro de leitura.')
    else:
        menu('PESSOAS CADASTRADAS')
        for lin in a:
            dado = lin.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:.<30}{dado[1]:>3} anos')
    finally:
        a.close()


def addpers(arq):
    try:
        a = open(arq, 'at')
    except FileNotFoundError:
        print('Erro no cadastro de novas pessoas.')
    else:
        menu('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        a.write(f'{nome}; {idade}\n')
        print(f'Novo registro de {nome} adicionado.')
    finally:
        a.close()