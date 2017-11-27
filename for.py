rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003, 'date1': '07/04/2012'},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002, 'date1': '07/03/2012'},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001, 'date1': '07/02/2012'},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004, 'date1': '07/04/2012'}
]

l = [n for n in rows if n['uid'] > 1002]

print(l)
#
# l2 = list(n for n in rows if n['uid'] > 1002)
#
# print(l2)

# for item in l2:
#     print(item)


# l3 =filter(lambda x: x['uid'] > 1002, rows)
#
# for item in l3:
#     print(item)
# print(l3)