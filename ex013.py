salario = float(input('Qual é o salário do funcionário? R$'))
novoSalario = salario + (salario*15/100)
print('O salário de R${:.2f} com 15% de aumento será R${:.2f}'.format(salario, novoSalario))