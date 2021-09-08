class People():
    @staticmethod
    def factory(type):
        if type == "Ukrainian":
            return Ukrainian()
        if type == "American":
            return American()


class Ukrainian(People):
    def greeting(self):
        print("Привіт!")


class American(People):
    def greeting(self):
        print("Hello!")


obj = People.factory("Ukrainian")  # Create object using factory
obj.greeting()
