from importlib.util import spec_from_file_location


class User:
    def __init__(self, first_name, last_name, email, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self) -> None:
        for key, value in self.__dict__.items():
            print(key, value, sep=": ")

    def enroll(self) -> bool:
        if self.is_rewards_member:
            print("Already a Member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
    
    def spend_points(self, amount) -> None:
        if self.gold_card_points - amount > 0:
            self.gold_card_points -= amount
        else:
            print(f"{self.first_name} does not have enough Points!")


user1 = User("Hunter", "Johns", "email@email.com", 27)
user2 = User("Steve", "Rogers", "hailhydra15@email.com", 105)
user3 = User("Thanos", None, "snap@glovemail.com", 1000)


user1.enroll()
user1.spend_points(50)
user2.enroll()
user2.spend_points(80)


user1.display_info()
user2.display_info()
user3.display_info()

user3.spend_points(40)