__author__ = 'Lina Andersson'
# Programmeringsteknik webbcourse KTH P-task.
# Lina Andersson
# 2016-03-29
# Program for a zoo where the user can search, sort, buy, sell and get recommendations on what to buy or sell.
# This file is the buy and sell page, where the user can buy, sell or get tips on what to buy or sell
# and is one of five modules in this program.

from tkinter import *
from ZooUtils import MyButton
import collections
from random import *

#class for the buy and sell page
class ZooBuySell:
    def __init__(self, tkRoot, viewDict):
        self.tkRoot = tkRoot
        self.viewDict = viewDict

        self.errorNameButton = None
        self.errorSpeciesButton = None
        self.errorGenderButton = None
        self.errorAgeButton = None

        self.labelNameEntry = None
        self.labelAgeEntry = None
        self.labelGenderEntry = None
        self.labelSpeciesEntry = None

        self.textLabelSell = None
        self.textLabelNoAnimalSell = None

        self.textLabelBuy = None
        self.textLabelNoAnimalBuy = None

        self.errorNameSellButton = None

        self.tipLabelBuy = None
        self.tipLabelSell = None

    def createButtonMenu(self):
        #Go back to main
        self.buttonMain = MyButton("backButton")
        self.buttonMain.addAsLabel(self.tkRoot, 107, 565, self.goToMain)

        #Buttons for buying, selling and getting tips
        self.buttonBuy = MyButton("buyAnimal")
        self.buttonBuy.addAsLabel(self.tkRoot, 298, 518, self.buyAnimal)

        self.buttonTipBuy = MyButton("tipBuy")
        self.buttonTipBuy.addAsLabel(self.tkRoot, 298, 591, self.tipBuyAnimal)

        self.buttonSell = MyButton("sellAnimal")
        self.buttonSell.addAsLabel(self.tkRoot, 435, 518, self.checkNumberOfAnimals)

        self.buttonTipSell = MyButton("tipSell")
        self.buttonTipSell.addAsLabel(self.tkRoot, 435, 591, self.tipSellAnimal)

    #Go back to mainpage
    def goToMain(self, event):
        #Destroy items if they contain information
        listOfItems = [self.buttonMain, self.buttonBuy, self.buttonSell, self.buttonTipBuy,
                       self.buttonTipSell]

        for item in listOfItems:
            if item is not None:
                item.destroy()

        self.viewDict["home"].destroyAnimalInfo()

        if self.viewDict["home"].pressedAnimalName:
            self.viewDict["home"].pressedAnimalName = False

        self.viewDict["home"].createButtonMenu()


    #Buy animal
    def buyAnimal(self, event):
        #if there is 35 or more animals in the zoo the user has to sell an animal before buying a new one
        if len(self.viewDict["home"].animalList) >= 35:
            #errorlabel if there is to many animals
            self.tooManyAnimalsLabel = MyButton("tooManyAnimals")
            self.tooManyAnimalsLabel.addAsLabel(self.tkRoot, 245, 215)

            self.cancelTooManyAnimals = MyButton("cancelButton")
            self.cancelTooManyAnimals.addAsLabel(self.tkRoot, 380, 410, self.closeTooManyAnimals)

        #Label where users can buy an animal by giving information about what they want to buy
        else:
            self.labelBuyInfo = MyButton("formBlock")
            self.labelBuyInfo.addAsLabel(self.tkRoot, 245, 215)

            self.labelNameEntry = Entry(bd = 0, width = 24, font = "14")
            self.labelNameEntry.place(x = 375, y = 245)

            self.labelAgeEntry = Entry(bd = 0, width = 24, font = "14")
            self.labelAgeEntry.place(x = 375, y = 281)

            self.labelSpeciesEntry = Entry(bd = 0, width = 24, font = "14")
            self.labelSpeciesEntry.place(x = 375, y = 353)

            self.radioVariabel = StringVar()
            self.radioVariabel.set("gender")

            self.radioFemale = Radiobutton(self.tkRoot, bg="#6fe577", activebackground="#6fe577", text="Female"
                                           , variable=self.radioVariabel, value="Female",
                                           indicatoron = 1)
            self.radioFemale.place(x = 375, y = 317)

            self.radioMale = Radiobutton(self.tkRoot, text="Male", bg="#6fe577",
                                         activebackground="#6fe577", variable=self.radioVariabel, value="Male",
                                         indicatoron = 1)
            self.radioMale.place(x = 440, y = 317)

            self.buyButton = MyButton("buyButton")
            self.buyButton.addAsLabel(self.tkRoot, 330, 410, self.checkInput)

            #Remove labels to buy an animal
            self.cancelButtonBuy = MyButton("cancelButton")
            self.cancelButtonBuy.addAsLabel(self.tkRoot, 435, 410, self.cancelBuy)


    #destroys error label
    def closeTooManyAnimals(self, event):
        self.tooManyAnimalsLabel.destroy()
        self.cancelTooManyAnimals.destroy()

    #checks if the user has written in correct data about the animal
    def checkInput(self, event):

        #delete earlier errorlabels if they contain some information
        errorButtons = [self.errorNameButton, self.errorSpeciesButton, self.errorGenderButton, self.errorAgeButton]

        for button in errorButtons:
            if button is not None:
                button.destroy()

        #collect user data
        userName = self.labelNameEntry.get()
        userAge = self.labelAgeEntry.get()
        userGender = self.radioVariabel.get()
        userSpecies = self.labelSpeciesEntry.get()

        checkedName = self.checkName(userName)

        #if checkedName is false
        if not checkedName:
            self.errorNameButton = MyButton("error")
            self.errorNameButton.addAsLabel(self.tkRoot, 600, 241, self.viewDict["home"].errorName)

        #check if age is integer
        try:
            userAge = int(userAge)
            #check age

            checkedAge = self.checkAge(userAge)
            if not checkedAge:
                self.errorAgeButton = MyButton("error")
                self.errorAgeButton.addAsLabel(self.tkRoot, 600, 277, self.viewDict["home"].errorAge)
            else:
                checkedAge = True
        except:
            self.errorAgeButton = MyButton("error")
            self.errorAgeButton.addAsLabel(self.tkRoot, 600, 277, self.viewDict["home"].errorAge)
            checkedAge = False

        #Check gender
        checkedGender = self.checkGender(userGender)
        if not checkedGender:
            self.errorGenderButton = MyButton("error")
            self.errorGenderButton.addAsLabel(self.tkRoot, 600, 313, self.viewDict["home"].errorGender)
        else:
            checkedGender = True

        #check species
        checkedSpecies = self.checkSpecies(userSpecies)
        if not checkedSpecies:
            self.errorSpeciesButton = MyButton("error")
            self.errorSpeciesButton.addAsLabel(self.tkRoot, 600, 349, self.viewDict["home"].errorSpecies)
        else:
            checkedSpecies = True

        #if all information is true - create animal
        if checkedName == True and checkedAge == True and checkedGender == True and checkedSpecies == True:

            #adds new animal to list
            newAnimalToList = [userName, int(userAge), userSpecies, userGender]

            #removes special characters from string and writes to file
            stringAnimal = str(newAnimalToList)
            stringAnimal = stringAnimal.replace("'", "")
            stringAnimal = stringAnimal.strip("[")
            stringAnimal = stringAnimal.strip("]")

            file = open("animalList.txt", "a")
            file.write(stringAnimal + "\n")
            file.close()

            #destroys buylabels and adds new animals to window
            self.cancelBuy(event)
            self.viewDict["home"].readAnimalsFromFile()
            self.viewDict["home"].addAnimalsToWindow()

    #check if user has written a correct name
    def checkName(self, userName):
        matchingCharacter = False
        lengthOfName = len(userName)

        # if two animals have the same name - set new name to nothing (which will make the name incorrect)
        for animal in self.viewDict["home"].animalList:
            if animal.name.lower() == userName.lower():
                userName = ""

        # checks if user has written anything at all or if the name short enough, if not the name is incorrect
        if userName != "" and lengthOfName < 11:
            lowerName = userName.lower()
            characterList = "abcdefghijklmnopqrstuvwxyz"

            firstCharacter = lowerName[0]

            # checks if the name starts with an alphabetic character, if not the name is incorrect
            for char in characterList:
                if char == firstCharacter:
                    matchingCharacter = True
                    return matchingCharacter
        return matchingCharacter

    # checks if the user has written in a propper age
    def checkAge(self, userAge):
        if len(str(userAge)) >= 11 or userAge < 0:
            return False
        else:
            return True

    # check if users written gender is correct
    def checkGender(self, userGender):
        genderStatus = None
        lowerGender = userGender.lower()
        if lowerGender == "female" or lowerGender == "male":
            if lowerGender == "female":
                genderStatus = "female"
                return genderStatus
            if lowerGender == "male":
                genderStatus = "male"
                return genderStatus
        return genderStatus

    #check if users written species is in listOfSpecies
    def checkSpecies(self, userSpecies):
        speciesList = None
        lowerSpecies = userSpecies.lower()
        listOfSpecies = ["tiger", "snow leopard", "t-rex", "rabbit", "fox", "parrot", "penguin",
                         "elephant", "lemur", "antilope", "clownfish", "zebra", "unicorn", "panda",
                         "giraffe", "snake", "serval", "fire dragon", "ice dragon", "cat", "frog",
                         "pig", "horse", "sea star"]
        for animal in listOfSpecies:
            if animal == lowerSpecies:
                speciesList = animal
                return speciesList
        return speciesList

    #removes labels from Buy-function
    def cancelBuy(self, event):
        listOfItems = [self.labelAgeEntry, self.labelNameEntry, self.labelSpeciesEntry, self.radioFemale, self.radioMale,
                       self.buyButton, self.cancelButtonBuy, self.labelBuyInfo]

        for item in listOfItems:
            item.destroy()

        errorButtons = [self.errorNameButton, self.errorSpeciesButton, self.errorGenderButton, self.errorAgeButton,
                        self.viewDict["home"].textLabelError, self.viewDict["home"].messageLabel]

        for button in errorButtons:
            if button is not None:
                button.destroy()

    #Tip for buying
    def tipBuyAnimal(self, event):
        if self.tipLabelBuy != None:
            self.cancelTipBuy(None)

        self.tipLabelBuy = MyButton("tipLabel")
        self.tipLabelBuy.addAsLabel(self.tkRoot, 245, 215)

        #randomly collects a singel animal
        lonleyAnimalSpecies = str(self.checkForLonleyAnimal())
        recommendedAnimal = str(self.checkGenderOfAnimal(lonleyAnimalSpecies))

        #if there is one or more lonley animal shall a message be printed with the recommmended animal
        if recommendedAnimal != "no animal":
            self.textLabelBuy = Label(text = "We recommend you to \n buy a " + recommendedAnimal + " " + lonleyAnimalSpecies
                                             + "!", font = ("Myriad Pro", 20), fg = "white", bg ="#6fe577")
            self.textLabelBuy.place(x = 300, y = 300)

        #if there is no lonley animal a label with no tip will be shown
        else:
            self.textLabelNoAnimalBuy = Label(text = "None of your animals\n are lonley, "
                                             "buy which \nanimal you like",
                                              font = ("Myriad Pro", 20), fg = "white", bg ="#6fe577")
            self.textLabelNoAnimalBuy.place(x = 300, y = 290)

        self.cancelButtonTipBuy = MyButton("cancelButton")
        self.cancelButtonTipBuy.addAsLabel(self.tkRoot, 380, 410, self.cancelTipBuy)

    #checks which genders the recommended animalspecies has and recommends the gender that is "lonley"
    def checkGenderOfAnimal(self, recommendedSpecies):
        listOfAnimals = []

        for animal in self.viewDict["home"].animalList:
            if recommendedSpecies == animal.species:
                listOfAnimals.append(animal)

        males = 0
        females = 0

        for animalGender in listOfAnimals:
            if animalGender.gender.lower() == "female":
                females += 1
            if animalGender.gender.lower() == "male":
                males += 1

        if males > females:
            return "female"
        else:
            return "male"

    #tip for selling
    def tipSellAnimal(self, event):
        if self.tipLabelSell != None:
            self.cancelTipSell(None)

        self.tipLabelSell = MyButton("tipLabel")
        self.tipLabelSell.addAsLabel(self.tkRoot, 245, 215)

        recommendedAnimal = str(self.checkForLonleyAnimal())

        #if there is one or more lonley animal shall a message be printed with the recommmended animal
        if recommendedAnimal != "no animal":
            self.textLabelSell = Label(text = "We recommend you to \n sell a " + recommendedAnimal + "!", font = ("Myriad Pro", 20), fg = "white", bg ="#6fe577")
            self.textLabelSell.place(x = 300, y = 300)

        #if there is no lonley animal shall a message about that be shown
        else:
            self.textLabelNoAnimalSell = Label(text = "None of your animals\n are lonley, "
                                             "sell which \nanimal you like", font = ("Myriad Pro", 20), fg = "white", bg ="#6fe577")
            self.textLabelNoAnimalSell.place(x = 300, y = 290)

        self.cancelButtonTipSell = MyButton("cancelButton")
        self.cancelButtonTipSell.addAsLabel(self.tkRoot, 380, 410, self.cancelTipSell)

    #makes all speices to lowercase characters
    def getSpeciesOf(self, animal):
        return animal.species.lower()

    #checks if there is a lonley animal
    def checkForLonleyAnimal(self):
        listOfLonleyAnimals = []

        #collects all species from animallist
        speciesList = map(self.getSpeciesOf, self.viewDict["home"].animalList)

        #counts how many of each animals is in the specieslist
        countAnimals = collections.Counter(speciesList)

        #if the number of animals is a modulus of two - add animal to listOfLonleyAnimals
        for animal, numberOfAnimal in countAnimals.items(): #returns a tuple containing animal: numberOfAnimals
            if numberOfAnimal%2 == 1:
                listOfLonleyAnimals.append(animal)

        lengthOfLonleyAnimals = len(listOfLonleyAnimals)

        #if listOfLonleyAnimals doesent contain something - return "no animal"
        if not listOfLonleyAnimals:
            noAnimal = "no animal"
            return noAnimal
        #if listOfLonleyAnimals contains something - take randomly out one of them to be shown for the user
        else:
            randomAnimalIndex = randint(0, lengthOfLonleyAnimals-1)
            return listOfLonleyAnimals[randomAnimalIndex]

    #removes labels from tipSell-function
    def cancelTipSell(self, event):
        self.tipLabelSell.destroy()
        self.cancelButtonTipSell.destroy()

        textLabels = [self.textLabelSell, self.textLabelNoAnimalSell]
        for labels in textLabels:
            if labels is not None:
                labels.destroy()

    #removes labels from tipBuy-function
    def cancelTipBuy(self, event):
        self.tipLabelBuy.destroy()
        self.cancelButtonTipBuy.destroy()

        textLabels = [self.textLabelBuy, self.textLabelNoAnimalBuy]
        for labels in textLabels:
            if labels is not None:
                labels.destroy()

    def checkNumberOfAnimals(self, event):
        if len(self.viewDict["home"].animalList) <= 0:
            print(len(self.viewDict["home"].animalList))
            self.tooFewAnimalsLabel = MyButton("tooFewAnimals")
            self.tooFewAnimalsLabel.addAsLabel(self.tkRoot, 245, 215)

            self.cancelTooFewAnimals = MyButton("cancelButton")
            self.cancelTooFewAnimals.addAsLabel(self.tkRoot, 380, 410, self.closeTooFewAnimals)
        else:
            self.sellAnimal()

    def closeTooFewAnimals(self, event):
        self.tooFewAnimalsLabel.destroy()
        self.cancelTooFewAnimals.destroy()

    #Sell animal
    def sellAnimal(self):
        self.labelSellAnimal = MyButton("sellName")
        self.labelSellAnimal.addAsLabel(self.tkRoot, 245, 215)

        #User writes the name of the animal that is to be sold
        self.sellEntry = Entry(bd = 0, width = 24, font = "14")
        self.sellEntry.place(x = 325, y = 350)

        self.sellButton = MyButton("sellButton")
        self.sellButton.addAsLabel(self.tkRoot, 330, 410, self.checkSoldAnimalName)

        self.cancelButtonSell = MyButton("cancelButton")
        self.cancelButtonSell.addAsLabel(self.tkRoot, 435, 410, self.cancelSell)

    #removes labels from sell-function
    def checkSoldAnimalName(self, event):
        foundAnimal = False
        userName = self.sellEntry.get()

        lowerName = userName.lower()
        #check if the users written name matches with an animal in animalList
        for animal in self.viewDict["home"].animalList:
            if animal.name.lower() == lowerName:
                foundAnimal = True
                self.subFromAnimalList(lowerName)
        if foundAnimal == False:
            self.noMatchName()

    #error message if no animal match the users name
    def noMatchName(self):
        self.errorNameSellButton = MyButton("error")
        self.errorNameSellButton.addAsLabel(self.tkRoot, 550, 345, self.errorSellName)

    def errorSellName(self, event):
        self.showError("nameError", 580, 345)

    def subFromAnimalList(self, animalName):

        #open file with animals and read lines to fileLines
        file = open("animalList.txt", "r")
        fileLines = file.readlines()
        file.close

        #open file and for each line read in the animals name and check for each line if the name of the animal that
        # will be removed matches with the lines in the file. If true then the animal is removed and the
        # other ones moved up
        file = open("animalList.txt", "w" )
        for line in fileLines:
            splitRow = line.split(", ")
            lowerSplit = splitRow[0].lower()
            if lowerSplit != animalName.lower():
                file.write(line)

        file.close()
        self.cancelSell(lowerSplit)
        self.viewDict["home"].readAnimalsFromFile()
        self.viewDict["home"].updateAnimalList(self.viewDict["home"].animalList)

    def cancelSell(self, event):

        self.sellEntry.destroy()
        self.sellButton.destroy()
        self.cancelButtonSell.destroy()
        self.labelSellAnimal.destroy()

        textLabels = [self.errorNameSellButton, self.viewDict["home"].messageLabel]
        for labels in textLabels:
            if labels is not None:
                labels.destroy()
