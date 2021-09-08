class Regions():
    def __init__(self, country):
        self._country = country

    def get_regions(self):
        return '%s has 25 regions!' % self._country


class States():
    def __init__(self, country):
        self._country = country

    def get_states(self):
        return '%s: has 50 states' % self._country


class USAAdapter(Regions):
    def __init__(self, country):
        super(USAAdapter, self).__init__(country=country)
        self._states = States(country=country)

    def get_regions(self):
        return self._states.get_states()


class UkraineAdapter(States):
    def __init__(self, country):
        super(UkraineAdapter, self).__init__(country=country)
        self._regions = Regions(country=country)

    def get_states(self):
        return self._regions.get_regions()


person = UkraineAdapter('Ukraine')
print(person.get_states())
person = USAAdapter('USA')
print(person.get_regions())
