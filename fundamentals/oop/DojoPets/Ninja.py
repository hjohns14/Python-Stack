from Pets import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet: Pet) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def display(self):
        for key, value in self.__dict__.items():
            print(key, value, sep=": ")

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()