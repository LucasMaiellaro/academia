nome = input("Digite o seu nome: ").lower()
idade = int(input("Digite sua idade: "))

if nome == "pedro" and idade == 22 or nome == "drake":
    print("Salve Drake")
elif nome == ("Murilo"):
    print("Salve henrique henrique")
else:
    print("Voce nao e o Drake")

numero = 0 
while numero < 5:
    print(numero)
    numero = numero + 1

lista = ['cubo magico', 'pagode japones', 'skate', 'manga com leite']

# for item in lista:
#     print(item)

# for i in range(0, len(lista), 2):
#     print(lista[i])

for i in range(len(lista)-1, 0, -2):
    print(lista[i])
    