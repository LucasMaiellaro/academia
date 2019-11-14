quantidade = float(input('Digite a quantidade de numeros: '))
i = 0 
soma = 0

while i <  quantidade:
    numero = float(input('Digite o numero: '))
    soma = soma + numero
    i = i + 1

media = soma / quantidade
print('A media e:', media)