from classes.ninja import Ninja, Samurai, Ronin
from classes.pirate import Pirate, Bombadier, Captain

running = True

michelangelo = Samurai("Michelanglo")

jack_sparrow = Bombadier("Jack Sparrow")

def check_health():
    running = True
    if jack_sparrow.health <= 0:
        print("\nMichelangelo Wins\n")
        running = False
    elif michelangelo.health <= 0:
        print("\nJack Sparrow Wins\n")
        running = False
    return running


while running:
    jack_sparrow.attack(michelangelo)
    running = check_health()
    michelangelo.attack(jack_sparrow)
    running = check_health()

jack_sparrow.show_stats()
michelangelo.show_stats()