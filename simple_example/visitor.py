class PersonVisitor(object):
    def say(self, person):
        methods = {
            Ukrainian: self.say_ukrainian,
        }

        say = methods.get(type(person), self.say_unknown)
        say(person)

    def say_ukrainian(self, person):
        print('Привіт!')

    def say_unknown(self, person):
        print('Hello!')


class Person(object):
    "Person"

    def say(self, visitor):
        visitor.say(self)


class American(Person):
    "American"


class Ukrainian(Person):
    "Ukrainian"


class Italian(Person):
    "Italian"


visitor = PersonVisitor()
ukrainian = Ukrainian()
ukrainian.say(visitor)
american = American()
american.say(visitor)
italian = Italian()
italian.say(visitor)
