student = {
    'mao': 30,
    'rui': 27,
    'bin': 33,
    'ou': 35,
    'chuan': 67,
    'yu': 12
}
name = {'mao', 'rui', 'bin'}
ret = dict((key, value) for key, value in student.items() if value >= 30 and key in name)

print(ret)
