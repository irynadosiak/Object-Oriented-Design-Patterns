class Subject():
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):  # підписатись на сповіщення
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):  # відписатись на сповіщення
        self._observers.discard(observer)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):  # повідомити всіх про сповіщення
        for observer in self._observers:
            observer.update(data)


class ObserverBase():
    @staticmethod
    def update(self, data):
        pass


class Observer(ObserverBase):
    def __init__(self, name):
        self._name = name

    def update(self, data):
        print('To %s: %s' % (self._name, data))


subject = Subject()
subject.attach(Observer('Ivan'))
subject.attach(Observer('David'))
subject.set_data('Good morning! You will receive a message twice a week.')
