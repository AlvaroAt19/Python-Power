# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 00:55:49 2020

@author: Alvar
"""

#Each animal will be a class, and each will have 2 characteristics
#Sound make and a fisical characteristics

class Dog:
    def __init__(self):
        self.name = 'dog'
    def sound(self):
        print('ow! ow!')
    def fisical(self):
        print('Fur')

class Cat:
    def __init__(self):
        self.name = 'cat'
    def sound(self):
        print('meowth! meowth!')
    def fisical(self):
        print('Fur')

class Pig:
    def __init__(self):
        self.name = 'pig'
    def sound(self):
        print('oink! oink!')
    def fisical(self):
        print('Fat')

class Chicken:
    def __init__(self):
        self.name = 'chicken'
    def sound(self):
        print('popó! popó!')
    def fisical(self):
        print('Feathers')

class Duck:
    def __init__(self):
        self.name = 'duck'
    def sound(self):
        print('quack! quack!')
    def fisical(self):
        print('Feathers')