from collections import defaultdict

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003, 'date1': '07/04/2012'},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002, 'date1': '07/03/2012'},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001, 'date1': '07/02/2012'},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004, 'date1': '07/04/2012'}
]

rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row['date1']].append(row)

print(dir(rows_by_date))