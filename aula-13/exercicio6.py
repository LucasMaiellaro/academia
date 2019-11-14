class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
pessoa = Pessoa('Lucas', 17)
print(pessoa.nome)
print(pessoa.idade)

class Pet():
    def __init__(self, nome, nome_do_dono, cor, pelos):
        self.nome = nome
        self.nome_do_dono = nome_do_dono
        self.cor = cor
        self.pelos = pelos

pet = Pet('Doguinho', 'Lucas', 'Marrom', 'Longos')
print(pet.nome)
print(pet.nome_do_dono)
print('==========TODOS OS ATRIBUTOS DO PET=========')
print(pet.nome)
print(pet.nome_do_dono)
print(pet.cor)
print(pet.pelos)

