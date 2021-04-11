# inheritance

class User():
    def __init__(self, email):
        self._email = email

    def signed_in(self):
        print('Logged in')


# encapsulation
class Wizard(User):  # inheritance
    def __init__(self, name, email, power):
        super().__init__(email)
        self._name = name  # abstraction
        self._power = power  # abstraction

    def attack(self):  # polymorphism
        print(f'Wizard {self._name} is attacking with a power of {self._power}')


class Archer(User):
    def __init__(self, name, num_arrow):
        self._name = name
        self._num_arrows = num_arrow

    def attack(self):  # polymorphism
        print(f'Archer {self._name} is attacking with {self._num_arrows} Arrows')


def char_player(char):
    char.signed_in()
    char.attack()


# instanciate
wiz1 = Wizard("merlin", "merlin@gmail.com", 20)
arch1 = Archer("robinhood", 100)

print(wiz1._email)
# polymorphism 1
char_player(wiz1)
char_player(arch1)

# polymorphism 2 using for loop

for char in [wiz1, arch1]:
    char.signed_in()
    char.attack()

