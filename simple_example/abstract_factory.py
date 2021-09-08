from abc import ABCMeta


# Abstract Factory
class StandardFactory():

    @staticmethod
    def get_factory(country):
        if country == 'Ukraine':
            return UkraineFactory()
        elif country == 'USA':
            return USAFactory()
        raise TypeError('Unknown Factory.')


# Factory
class UkraineFactory():
    def get_site(self):
        return Grammarly()


class USAFactory():
    def get_site(self):
        return Amazon()


# Product Interface
class Website():
    __metaclass__ = ABCMeta

    def achievement(self):
        pass


# Products
class Grammarly():
    def achievement(self):
        print('Grammarly is Ukrainian site!')


class Amazon():
    def achievement(self):
        print('Amazon is USA site!')


if __name__ == "__main__":
    factory = StandardFactory.get_factory('Ukraine')
    site = factory.get_site()
    site.achievement()

    factory = StandardFactory.get_factory('USA')
    site = factory.get_site()
    site.achievement()
