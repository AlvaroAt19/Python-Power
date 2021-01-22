# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 00:55:49 2020

@author: Alvaro
"""

#Each animal will be a class, and each will have 2 characteristics
#Sound make and a fisical characteristics

class Dog:
    def __init__(self):
        self.name = 'dog'
    def sound(self):
        return 'ow! ow!'
    def fisical(self):
        return 'Fur'

class Cat:
    def __init__(self):
        self.name = 'cat'
    def sound(self):
        return 'meowth! meowth!'
    def fisical(self):
        return 'Fur'

class Pig:
    def __init__(self):
        self.name = 'pig'
    def sound(self):
        return 'oink! oink!'
    def fisical(self):
        return 'Fat'

class Chicken:
    def __init__(self):
        self.name = 'chicken'
    def sound(self):
        return 'popó! popó!'
    def fisical(self):
        return 'Feathers'

class Duck:
    def __init__(self):
        self.name = 'duck'
    def sound(self):
        return 'quack! quack!'
    def fisical(self):
        return 'Feathers' 