# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 00:38:29 2020

@author: Alvar
"""

from random import choice
from Animals import *

list_of_animals = [Dog(),Cat(),Pig(),Chicken(),Duck()]

def main():
    animal = choice(list_of_animals)
    
    print("\nIt's sound like: ")
    animal.sound()
    
    print("And have the following characteristic: ")
    animal.fisical()
    
    print('You have 3 attempts')
    att = 3
    
    while att != 0:
        ans = input("What animal is it?\n")
        if ans.lower() == animal.name:
            return 'YOU WIN!!!!'
        else:
            att -= 1
            if att == 0:
                pass
            else:
                print('You have ' + str(att) + ' attempts')
    return 'YOU LOOOOSE!!!! \nThe correct answer is: ' + animal.name.upper()

if __name__ == '__main__':
    print('='*70)
    print ('-'*27 + 'GUESS THE ANIMAL' + '-'*27)
    while True:
        game = input('Do you wanna play? \nAnswer with Y or N: ')
        
        if game.lower() == 'n':
            print('See ya!!!')
            exit()
        
        elif game.lower() == 'y':
            print(main())
        
        else:
            print('You made a mistake, try again! ')

