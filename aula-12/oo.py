class Mamiferos():
    olhos = 2
    patas = 4

    def __init__(self, pelo, especie, rabo, cor):
        self.pelo = pelo
        self.especie = especie
        self.rabo = rabo
        self.cor = cor

    def comer(self):
        print('Comi')
    
    def fazer_som(self):
        print('SOM')

mamifero = Mamiferos('curto','doguinhos caninos', True, 'caramelo')
mamifero2 = Mamiferos('longo', 'agrarios monata', False, 'purple')

mamifero.comer()
mamifero2.fazer_som()   
print(mamifero.especie)
print(mamifero2.especie)