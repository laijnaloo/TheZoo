__author__ = 'Lina Andersson'
# Programmeringsteknik webbcourse KTH P-task.
# Lina Andersson
# 2016-03-29
# Program for a zoo where the user can search, sort, buy, sell and get recommendations on what to buy or sell.
# This file is the sorting page, where the user can sort the animals after specific attributes
# and is one of five modules in this program.

from ZooUtils import MyButton

#class for the sort page
class ZooSort:
    def __init__(self, tkRoot, viewDict):
        self.tkRoot = tkRoot
        self.viewDict = viewDict

    def createButtonMenu(self):

        #back to main page
        self.buttonMain = MyButton("backButton")
        self.buttonMain.addAsLabel(self.tkRoot, 107, 565, self.goToMain)

        #Eight buttons doind different kinds of sorting
        self.buttonNameAZ = MyButton("namesAZ")
        self.buttonNameAZ.addAsLabel(self.tkRoot, 161, 518, self.nameAZ)

        self.buttonNameZA = MyButton("namesZA")
        self.buttonNameZA.addAsLabel(self.tkRoot, 161, 591, self.nameZA)

        self.buttonAgeYO = MyButton("ageYO")
        self.buttonAgeYO.addAsLabel(self.tkRoot, 298, 518, self.ageYoung)

        self.buttonAgeOY = MyButton("ageOY")
        self.buttonAgeOY.addAsLabel(self.tkRoot, 298, 591, self.ageOld)

        self.buttonGenderFM = MyButton("genderFM")
        self.buttonGenderFM.addAsLabel(self.tkRoot, 435, 518, self.genderFemale)

        self.buttonGenderMF = MyButton("genderMF")
        self.buttonGenderMF.addAsLabel(self.tkRoot, 435, 591, self.genderMale)

        self.buttonSpeciesAZ  = MyButton("speciesAZ")
        self.buttonSpeciesAZ.addAsLabel(self.tkRoot, 572, 518, self.speciesAZ)

        self.buttonSpeciesZA = MyButton("speciesZA")
        self.buttonSpeciesZA.addAsLabel(self.tkRoot, 572, 591, self.speciesZA)

    def goToMain(self, event):
        #Destroy items
        self.buttonMain.destroy()

        self.buttonNameAZ.destroy()
        self.buttonNameZA.destroy()

        self.buttonAgeYO.destroy()
        self.buttonAgeOY.destroy()

        self.buttonGenderFM.destroy()
        self.buttonGenderMF.destroy()

        self.buttonSpeciesAZ.destroy()
        self.buttonSpeciesZA.destroy()

        #if the user have pushed on an animal picture it will be destroyed when moving to a different page
        self.viewDict["home"].destroyAnimalInfo()

        #resets pressedName to False if it was True
        if self.viewDict["home"].pressedAnimalName:
            self.viewDict["home"].pressedAnimalName = False

        self.viewDict["home"].createButtonMenu()

    def nameAZ(self, event):
        #returns animal with A (or first) first in list
        sortedList = sorted(self.viewDict["home"].animalList, key = lambda animal: animal.name.lower())
        animalList = sortedList
        self.viewDict["home"].updateAnimalList(animalList)
        self.viewDict["home"].destroyAnimalInfo()

    def nameZA(self, event):
        #returns animal with Z (or last) first in list
        sortedList = sorted(self.viewDict["home"].animalList, key = lambda animal: animal.name.lower(), reverse=True)
        animalList = sortedList
        self.viewDict["home"].updateAnimalList(animalList)
        self.viewDict["home"].destroyAnimalInfo()

    def ageYoung(self, event):
        #returns youngest animal first in list
        sortedList = sorted(self.viewDict["home"].animalList, key = lambda animal: animal.age)
        animalList = sortedList
        self.viewDict["home"].updateAnimalList(animalList)
        self.viewDict["home"].destroyAnimalInfo()

    def ageOld(self, event):
        #returns oldest animal first in list
        sortedList = sorted(self.viewDict["home"].animalList, key = lambda animal: animal.age, reverse=True)
        animalList = sortedList
        self.viewDict["home"].updateAnimalList(animalList)
        self.viewDict["home"].destroyAnimalInfo()

    def genderFemale(self, event):
        #returns femalesbfirst in list
        sortedList = sorted(self.viewDict["home"].animalList, key = lambda animal: animal.gender.lower())
        animalList = sortedList
        self.viewDict["home"].updateAnimalList(animalList)
        self.viewDict["home"].destroyAnimalInfo()

    def genderMale(self, event):
        #returns malesbfirst in list
        sortedList = sorted(self.viewDict["home"].animalList, key = lambda animal: animal.gender.lower(), reverse=True)
        animalList = sortedList
        self.viewDict["home"].updateAnimalList(animalList)
        self.viewDict["home"].destroyAnimalInfo()

    def speciesAZ(self, event):
        #returns animal with A (or first) first in list
        sortedList = sorted(self.viewDict["home"].animalList, key = lambda animal: animal.species.lower())
        animalList = sortedList
        self.viewDict["home"].updateAnimalList(animalList)
        self.viewDict["home"].destroyAnimalInfo()

    def speciesZA(self, event):
        #returns animal with Z (or last) first in list
        sortedList = sorted(self.viewDict["home"].animalList, key = lambda animal: animal.species.lower(), reverse=True)
        animalList = sortedList
        self.viewDict["home"].updateAnimalList(animalList)
        self.viewDict["home"].destroyAnimalInfo()