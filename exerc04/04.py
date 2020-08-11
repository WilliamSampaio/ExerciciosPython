import os

salarioLiqMensal = float(input('Salário liquido mensal: '))
percentualReajuste = float(input('Percentual de reajuste em %: '))

novoSalario = salarioLiqMensal + (salarioLiqMensal / 100 * percentualReajuste)

print(f'Novo Salário: R${round(novoSalario, 2)}')

os.system('pause')