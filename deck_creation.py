import random as random


class Character:

    def __init__(self, name, health, attack, element):
        self.name = name
        self.health = health
        self.attack = attack
        self.element = element

    '''def isDead(self,character):
        if character.health <= 0:
            return True
        else:
            return False'''


def choose_element():
    element_list = ['Fire', 'Water', 'Ice', 'Grass', 'Death', 'Steel', 'Shadow']
    return random.choice(element_list)

# We can turn this into spells or something later




# Could we also use a for loop and random generate attack and defense values?

chars1 = Character('Warrior', 100, 25, choose_element())
chars2 = Character('Assassin', 70, 30, choose_element())
chars3 = Character('Thief', 70, 20, choose_element())
chars4 = Character('Necromancer', 120, 15, choose_element())
chars5 = Character('Charmer', 100, 20, choose_element())
chars6 = Character('Berserker', 125, 30, choose_element())
chars7 = Character('Archer', 50, 50, choose_element())
chars8 = Character('Knight', 150, 20, choose_element())
chars9 = Character('Lancer', 200, 15, choose_element())
chars10 = Character('Juggernaut', 200, 30, choose_element())

char_list = [chars1, chars2, chars3, chars4, chars5, chars6, chars7, chars8, chars9, chars10]

# Assign elements/types randomly or we can keep them fixed,
