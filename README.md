# Calculo-de-aumento-salarial
Este código é uma implementação simples para calcular o aumento salarial de um funcionário em 10%. 

salario = float(input('Qual é o salário de um funcionário: R$ '))
Esta linha é responsável por receber a entrada do usuário, ou seja, o valor do salário atual do funcionário. A função input() solicita ao usuário que digite um valor, e a função float() converte esse valor para um número decimal (do tipo float), permitindo que o programa realize cálculos matemáticos.

aumentosalarial = salario * 10 / 100
Aqui, o código calcula o valor do aumento salarial em 10% do salário atual do funcionário. Essa instrução multiplica o salário digitado pelo usuário por 10 e divide o resultado por 100. O resultado é armazenado na variável aumentosalarial.

valorfinal = salario + aumentosalarial
Aqui, o código calcula o novo valor do salário do funcionário com o aumento incluído. Essa instrução adiciona o valor do aumento salarial à variável salario e armazena o resultado na variável valorfinal.

print('O funcionário que ganhava R$ {:.3f} com 10% de aumento salarial vai passar a ganhar R$ {:.3f}'.format(salario, valorfinal))
Por fim, o programa exibe o resultado para o usuário. A instrução print() exibe uma mensagem para o usuário, formatada com o valor atual do salário (salario) e o novo valor do salário após o aumento (valorfinal). O :.3f é utilizado para formatar o valor em 3 casas decimais.
