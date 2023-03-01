salario = float(input('Qual é o salário de um funcionário: R$ '))
aumentosalarial = salario * 10 / 100
valorfinal = salario + aumentosalarial
print('O funcionário que ganhava R$ {:.3f} com 10% de aumento salarial vai passar a ganhar R$ {:.3f}'.format(salario, valorfinal))
