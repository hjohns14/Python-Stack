from random import randint


class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 10
        self.health = 100
        self.attack_log = []
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nAttack Log{self.attack_log} \n")

    def attack( self , pirate):
        speed_roll = randint(1, 20) + self.speed > 18
        attack = self.strength * randint(1,20) / 20
        pirate.health -= attack
        self.attack_log.append(attack)
        if speed_roll:
            print(f"Double Attack from {self.name}")
            attack = self.strength * randint(1,20) / 20
            pirate.health -= self.strength + randint(1,20)
            self.attack_log.append(attack)
        return self

class Samurai(Ninja):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 20
        self.health = 120
        self.speed = 7

class Ronin(Ninja):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 15
        self.speed = 14
        self.health = 45