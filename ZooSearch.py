__author__ = 'Lina Andersson'
# Programmeringsteknik webbcourse KTH P-task.
# Lina Andersson
# 2016-03-29
# Program for a zoo where the user can search, sort, buy, sell and get recommendations on what to buy or sell.
# This file is the search page, where the user can search for specific attributes of the animals and is one
# of five modules in this program.

from tkinter import *
from PIL import ImageTk, Image
from ZooUtils import MyButton

#class for the search page
class ZooSearch:
    def __init__(self, tkRoot, viewDict):
        self.tkRoot = tkRoot
        self.viewDict = viewDict

    def createButtonMenu(self):
        #go back to main
        self.buttonMain = MyButton("backButton")
        self.buttonMain.addAsLabel(self.tkRoot, 117, 565, self.goToMain)

        #search name
        self.labelName = MyButton("searchName")
        self.labelName.addAsLabel(self.tkRoot, 171, 518)

        #search age
        self.labelAge = MyButton("searchAge")
        self.labelAge.addAsLabel(self.tkRoot, 171, 557)

        #search gender
        self.labelGender = MyButton("searchGender")
        self.labelGender.addAsLabel(self.tkRoot, 171, 596)

        #search species
        self.labelSpecies = MyButton("searchSpecies")
        self.labelSpecies.addAsLabel(self.tkRoot, 171, 635)

        #User input for search
        self.labelNameEntry = Entry(bd = 0, width = 67)
        self.labelAgeEntry = Entry(bd = 0, width = 67)
        self.labelGenderEntry = Entry(bd = 0, width = 67)
        self.labelSpeciesEntry = Entry(bd = 0, width = 67)

        entryList = [self.labelNameEntry, self.labelAgeEntry, self.labelGenderEntry, self.labelSpeciesEntry]

        #place for entry
        for index, entry in enumerate(entryList):
            entry.place(x = 282, y = 528 + 38.5*index)

        #Search
        self.buttonSearch = MyButton("searchSearch")
        self.buttonSearch.addAsLabel(self.tkRoot, 700, 565, self.checkSearch)

    def goToMain(self, event):

        #Destroy items
        listOfItems = [self.buttonMain, self.labelName, self.labelAge, self.labelGender,
                       self.labelSpecies, self.buttonSearch, self.labelAgeEntry,
                       self.labelNameEntry, self.labelGenderEntry, self.labelSpeciesEntry]

        for item in listOfItems:
            if item is not None:
                item.destroy()

        self.viewDict["home"].destroyAnimalInfo()

        if self.viewDict["home"].pressedAnimalName:
            self.viewDict["home"].pressedAnimalName = False

        for animLabel in self.viewDict["home"].animalLabels:
            animLabel.img = Image.open("square.png")
            animLabel.tkImg = ImageTk.PhotoImage(animLabel.img)
            animLabel.imgLabel.configure(image = animLabel.tkImg)
            animLabel.imgLabel.image = animLabel.tkImg

        self.viewDict["home"].createButtonMenu()

    def checkSearch(self, event):
        #gather and make all input in lowercase
        userName = self.labelNameEntry.get().lower()
        userAge = self.labelAgeEntry.get().lower()
        userGender = self.labelGenderEntry.get().lower()
        userSpecies = self.labelSpeciesEntry.get().lower()

        matchingAnimals = []
        for animal in self.viewDict["home"].animalList:

            matchName = False
            matchAge = False
            matchGender = False
            matchSpecies = False

            #if no input - no matches
            if userName == "" and userAge == "" and userGender == "" and userSpecies == "":
                self.noMatch()
                self.goToDestroy(None)

            else:
                #see what user input matches zoo-animals
                if userName == "" or userName == animal.name.lower():
                    matchName = True
                if userAge == "" or userAge == str(animal.age):
                    matchAge = True
                if userGender == "" or userGender == animal.gender.lower():
                    matchGender = True
                if userSpecies == "" or userSpecies == animal.species.lower():
                    matchSpecies = True

                #if match - add animal to a list of matches
                if matchName == True and matchAge == True and matchGender == True and matchSpecies == True:
                    matchingAnimals.append(animal)

        #Checks if there is a match or not
        lengthOfMatchList = len(matchingAnimals)
        if lengthOfMatchList != 0:
            self.greenSearchLabel(matchingAnimals)
        else:
            self.noMatch()

    #changes background image from black to green when matching
    def greenSearchLabel(self, listOfMatches):
        for animLabel in self.viewDict["home"].animalLabels:
            #makes all labels black
            animLabel.img = Image.open("square.png")
            animLabel.tkImg = ImageTk.PhotoImage(animLabel.img)
            animLabel.imgLabel.configure(image = animLabel.tkImg)
            animLabel.imgLabel.image = animLabel.tkImg

        for animLabel in self.viewDict["home"].animalLabels:
            #matches animal with animallabel and chages the color of the label
            for animal in listOfMatches:
                if animLabel.anAnimal == animal:
                    newImg = Image.open("greenSquare.png")
                    newTkImg = ImageTk.PhotoImage(newImg)
                    animLabel.imgLabel.configure(image = newTkImg)
                    animLabel.imgLabel.image = newTkImg
                    animLabel.img = newImg
                    animLabel.tkImg = newTkImg

    #shows label when there is no match with user input and animalList
    def noMatch(self):
        self.noMatchImg = MyButton("noMatches")
        self.noMatchImg.addAsLabel(self.tkRoot, 245, 215)

        self.closeButton = MyButton("closeButton")
        self.closeButton.addAsLabel(self.tkRoot, 360, 350, self.goToDestroy)

    #removes noMatch content
    def goToDestroy(self, event):
        self.noMatchImg.destroy()
        self.closeButton.destroy()
