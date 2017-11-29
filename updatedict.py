a = {'x': 20, 'y': 30}
b = {'x': 30, 'z': 50}

z = dict(a)
z['x'] = 30
print(a)

class A :
    def __init__(self):
        pass

print(dir(A.__class__.__getattribute__))