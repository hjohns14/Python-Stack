from Pets import Cat, Dog, Capybara
from Ninja import Ninja

# Creating Pets First
prismo = Cat("Prismo", "Tuxedo", ["Sleep", "Loaf"], 90, 15)
chai = Cat("Chai", "Torbie", ["Expert huntress", "Long Jump", "High Jump", "Vocalist"], 95, 100)
tucker = Dog("Tucker", "Miniature Weiner Dog", "Beg", 75, 50)
belle_la_roux = Dog("Belle La Roux", "Yellow Lab", ["Fetch", "Sit", "Stay", "Mark", "Lay"], 85, 150)
jimmy = Capybara("Cappy-tain America", "The big ones", "Be cute", 100, 60)

hunter = Ninja("Hunter", "Johns", 10, 50, chai)
hunter.feed()
hunter.walk()
hunter.bathe()
print(chai.health)

brooke = Ninja("Brooke", "Rock", 5, 10, tucker)
brooke.feed()
brooke.walk()
brooke.bathe()
print(tucker.health)



