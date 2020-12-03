class Animals:

    def __init__(self):
        self.size = 'any'
        self.skin = 'any'

    def eat(self):
        print('food')

    def say(self):
        print('voice')

animal = Animals()

animal.say()
animal.eat()