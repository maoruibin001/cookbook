from operator import itemgetter
a = [{'age': 1, 'name': 3},{'age': 1, 'name': 2}, {'age': 4, 'name': 2}, {'age': 3, 'name': 8}]
print(sorted(a, key=itemgetter('age', 'name')))

for ages, item in a:
    print(item)

# b = {'name': 'maoruibin'}
#
# print(b['name'])