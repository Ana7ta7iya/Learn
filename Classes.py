def print_test():
    print('lets test begin')
    i = 5
    a = i -2
    print(a)
    print('this is our TEST!')
#def main():
#   print('this is main')

print('this is script')
print_test()

def print_test(var1):
    print('lets test begin')
    print(var1)
    print('this is our TEST!')
print('this is script')
print_test([1, 2, 3])

def print_test(var1):
    print('lets test begin')
    res = var1 + 2
    print(var1)
    print('this is our TEST!')
print('this is script')
print_test(7)

def print_test(var1):
    print('lets test begin')
    res = var1 + 2
    print(res)
    print('this is our TEST!')
def print_default_value(var1=9):
    print('lets test begin')
    res = var1 + 2
    print(res)
    print('this is our TEST!')
print('this is script')

print_test(5)
print_default_value()


def print_test(var1):
    print('lets test begin')
    res = var1 + 2
    print(res)
    print('this is our TEST!')
def print_default_value(var1=9):
    print('lets test begin')
    res = var1 + 2
    print(res)
    print('this is our TEST!')

def print_multiple_value(var1, var2):
    print('lets test begin')
    res = var1 + var2
    print(res)
    print('this is our TEST!')
print('this is script')

print_test(5)
print_multiple_value(7, 3)


def print_multiple_value(var1, var2 = 6):
    print('lets test begin')
    res = var1 + var2
    print(res)
    print('this is our TEST!')
print('this is script')

print_test(5)
print_default_value(22)
print_multiple_value(34, 8)


def print_multiple_value_order(var1, var2 = 'default'):
    print('lets test begin')
    print(var1 + 1)
    print(var2 + 'value!')
    print('this is our TEST!')
print('this is script')

print_test(5)
print_default_value(22)
print_multiple_value(34, 8)
print_multiple_value_order(3)


def calc_val(var1, var2 = 2):
    summ = var1 + var2
    print(var1)
    print(var2)
    print(summ)
    return summ
calc_val(1)
result = calc_val(1)
print('result = {}'.format(result))

#CLASSES 2

class OurFirstClass:

    def say_hello(self):
        print('my first class!')
    def say_hi(self, name):
        print('Hi {}'.format(name))

print('Not a class')

obj = OurFirstClass()
print(obj.__class__)

obj.say_hello()
obj.say_hi('Everyone')

#CLASSES 11/11
#1
class OurFirstClass:

    def __init__(self):
        self.name = 'Your First Class'

    def say_hello(self):
        print(self.name)

    def say_hi(self, name):
        print('Hi {}'.format(name))

print('Not a class')

obj = OurFirstClass()
print(obj.__class__)
obj2 = OurFirstClass

obj.say_hello()
obj2.say_hello()
obj.name = 'Another Name'
obj.say_hello()
obj2.say_hello()

obj.say_hi('Everyone')

#2
class OurFirstClass:

    def __init__(self):
        self.name = 'Your First Class'
        self.color = None

    def _internal_method(self):
        pass

    @classmethod
    def say_hello(self):
        print(self.name)
        if self.color:
            print('color: {}'.format(self.color))

    def say_hi(self, name):
        print('Hi {}'.format(name))

    def use_class_method(self):
        self.say_hello()

    def set_name(self, name):
        self.name = name

print('Not a class')

obj = OurFirstClass()
print(obj.__class__)
obj2 = OurFirstClass
obj2.set_name()

#3
class OurFirstClass:

    def __init__(self, nick='Your First Class', color=None):
        self.name = nick
        self.color = color

    def _internal_method(self):
        pass

    # @classmethod
    # def say_hello(self):
    #     print(self.name)
    #     if self.color:
    #         print('color: {}'.format(self.color))
    #

    def say_hi(self, name):
        print('Hi {}'.format(name))

    def use_class_method(self):
        self.say_hello()

    def set_name(self, name):
        self.name = name

obj = OurFirstClass()
print(obj.__class__)
obj2 = OurFirstClass('magic')

#4
class OurFirstClass:

    def __init__(self, nick='Your First Class', color=None):
        self.name = nick
        self.color = color

    def _internal_method(self):
        pass

    def say_hi(self, name):
        print('Hi {}'.format(name))

    def use_class_method(self):
        self.say_hello()

    def set_name(self, name):
        self.name = name

    def main(self):
        print('main in charge')

obj = OurFirstClass()
print(obj.__class__)
obj2 = OurFirstClass('magic')

obj.main()



