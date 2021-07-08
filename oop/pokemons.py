#1. Crear clase Pokemon con los siguientes atributos y métodos
# types: fire, grass, water
# name
# type
# HP
# attacks []
# Métodos: learn_attack, attack, receive_damage

elements = ["fire", "grass", "water"]

class Pokemon:

    def __init__(self, name, element, HP):
        self.name = name
        self.element = element
        self.HP = HP
        self.attacks = []

    def __str__(self):
        return f"name: {self.name}\ntype: {self.element}\nHP: {self.HP}\nattacks: {self.attacks}"

    def learn(self, attack): ## un método que permite agregar un ataque. Tiene que ser un método de instancia. Este método permite aprender un ataque y esto lo mete en la porpiedad de ataques un objeto de ataque
        self.attacks.append(attack)
        

class Attack:
    def __init__(self, name, element, damage):
        self.name = name
        self.element = element
        self.damage = damage
        
    def __str__(self):  #Cuando el usuario vea los ataques, con esto sólo le aparece el nombre. Modificación del str de la línea 19
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"    

charmander = Pokemon("Charmander", elements[0], 120)
squirtle = Pokemon("Squirtle", elements[2], 140)
bulbasaur = Pokemon("Bulbasaur", elements[1], 160)




# print(charmander) # este print llama a un metodo especial que se llama __str__ en la línea 19
# print(squirtle)
# print(bulbasaur)

flamethrower = Attack("Flamethrower", elements[0], 40)
razor_leaf = Attack("Razor leaf", elements[1], 25)
surf = Attack("surf", elements[2], 35)
charmander.learn(flamethrower) #Charmander ha aprendido a usar el lanzallamas, usando el str de la línea 32
charmander.learn(razor_leaf)
charmander.learn(surf)


print(charmander)