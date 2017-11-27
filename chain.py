from collections import ChainMap

a = {'name': 'mao', 'age': 20}
b = {'t': '33', 'age': 55}
c = {'age': 33, 't': 22}

z = ChainMap({}, a, b)

z['name'] = 'rui'
b['t'] = 35
print(z)
print(z['t'])
