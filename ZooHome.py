__author__ = 'Lina Andersson'
# Programmeringsteknik webbcourse KTH P-task.
# Lina Andersson
# 2016-03-29
# Program for a zoo where the user can search, sort, buy, sell and get recommendations on what to buy or sell.
# This file is the main or start file and is one of five modules in this program.

from tkinter import *
from PIL import ImageTk, Image
from ZooSearch import ZooSearch
from ZooSort import ZooSort
from ZooBuySell import ZooBuySell
from ZooUtils import MyButton, Animal, AnimalLabel

def main():

    #create window and dictionary for the different pages
    tkRoot = Tk()
    viewDict = {}

    home = ZooHome(tkRoot, viewDict)
    viewDict["home"] = home

    buySell = ZooBuySell(tkRoot, viewDict)
    viewDict["buySell"] = buySell

    sort = ZooSort(tkRoot, viewDict)
    viewDict["sort"] = sort

    search = ZooSearch(tkRoot, viewDict)
    viewDict["search"] = search

    #create first page, read in animals and uppdate animalList
    home.display()
    home.readAnimalsFromFile()
    home.updateAnimalList(home.animalList)
    home.tkRoot.mainloop()

#class for the home page
class ZooHome:
    def __init__(self, tkRoot, viewDict):
        self.tkRoot = tkRoot

        #makes size of the window fixed
        self.tkRoot.resizable(width= False, height= False)
        self.tkRoot.title("Zoo")

        self.viewDict = viewDict
        self.pressedName = False
        self.pressedAnimalName = False
        self.lastPosition = 0
        self.lastAnimalPositionY = 0
        self.lastAnimalPositionX = 0

        self.infoLabel = None
        self.messageLabel = None
        self.textLabelError = None
        self.nameText = None
        self.ageText = None
        self.genderText = None
        self.speciesText = None
        self.messageLabel = None

    #creates first page with buttons and background image
    def display(self):
        self.animalList = []
        self.animalLabels = []

        #create background image
        img = Image.open("polybackground.png")
        self.imgBackground = ImageTk.PhotoImage(img)

        #display background image on screen
        self.panel = Label(self.tkRoot, image = self.imgBackground, borderwidth = 0)
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")

        #top button
        self.buttonTop = MyButton("animalButton")
        self.buttonTop.addAsLabel(self.tkRoot, 350, 50)

        self.createButtonMenu()

    def createButtonMenu(self):

        #buy and sell button
        self.buttonBuy = MyButton("buySellButton")
        self.buttonBuy.addAsLabel(self.tkRoot, 350, 550, self.goToSellBuy)

        #search button
        self.buttonSearch = MyButton("searchButton")
        self.buttonSearch.addAsLabel(self.tkRoot, 171, 550, self.goToSearch)

        #sort button
        self.buttonSort = MyButton("sortButton")
        self.buttonSort.addAsLabel(self.tkRoot, 529, 550, self.goToSort)

    #Go to sell/buy page
    def goToSellBuy(self, event):
        self.goToOtherPage("buySell")

    #Go to search page
    def goToSearch(self, event):
        self.goToOtherPage("search")

    #Go to sort page
    def goToSort(self, event):
        self.goToOtherPage("sort")

    #destroys button menu and sends the user to the desired page
    def goToOtherPage(self, page):
        self.buttonBuy.destroy()
        self.buttonSort.destroy()
        self.buttonSearch.destroy()

        #destroys animalInfo the info is on the screen
        self.destroyAnimalInfo()

        if self.pressedAnimalName:
            self.pressedAnimalName = False

        self.viewDict[page].createButtonMenu()

    #reads in animals from file
    def readAnimalsFromFile(self):

        #open list of animals
        self.animalList = []
        animalFile = open("animalList.txt", "r")

        #appends all the animals to a list
        for row in animalFile:
            if len(row) == 1:
                break
            else:
                splitRow = row.split(", ")

                name = splitRow[0]
                age = int(splitRow[1])
                species = splitRow[2]
                gender = splitRow[3].replace("\n", "")

                #create animal instance
                animalInstance = Animal(name, age, species, gender)

                self.animalList.append(animalInstance)

    #Updates animalList before adding animals to window
    def updateAnimalList(self, newAnimalList):
        self.animalList = newAnimalList
        self.addAnimalsToWindow()

    #create grid of animals
    def addAnimalsToWindow(self):
        self.animalLabels = []
        index = 0
        animalCount = len(self.animalList)

        #squares in 2d-list for each animal
        for column in range(140, 480, 75):

            for row in range(171, 650, 75):
                if index < animalCount:
                    #black squares if no animal
                    anAnimal = self.animalList[index]
                    animalLabel = AnimalLabel(anAnimal, "square.png")
                    animalLabel.addAsLabel(self.tkRoot, row, column, self.createLambda(row, column, anAnimal.name,
                                                                                      anAnimal.age, anAnimal.gender,
                                                                                      anAnimal.species)) #event that
                                                                                      # occurs when user pusches the
                                                                                      # label. Sends info about animal
                                                                                      # to createLambda
                    self.animalLabels.append(animalLabel)

                    index += 1
                else:
                    #creates images of animals
                    animalLabel = AnimalLabel(None, "square.png")
                    animalLabel.addAsLabel(self.tkRoot, row, column)
                    self.animalLabels.append(animalLabel)

    #captures all values passed in as arguments and creates a lambda that calls showInfoBox
    #with the captured values
    def createLambda(self, row, column, name, age, gender, species):
        return lambda x: self.showInfoBox(row, column, name, age, gender, species)

    #function that create different error message labels that can be pusched once to be shown and twice to be deleted
    def showError(self, messageText, xPosition, yPosition, text = False):

        # checks if the label was pressed before or not - if it was pushed before the messagelabel is now
        # destroyed and the press counter is set to False
        if self.messageLabel is not None and self.lastPosition != yPosition:
            self.messageLabel.destroy()
            self.pressedName = False #count presses, if first press true if second press false
            if self.textLabelError is not None:
                self.textLabelError.destroy()

        #if pressedName is false (users first push is made) a messageLabel is created and pressedName changes to True
        if not self.pressedName:
            self.messageLabel = MyButton(messageText)
            self.messageLabel.addAsLabel(self.tkRoot, xPosition, yPosition)
            self.pressedName = True

            # if text-attribute contains something then a text shall appear
            if text == True:
                self.textLabelError = Label(text = "Zebra, Parrot, Tiger, \nSnow leopard, Fox, Rabbit, "
                                      "\nAntilope, Elephant, Penguin \nLemur, Clownfish, T-rex \n "
                                      "Panda, Giraffe, Snake \n Serval, Car, Frog, Pig  \n"
                                      "Horse, Sea star, Fire dragon, \nIce dragon and Unicorn",
                                            font = ("Myriad Pro", 10), fg = "white", bg ="#6fe577")
                self.textLabelError.place(x = 660, y = 400)

        else:
            #destroys labels if they contain information and resets attributes to None/False
            if self.messageLabel is not None:
                self.messageLabel.destroy()
            if self.textLabelError is not None:
                self.textLabelError.destroy()

            self.textLabelError = None
            self.messageLabel = None
            self.pressedName = False

        #checks wich button the user puched last time
        self.lastPosition = yPosition

    #shows errorlabel if user enters wrong characters
    def errorName(self, event):
        self.showError("alphaError", 632, 241)

    def errorAge(self, event):
        self.showError("ageError", 632, 277)

    def errorGender(self, event):
        self.showError("genderError", 632, 313)

    def errorSpecies(self, event):
        self.showError("speciesError", 632, 349, True)

    #Sends info about animal to showMessage
    def showInfoBox(self, row, column, name, age, gender, species):
        self.showAnimalInfoBox("infoLabel", int(row) - 35, int(column) + 70, name, age, gender, species)

    #keeps track of the info boxes for each animal and checks if the infobox should be shown or not
    def showAnimalInfoBox(self, imageName, xPosition, yPosition, name, age, gender, species):

        # checks if the label was pressed before or not - if it was pushed before the infolabel is
        # destroyed and the press counter is set to False
        if self.infoLabel is not None and (self.lastAnimalPositionY != yPosition or self.lastAnimalPositionX != xPosition):
            self.pressedAnimalName = False #count presses, if first press true if second press false
            self.infoLabel.destroy()
            self.destroyAnimalInfo()

        #if pressedName is false (users first push is made) a messageLabel is created and pressedName changes to True
        if not self.pressedAnimalName:
            self.infoLabel = MyButton(imageName)
            self.infoLabel.addAsLabel(self.tkRoot, xPosition, yPosition)
            self.pressedAnimalName = True

            #if name contains something then information is sent to showAnimalInfo
            if name:
                self.showAnimalInfo(xPosition, yPosition, name, age, gender, species)

        else:
            #destroys labels if they contain information and resets attributes to None/False
            if self.infoLabel is not None:
                self.infoLabel.destroy()
                self.destroyAnimalInfo()

            self.infoLabel = None
            self.pressedAnimalName = False

        #checks wich button the user puched last time
        self.lastAnimalPositionY = yPosition
        self.lastAnimalPositionX = xPosition


    #if user pushes an animalLabel this function makes a box of information about the animal pop up
    def showAnimalInfo(self, xPosition, yPosition, name, age, gender, species):

        name = self.makeFirstCharacterUppercase(name)
        gender = self.makeFirstCharacterUppercase(gender)
        species = self.makeFirstCharacterUppercase(species)

        #create textlabels with animal information
        self.nameText = Label(text = str(name), font = ("Myriad Pro", 12), fg = "white", bg ="#6fe577")
        self.nameText .place(x = xPosition + 56, y = yPosition + 9)

        self.ageText = Label(text = str(age), font = ("Myriad Pro", 12), fg = "white", bg ="#6fe577")
        self.ageText .place(x = xPosition + 56, y = yPosition + 28)

        self.genderText = Label(text = str(gender), font = ("Myriad Pro", 12), fg = "white", bg ="#6fe577")
        self.genderText .place(x = xPosition + 68, y = yPosition + 48)

        self.speciesText = Label(text = str(species), font = ("Myriad Pro", 12), fg = "white", bg ="#6fe577")
        self.speciesText .place(x = xPosition + 68, y = yPosition + 66)

    #make first character in string uppercase
    def makeFirstCharacterUppercase(self, word):
        word = word[0].upper() + word[1:]
        return word

    #destroys infolabels about animals if they contain information
    def destroyAnimalInfo(self):
        listOfItems = [self.nameText, self.ageText,
                       self.genderText, self.speciesText,
                       self.infoLabel]

        for item in listOfItems:
            if item is not None:
                item.destroy()

#call main function
if __name__ == "__main__":
    main()