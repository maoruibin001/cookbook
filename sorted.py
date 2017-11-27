from operator import itemgetter
from itertools import groupby
rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003, 'date1': '07/04/2012'},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002, 'date1': '07/03/2012'},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001, 'date1': '07/02/2012'},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004, 'date1': '07/04/2012'}
]
# print(sorted(rows, key=lambda x: x['lname']))
# rows = sorted(rows, key=itemgetter('date1'))
rows.sort(key=itemgetter('date1'))

print(rows)

for date, items in groupby(rows, key=itemgetter('date1')):
    print(date)
    for i in items:
        print(' ', i)