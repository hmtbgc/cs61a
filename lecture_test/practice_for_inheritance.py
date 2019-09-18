class animal:

    def __init__(self, name, owner_name):
        self.name = name
        self.owner_name = owner_name

    def speak(self, content):
        print(content + '!')

class Dog(animal):

    legs = 4

    def fetch(self, item):
        print('I fetched' + ' ' + str(item))

    def speak(self):
        animal.speak(self, 'woof')

class Chicken(animal):

    legs = 2

    def speak(self):
        animal.speak(self, 'cluck')

class GoldenRetriever(animal):

    legs = 4

    def fetch(self, item):
        print('I fetched' + ' ' + str(item))

    def speak(self):
        animal.speak(self, 'woof')
