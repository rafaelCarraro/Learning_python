#emprestimo
vc = float(input('Qual o valor da casa requisitada? '))
s = float(input('Qual o salário do comprador? '))
a = float(input('Em quantos anos pretende pagar?'))
p = vc / (a * 12)
if p > s * 0.3:
    print('Sinto muito porém o custo de {}R${:.2f}{} é maior que 30% do seu rendimento mensal'.format('\033[1;33m', p, '\033[m'))
else:
    print("Parabéns, você conquistou o direito ao empréstimo; \nAgora você terá de pagar {}R${:.2f}{} pelo o resto de "
          "sua vida, ou {} anos".format('\033[1;33m', p, '\033[m', int(a)))
