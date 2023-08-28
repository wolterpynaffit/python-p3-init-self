#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed='Mutt'):
        self.breed = breed
        self.name = name

    def bark(self):
        print('Woof!')

    def get_adopted(self, owner):
        self.owner = owner
        print(self.owner)


fido = Dog('Snoopy')
fido.get_adopted("Tim")
fido.owner
