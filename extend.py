class Parent:
    def __init__(self):
        self.name = 'maoruibin'

    def say(self):
        print('say hello')

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.age = 20

child = Child()
print(dir(child))