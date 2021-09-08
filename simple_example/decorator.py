class Person():
    def __init__(self, name):
        self._name = name

    def say(self):
        print('Привіт! Я %s!' % self._name)


class Ukrainian():
    def __init__(self, man):
        self._person = person

    def __getattr__(self, item):
        return getattr(self._person, item)

    def go_to(self):
        print('%s хоче відвідати Америку' % self._person._name)


person = Person('Іван')
person_ukrainian = Ukrainian(person)
person_ukrainian.say()
person_ukrainian.go_to()
