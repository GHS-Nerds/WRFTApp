import kivy
from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
import numpy as np
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


lochNames = ['Loch Tollie', 'Loch Bad an Sgalaig', 'Dubh Loch', 'Loch Garbhaig', 'Loch nam Breac', 'Loch Feur', 'Loch a\' Gharbh-doire', 'Loch Airigh Mhic Criadh', 'Loch Airigh a\' Phuill', 'Loch nam Buainichean', 'Loch na Feithe Mugaig', 'Loch Doire na h-Airighe', 'Loch an Aird-sheilg']

class HomeScreen(Screen):
    pass

class WeatherScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class InvaScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class NonInvaScreen(Screen):
    pass

class LicencesScreen(Screen):
    pass

class SettingsScreen(Screen):

    def wifiState(self):
        print('###')
        #Get the status and check if the wifi is active and has network access
    pass

class RecordCatchScreen(Screen):
    fishWeightIn = ObjectProperty(None)
    fishLengthIn = ObjectProperty(None)

    def sendDatabase():
        #exportToDatabase(csvPackage(name, fishSpecies, fishWeight, fishLength))
        #get the output from csvPackage() and use Jacks email script to send it
        pass

    def exportToDatabase():
        ''''
        This is where Jacks email code will go
        '''
        pass

    pass

class ScreenManagement(ScreenManager):
    pass

kivyFile = Builder.load_file("main.kv")

class MainApp(App):
    index = 0
    '''
    Information to be sent to server need to be packaged in the following order:
    full name as nameIn
    fish species as fishSpeciesIn
    fish weight as fishWeightIn
    fish length as fishLengthIn
    This is important for translation on server side
    '''

    def textPackage(self, nameIn, fishSpeciesIn, fishWeightIn, fishLengthIn):
            #Peace of mind convertions to float values
            fishWeightIn = int(fishWeightIn)
            fishLengthIn = int(fishLengthIn)

            #Convert to bytes for np
            nameIn = str.encode(nameIn)
            fishSpeciesIn = str.encode(fishSpeciesIn)

            #Checking input variable types
            if (type(fishWeightIn) is int) == False:
                typeChecks = True
                print('Incorrect Type fishWeightIn')
                #Make this produce an error code
            elif (type(fishWeightIn) is int) == True:
                typeChecks = False
                fishWeightIn = bytes([fishWeightIn])
                print('Correct Type fishWeightIn')

            if (type(fishLengthIn) is int) == False:
                typeChecks = True
                print('Incorrect Type fishLengthIn')
                #Make this produce an error code
            elif (type(fishLengthIn) is int) == True:
                typeChecks = False
                fishLengthIn = bytes([fishLengthIn])
                print('Correct Type fishLengthIn')


            if typeChecks == False:
                print(nameIn, fishSpeciesIn, fishWeightIn, fishLengthIn)
                data = np.array([nameIn, fishSpeciesIn, fishWeightIn, fishLengthIn],dtype=[('Name', 'S20'), ('FishSpecies', 'S20'), ('FishWeight', 'f4'), ('FishLength', 'f4')])
                data = np.savetxt('C:/Users/rwmac/Documents/Programming/WRFTApp/InProgress/WRFT.txt',data, fmt=['%s', '%s', '%i', '%i'])
                return data
            elif typeChecks == True:
                print('Error in input types: Data not encoded')

    def build(self):
        return kivyFile

if __name__ == "__main__":
    MainApp().run()
