nome = input('Digite o nome do funcionario: ')
horas = int(input('Digite o numero de horas que esse funcionario trabalha por dia: '))
valor = int(input('Digite o valor que esse funcionario recebe por hora: '))

salario = (valor * horas)*24

print(nome)
print('O salario do funcionario e:', salario)
