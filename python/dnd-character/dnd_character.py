from numpy.random import randint

class Character:
    def __init__(self):
        self.strength = set_ability()
        self.dexterity = set_ability()
        self.constitution = set_ability()
        self.intelligence = set_ability()
        self.wisdom = set_ability()
        self.charisma = set_ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return randint(3, 19)

def modifier(constitution):
    return ((constitution - 10) // 2)

def set_ability():
    return randint(3, 19)