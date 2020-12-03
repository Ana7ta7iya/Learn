from Animals import Animals

class Cat(Animals):

    def __init__(self):
        super(Cat, self).__init__()
        self.size = 'small'

    def say(self):
        super().say()
        print('Miu')

    def eat(self):
        print('mouse')

    def print_size(self):
        print(self.size)

cat = Cat()

cat.say()
cat.eat()
cat.print_size()
print(cat.skin)

cat.skin = 'fur'

cat2 = Cat()
cat2.size = 'medium'
cat2.skin = 'bold'

obj_list = [Animals(), cat, cat2]

for current_obj in obj_list:
    print('current animal are {} size and {}'.format(current_obj.size, current_obj.skin))
