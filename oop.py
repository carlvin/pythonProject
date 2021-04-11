# OOP

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'
player1 = PlayerCharacter('carly', 4)
player2 = PlayerCharacter('George', 57)

player2.attack = 50

print(player1.name)
print(player2.age)

print(player1.run())
print(player2.attack)

print(player1.membership)
print(player2.membership)
