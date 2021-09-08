class Ukrainian(object):
    def __init__(self, name):
        self._name = name

    def greeting(self):
        return '%s: Привіт!' % self._name


class American(object):
    def __init__(self, name):
        self._name = name

    def live_in(self):
        return '%s: I live in America' % self._name


class AmericanAdapter(Ukrainian):
    def __init__(self, name):
        super(AmericanAdapter, self).__init__(name=name)
        self._american = American(name=name)

    def greeting(self):
        return self._american.live_in()


person = Ukrainian('Ivan')
print(person.greeting())
person = AmericanAdapter('Joe')
print(person.greeting())
