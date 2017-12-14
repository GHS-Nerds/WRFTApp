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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color
#Packaging module
import csv
#Sheets intergration
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('SWRFTTesting.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open("WRFTAppTest").sheet1

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

class LampreysScreen(Screen):
    pass

class EelScreen(Screen):
    pass

class MinnowScreen(Screen):
    pass

class SticklebackScreen(Screen):
    pass

class SalmonScreen(Screen):
    pass

class TroutScreen(Screen):
    pass

class ArcticCharrScreen(Screen):
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
    def textPackage(self, nameIn, fishSpeciesIn, fishWeightIn, fishLengthIn):
            Name = nameIn
            fishSpecies = fishSpeciesIn
            fishWeight = str(fishWeightIn)
            fishLength = str(fishLengthIn)

            f_test = open('test.txt')
            f_test_read = f_test.read()
            print(f_test_read)
            if 'NEW_ENTRY' not in f_test_read:
                f_test.close()
                f = open("test.txt","w") #opens file with name of "test.txt"
                f.write('NEW_ENTRY\n')
                f.write(Name)
                f.write('\n')
                f.write(fishSpecies)
                f.write('\n')
                f.write(fishWeight)
                f.write('\n')
                f.write(fishLength)
                f.write('\n')
                f.close()
            else:
                f_test.close()
                f = open("test.txt","a") #opens file with name of "test.txt"
                f.write('NEW_ENTRY\n')
                f.write(Name)
                f.write('\n')
                f.write(fishSpecies)
                f.write('\n')
                f.write(fishWeight)
                f.write('\n')
                f.write(fishLength)
                f.write('\n')
                f.close()

    def SendtoSheets(self):
        #Reads information from the text file
        f_test = open('test.txt')
        f_test_read = f_test.read()
        #Splits information into various sections (Name, Surname, Fish Species, Fish Weight, Fish Length)
        info = f_test_read.split()
        info = info[1:]
        Name = info[0]
        S_Name = info[1]
        fishSpecies = info[2]
        fishWeight = info[3]
        fishLength = info[4]
        row = [Name, fishSpecies, fishWeight, fishLength]
        index = 1
        #Inserts information into spreadsheet
        sheet.append_row(row)
        f_test.write("")
        f_test.close()



    def build(self):
        return kivyFile

if __name__ == "__main__":
    MainApp().run()

