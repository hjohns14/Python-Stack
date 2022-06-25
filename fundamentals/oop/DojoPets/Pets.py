class Pet:
    def __init__(self, name, type, tricks, health, energy) -> None:
        self.type = type
        self.name = name
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25

    def play(self):
        self.health += 5

    def eat(self):
        print(f"{self.name} is eating")
        self.energy += 5
        self.health += 10

    def noise(self):
        print(f"{self.name} is being bathed")

class Cat(Pet):
    def __init__(self, name, type, tricks, health, energy) -> None:
        super().__init__(name, type, tricks, health, energy)

    def play(self):
        super().play()
        print(f"You try to walk your cat but everyone knows that is not how cats work.\nYou end up dangling a string in front of {self.name} for an hour. They love it.")

    def noise(self):
        super().noise()
        print("YOOOOWWWLL --(Translation: You will regret this decision for the rest of your days.")

class Dog(Pet):
    def __init__(self, name, type, tricks, health, energy) -> None:
        super().__init__(name, type, tricks, health, energy)

    def play(self):
        super().play()
        print(f"Dog. Love Walk. \nS tier Walk in {self.name}'s opinion")

    def noise(self):
        super().noise()
        print("Woof --(Translation: You're The best)")

class Capybara(Pet):
    def __init__(self, name, type, tricks, health, energy) -> None:
        super().__init__(name, type, tricks, health, energy)

    def play(self):
        super().play()
        print(f"{self.name} looks at you unsure but is happy anyway.")

    def noise(self):
        super().noise()
        print("Chirp --(Unable to translate)")
