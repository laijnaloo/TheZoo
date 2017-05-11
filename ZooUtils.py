__author__ = 'Lina Andersson'
# Programmeringsteknik webbcourse KTH P-task.
# Lina Andersson
# 2016-03-29
# Program for a zoo where the user can search, sort, buy, sell and get recommendations on what to buy or sell.
# This file contains helpclasses that occurs in the other files and is one of five modules in this program.

from tkinter import *
from PIL import ImageTk, Image

#Class for labels behind animal picture/objects
class AnimalLabel:
    def __init__(self, anAnimal, imageName):
        #animal picture
        self.anAnimal = anAnimal
        self.img = Image.open(imageName)
        self.tkImg = ImageTk.PhotoImage(self.img)

    def addAsLabel(self, tkRoot, row, column, event = lambda X: None):
        #creates a label with image and adds it too root
        self.imgLabel = Label(tkRoot, image = self.tkImg, borderwidth = 0)
        self.imgLabel.bind("<Button-1>", event)
        self.imgLabel.place(x = row, y = column)

        #if no animal - make black square
        if self.anAnimal != None:
            self.anAnimal.addAsLabel(tkRoot, row, column, event)

#Class for animal objects
class Animal:
    def __init__(self, name, age, species, gender):
        self.name = name
        self.age = age
        self.species = species
        self.gender = gender

        #creates picture of animal
        nameImage = self.species + ".png"
        self.img = Image.open(nameImage)
        self.tkImg = ImageTk.PhotoImage(self.img)

    #creates a label with image and adds animal to label
    def addAsLabel(self, tkRoot, row, column, event = lambda X: None):
        self.imgLabel = Label(tkRoot, image = self.tkImg, borderwidth = 0)
        self.imgLabel.bind("<Button-1>", event)
        self.imgLabel.place(x = row + 3, y = column + 3)

#class for buttons in the program
class MyButton:
    def __init__(self, name):
        self.name = name

        nameImage = self.name + ".png"
        self.img = Image.open(nameImage)
        self.tkImg = ImageTk.PhotoImage(self.img)

    #creates a label with image and adds it too root
    def addAsLabel(self, tkRoot, xPosition, yPosition, event = lambda X: None):
        self.imgLabel = Label(tkRoot, image = self.tkImg, borderwidth = 0)
        self.imgLabel.bind("<Button-1>", event)
        self.imgLabel.place(x = xPosition, y = yPosition)

    def destroy(self):
        self.imgLabel.destroy()
