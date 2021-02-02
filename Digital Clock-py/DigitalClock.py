# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:14:55 2021

@author: Alvaro Alves Travessa
"""
from tkinter import *
from threading import Thread
import time


class digitalClock:
    """Simple digital clock, with timer"""
    def __init__ (self, clock, time='' ):
        self.clock = clock #Label
        self.time = time #time string for initializing the time.
 
    
    def tick(self):
        """Updates the clock display"""
        self.time = time.strftime('%H:%M:%S') #Get the atual time
        self.clock.configure(text=self.time) #Atualize the label        
        self.clock.after(1000, self.tick) # calls itself every 1000 milliseconds to update the time display as needed 
         

    def tickDown(self):
        """Starts a count down from the number of seconds set to zero."""
        global start_flag
        global e1 #tickDown entry
        global pause_flag 
        if start_flag: #Starting(start button)
            if not pause_flag: #pause_flag == False
                try:
                    self.secs = int(e1.get()) #Reading the entry 
                except:
                    self.clock.after(1, self.tickDown)
                    start_flag = False #When e1.get() is not int, stop the count
                else:
                    if self.secs > 0:
                        self.secs -= 1
                        self.clock.delete(0,END)
                        self.clock.insert(0,self.secs)
                        self.clock.after(1000, self.tickDown)
                    else:
                        self.secs = 'TIME OVER'
                        self.clock.delete(0,END)
                        self.clock.insert(0,self.secs)
                        start_flag = False #tickDown over 
                        self.clock.after(1, self.tickDown)
            else: #pause_flag == True (pause button)
                self.clock.after(1000, self.tickDown)
        else: #start_flag == False
            self.clock.after(1, self.tickDown)
 
             
class makeThread (Thread):
    """Creates a new thread."""
    def __init__ (self,func):
        Thread.__init__(self)
        self.__action = func#function to be executed in this thread.
        self.debug = False


    def run (self):
        """Method representing the thread's activity."""
        if ( self.debug ): print ("Thread begin")
        self.__action()
    

root = Tk()
root.title('Digital Clock')
root.resizable(False,False)
root.iconbitmap('clock-ico.ico')

aLabel = Label(root, font=('times 28', 20, 'bold'), bg='green')#Time label
aLabel.grid(row=0, column=0, columnspan=3, ipadx=94, ipady=10)

e1 = Entry(root, font=('times 28', 20, 'bold'), bg='red')#TickDown entry
e1.grid(row=1, column=0, columnspan=3, ipadx=0, ipady=10)

d = digitalClock(aLabel)#Time Clock(tick)
t = makeThread(d.tick)
t.start()

d2 = digitalClock(e1)#Timer Clock(tickDown)
t2 = makeThread(d2.tickDown)


start_flag = False
def start():
    """Starts digitalClock tickDown"""
    global start_flag
    start_flag = True


t2.start()#Calls d2.tickDown()
btn1 = Button(root, text='Start', command=start)#Start button
btn1.grid(row=2,column=0, ipadx=30, ipady=10)


pause_flag = False
def pause():
    """Pauses digitalClock tickDown"""
    global pause_flag #flag
    if pause_flag:
        pause_flag = False
    else:
        pause_flag = True


btn2 = Button(root, text='Pause', command=pause)#Pause button
btn2.grid(row=2,column=2, ipadx=30, ipady=10)


def sec_30():
    """Add 30 secs to tickDown entry"""
    global e1 #tickDown entry
    try:
        sec = int(e1.get())
    except:
        sec = 0
    e1.delete(0,END) #Deleting old
    sec += 30
    e1.insert(0,sec) #Inserting new


btn3 = Button(root, text='+30s', command=sec_30)#+30sec button
btn3.grid(row=2,column=1, ipadx=30, ipady=10)

root.mainloop()
