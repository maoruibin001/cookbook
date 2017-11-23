class Hello:
    def __init__(self, name):
        print('hello world')
        self.name = name
    def sayName(self):
        print(self.name)

hello = Hello('maoruibin')

print(hello.name)

hello.sayName()
