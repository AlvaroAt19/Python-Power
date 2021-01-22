# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 00:38:29 2020

@author: Alvaro
"""

from random import choice
from Animals import *
from tkinter import *
from PIL import ImageTk,Image


list_of_animals = [Dog(),Cat(),Pig(),Chicken(),Duck()]

root = Tk()
root.title('Guess the Animal')
root.iconbitmap('img/animal-ico.ico')
root.resizable(False,False)

img1 = Image.open('img/dog.jpg') #Opening the dog image
img1 = img1.resize((100,100),Image.ANTIALIAS) #Resizing
dog = ImageTk.PhotoImage(img1) #Converting to Tk

img2 = Image.open('img/cat.jpg') #Opening the cat image
img2 = img2.resize((100,100),Image.ANTIALIAS) #Resizing
cat = ImageTk.PhotoImage(img2) #Converting to Tk

img3 = Image.open('img/pig.jpg') #Opening the pig image
img3 = img3.resize((100,100),Image.ANTIALIAS) #Resizing
pig = ImageTk.PhotoImage(img3) #Converting to Tk

img4 = Image.open('img/chicken.jpg') #Opening the chicken image
img4 = img4.resize((100,100),Image.ANTIALIAS) #Resizing
chicken = ImageTk.PhotoImage(img4) #Converting to Tk

img5 = Image.open('img/duck.jpg') #Opening the duck image
img5 = img5.resize((100,100),Image.ANTIALIAS) #Resizing
duck = ImageTk.PhotoImage(img5) #Converting to Tk

img6 = Image.open('img/loose.jpg') #Opening the loose image
img6 = img6.resize((320,260),Image.ANTIALIAS) #Resizing
loose = ImageTk.PhotoImage(img6) #Converting to Tk

img7 = Image.open('img/win.jpg') #Opening the win image
img7 = img7.resize((320,260),Image.ANTIALIAS) #Resizing
win = ImageTk.PhotoImage(img7) #Converting to Tk


def game():
    """Game function"""
    global play
    play.destroy()
    
    global play_again
    if play_again:
        play_again.destroy()
    
    global play_label
    play_label.destroy()
    
    global close
    close.destroy()
    
    global counting #Number of 
    counting = 3

    global animal
    animal = choice(list_of_animals)
    
    global lb1
    lb1 = Label(root,text='It Sounds like ' + animal.sound())
    lb1.grid(row=0, column=0, columnspan=3)
    
    global lb2
    lb2 = Label(root, text='Its fisical characteristics is ' + animal.fisical())
    lb2.grid(row=1, column=0, columnspan=3)
    
    global btn1
    btn1 = Button(root,image=dog, command=lambda: choose('dog', counting)) #Defining dog button
    btn1.grid(row=2, column=0) #Putting on screen
    
    global btn2
    btn2 = Button(root,image=cat, command=lambda: choose('cat', counting)) #Defining cat button
    btn2.grid(row=2, column=1) #Putting on screen
    
    global btn3
    btn3 = Button(root,image=pig, command=lambda: choose('pig', counting)) #Defining pig button
    btn3.grid(row=2, column=2) #Putting on screen
    
    global btn4
    btn4 = Button(root,image=chicken, command=lambda: choose('chicken', counting)) #Defining chicken button
    btn4.grid(row=3, column=0) #Putting on screen
    
    global btn5
    btn5 = Button(root,image=duck, command=lambda: choose('duck', counting)) #Defining duck button
    btn5.grid(row=3, column=1) #Putting on screen
    
    
def choose(name, loose_counting):
    """Choose function to define the winning or loosing"""    
    if name != animal.name and loose_counting > 0:#Try again
        msg = 'Wrong choose, you still have ' + str(loose_counting) + ' attemps'
        global lb3
        if loose_counting < 3:
            lb3.destroy()
        lb3 = Label(root, text=msg)
        lb3.grid(row=4,column=0, columnspan=3)
        global counting
        counting -= 1
    
    elif name == animal.name:#Win
        #Destroying labels and buttons
        lb1.destroy()
        lb2.destroy()
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        btn5.destroy()
        if loose_counting < 3:
            lb3.destroy()
        
        win_label = Label(root, image=win)#Win image
        win_label.grid(rowspan=5,columnspan=3)
        
        close_game = Button(root,text='EXIT', command=exit)
        close_game.grid(row=5, column=1, ipadx = 40, ipady = 50)   
          
        global play_again
        play_again = Button(root,text='Play again', command=lambda:[game(), win_label.destroy(),close_game.destroy()])
        play_again.grid(row=5, column=0, ipadx = 30, ipady = 50)
        
       
                       
    else:#Loose
        #Destroying labels and buttons
        lb1.destroy()
        lb2.destroy()
        lb3.destroy()
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        btn5.destroy()

        loose_label = Label(root, image=loose)#Loose image
        loose_label.grid(rowspan=5,columnspan=3)
        
        close_game = Button(root,text='EXIT', command=exit)
        close_game.grid(row=5, column=1, ipadx = 40, ipady = 50)

        play_again = Button(root,text='Play again', command=lambda:[game(), loose_label.destroy(),close_game.destroy()])
        play_again.grid(row=5, column=0, ipadx = 30, ipady = 50)
        
        
        

play_label = Label(root, text='Do you wanna play Guess the Animal?')
play_label.grid(row=0, column=0, columnspan=3)

play_again = False
play = Button(root,text='YES', command=game) #starting game
play.grid(row=3, column=0, ipadx = 30, ipady = 50)

close = Button(root,text='NO', command=exit)
close.grid(row=3, column=1, ipadx = 30, ipady = 50)

root.mainloop()