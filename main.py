import kivy
from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
import plyer
import csv

lochNames = ['Loch Tollie', 'Loch Bad an Sgalaig', 'Dubh Loch', 'Loch Garbhaig', 'Loch nam Breac', 'Loch Feur', 'Loch a\' Gharbh-doire', 'Loch Airigh Mhic Criadh', 'Loch Airigh a\' Phuill', 'Loch nam Buainichean', 'Loch na Feithe Mugaig', 'Loch Doire na h-Airighe', 'Loch an Aird-sheilg']

class HomeScreen(Screen):
    pass

class WeatherScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class SettingsScreen(Screen):
    '''
    DEBUG
    '''
    fNameIn = 'Roddy'
    sNameIn = 'MacRae'
    fishSpeciesIn = 'Trout'

    def wifiState(self):
        print('###')
        #Get the status and check if the wifi is active and has network access
    pass

class RecordCatchScreen(Screen):
    def exportToDatabase():
        ''''
        This is where Jacks email code will go
        '''
        pass

    def fishName():
        fishNames = ['Brown Trout', 'Sea Trout', 'Pike', 'Salmon', 'Charr', 'Arctic Charr']
        #Need kivy script from Sean to finish this
        #Plan is for a drop down however if Sean thinks up anythong different he is welcome to it

    def fishWeightCollection(self):
        fishWeightIn = NumericProperty(None)
        print (fishWeightIn) #DEBUG
        fishWeightTypeInt = type(fishWeightIn) is int
        fishWeightTypeFloat = type(fishWeightIn) is float
        if fishWeightTypeInt != True or fishWeightTypeFloat != True:
            #If the weight of the fish is not a number do this
            print('Entered weight is not a number', fishWeightIn) #Error Message
        elif fishWeightTypeInt == True or fishWeightTypeFloat == True:
            #If the fish weight is a number do this
            return fishWeightIn

    def fishLengthCollection(self):
        fishLengthIn = NumericProperty(None)
        print (fishLengthIn) #DEBUG
        fishLengthTypeInt = type(fishLengthIn) is int
        fishLengthTypeFloat = type(fishLengthIn) is float
        if fishLengthTypeInt != True or fishLengthTypeFloat != True:
            #If the length of the fish is not a number do this
            print('Entered length is not a number', fishLengthIn) #Error Message
        elif fishLengthTypeInt == True or fishLengthTypeFloat == True:
            #If the fish length is a number do this
            return fishLengthIn
    '''
    Information to be sent to server need to be packaged in the following order:
    forename as fNameIn
    surname as sNameIn
    fish species as fishSpeciesIn
    fish weight as fishWeightIn
    fish length as fishLengthIn
    This is important for translation on server side
    '''

    def csvPackage(self, NameIn, fishSpeciesIn, fishWeightIn, fishLengthIn):

        Name = ['name', NameIn]
        fishSpecies = ['fishName', fishSpeciesIn]
        fishWeight = ['fishWeight', fishWeightIn]
        fishLength = ['fishLength', fishLengthIn]

        with open('WRFT.csv', 'w', newline='') as csvfile:
            lineWriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            lineWriter.writerow(fName)
            lineWriter.writerow(sName)
            lineWriter.writerow(fishSpecies)
            lineWriter.writerow(fishWeight)
            lineWriter.writerow(fishLength)
            #Call the below to change the specified information
            #csvPackage(fName, sName, fishSpecies, fishWeight, fishLength)

    def sendDatabase():
        exportToDatabase(csvPackage(fName, sName, fishSpecies, fishWeight, fishLength))
        #get the output from csvPackage() and use Jacks email script to send it
        print('sent')
    pass

class ScreenManagement(ScreenManager):
    pass

kivyFile = Builder.load_file("main.kv")

class MainApp(App):

    def build(self):
        return kivyFile

if __name__ == "__main__":
    MainApp().run()
