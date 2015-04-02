#Import the required libraries or modules

import graphics

from graphics import *
from random import randint
from random import shuffle
import random

#Creates random integers for each colour, between 0, 255

blue = randint(0,255)
green = randint(0,255)
red = randint(0,255)

#Creates random integers for x and y. Set it between 20, 450 as this minimizes the risk of certain elements not fitting on the 'canvas'

x = randint(20,450)
y = randint(30,440)

data = []

# Read in and print out the data in the data file

window = GraphWin("Visualisation", 500, 500)
datafile = open("data.txt",'r')


for line in datafile: 
    data.append(line)
    
#Shuffles the data in the array around
    shuffle(data)

#'mark' represents each float within the data array.
#Each time the code is run a different mark it shown at the points 420, 420.
#Is set to the text size of 20, font arial and is bold
#Prints all the marks out so that all the data can be seen. 

for mark in data:
    text = Text(Point(420,420),mark)
    text.setSize(20)
    text.setFace('arial')
    text.setStyle('bold')
    text.setTextColor(color_rgb(blue, green, red))
    print(mark)

#For loop that creates circles based upon the data in the array.
#The circles are given random x and y coordinates.
#Float - the floats in the data create the size of the circle. 

for i in range(0, len(data)):
    ball = Circle(Point(x,y), float(data[i]))
    ball.setFill(color_rgb(red, green, blue))
    ball.draw(window)

    
text.draw(window)

# Waits until the mouse is clicked before closing the window
window.getMouse()
