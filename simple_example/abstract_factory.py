from abc import ABCMeta


# Abstract Factory
class StandardFactory(object):

    @staticmethod
    def get_factory(country):
        if country == 'Ukraine':
            return UkraineFactory()
        elif country == 'USA':
            return USAFactory()
        raise TypeError('Unknown Factory.')


# Factory
class UkraineFactory(object):
    def get_site(self):
        return Grammarly()


class USAFactory(object):
    def get_site(self):
        return Amazon()


# Product Interface
class Website(object):
    __metaclass__ = ABCMeta

    def achievement(self):
        pass


# Products
class Grammarly(object):
    def achievement(self):
        print('Grammarly is Ukrainian site!')


class Amazon(object):
    def achievement(self):
        print('Amazon is USA site!')


if __name__ == "__main__":
    factory = StandardFactory.get_factory('Ukraine')
    site = factory.get_site()
    site.achievement()

    factory = StandardFactory.get_factory('USA')
    site = factory.get_site()
    site.achievement()
