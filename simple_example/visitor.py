class PersonVisitor():
    def say(self, person):
        methods = {
            Ukrainian: self.say_ukrainian,
        }

        say = methods.get(type(person), self.say_unknown)
        say()

    def say_ukrainian(self):
        print('Привіт!')

    def say_unknown(self):
        print('Hello!')


class Person():
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
