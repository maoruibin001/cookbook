from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['name', 'age'])

ret = Subscriber('mao', 20)

class A(dict):
    age = 333
    def __init__(self, default_factory=None, **kwargs):
        self.age = 20
        if default_factory and isinstance(default_factory(), list):
            self.default_factory = []
        elif default_factory and isinstance(default_factory(), dict):
            self.default_factory = {}
        else:
            self.default_factory = default_factory
    def __missing__(self, key):
        return self.default_factory
a = A()
print(a['age'])


cc = dict([('name', 20), ('age', 30)])
print(cc)