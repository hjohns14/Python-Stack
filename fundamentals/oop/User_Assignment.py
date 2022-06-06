from importlib.util import spec_from_file_location


class User:
    def __init__(self, first_name, last_name, email, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        for key, value in self.__dict__.items():
            print(key, value, sep=": ")
        return self

    def enroll(self):
        if self.is_rewards_member:
            print("Already a Member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    
    def spend_points(self, amount):
        if self.gold_card_points - amount > 0:
            self.gold_card_points -= amount
        else:
            print(f"{self.first_name} does not have enough Points!")
        return self


user1 = User("Hunter", "Johns", "email@email.com", 27)
user2 = User("Steve", "Rogers", "hailhydra15@email.com", 105)
user3 = User("Thanos", None, "snap@glovemail.com", 1000)


user1.enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
user3.display_info().spend_points(40)