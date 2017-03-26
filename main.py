from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

          
class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class RecordCatchScreen(Screen):
    def sendDatabase():
        print'sent'

    def fishWeightCollection(self):
        fishWeight = ObjectProperty(None)
        print (fishWeightIn) #DEBUG
        fishWeightTypeInt = type(fishWeightIn) is int
        fishWeightTypeFloat = type(fishWeightIn) is float
        if fishWeightTypeInt != True or fishWeightTypeFloat != True: 
            #If the weight of the fish is not a number do this
            print('Entered weight is not a number', fishWeight) #Error Message 
        elif fishWeightTypeInt == True or fishWeightTypeFloat == True:
            #If the fish weight is a number do this
            return fishWeightIn

    def fishLengthCollection(self):
        fishLengthIn = ObjectProperty(None)
        print (fishLengthIn) #DEBUG
        fishLengthTypeInt = type(fishLengthIn) is int
        fishLengthTypeFloat = type(fishLengthIn) is float
        if fishLengthTypeInt != True or fishLengthTypeFloat != True: 
            #If the length of the fish is not a number do this
            print('Entered length is not a number', fishLength) #Error Message 
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
    '''

    def csvPackage(fNameIn, sNameIn, fishSpeciesIn, fishWeightIn, fishLengthIn):
        fName = ['f_name', fNameIn]
        sName = ['s_name', sNameIn]
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
    pass

class ScreenManagement(ScreenManager):
    pass


kivyFile = Builder.load_file("main.kv")

class MainApp(App):
    
    def build(self):
        return kivyFile

if __name__ == "__main__":
    MainApp().run()
