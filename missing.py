class DefaultDict2(dict):
    def __init__(self, default_factory=None, **kwargs):
        if default_factory and isinstance(default_factory(), list):
            self.default_factory = []
        elif default_factory and isinstance(default_factory(), dict):
            self.default_factory = {}
        else:
            self.default_factory = default_factory
    def __missing__(self, key):
        return self.default_factory

d = DefaultDict2(list)
# d['name']['age'] = 20
d['name'].append('20')
print(d['name'])

