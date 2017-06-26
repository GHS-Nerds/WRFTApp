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
import plyer
import pandas

lochNames = ['Loch Tollie', 'Loch Bad an Sgalaig', 'Dubh Loch', 'Loch Garbhaig', 'Loch nam Breac', 'Loch Feur', 'Loch a\' Gharbh-doire', 'Loch Airigh Mhic Criadh', 'Loch Airigh a\' Phuill', 'Loch nam Buainichean', 'Loch na Feithe Mugaig', 'Loch Doire na h-Airighe', 'Loch an Aird-sheilg']

class HomeScreen(Screen):
    pass

class WeatherScreen(Screen):
    pass

class MapScreen(Screen):
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
    def csvPackage(self, nameIn, fishSpeciesIn, fishWeightIn, fishLengthIn, index):
        finalData = {
            'index': [0],
            'nameIn':nameIn,
            'fishSpeciesIn':fishSpeciesIn,
            'fishWeightIn':fishWeightIn,
            'fishLengthIn':fishLengthIn
        }
        df = pandas.DataFrame(finalData)
        df = df.set_index('index')
        df.to_csv('C:/Users/rwmac/Documents/Programming/WRFTApp/InProgress/WRFT.csv')
        print('\nDataFrame\n', df)
        #Find the last index of the df and make the next index
        index = (df.tail(1).index)+1
        print('\n',index, '\n')
        return df
        return index

    def build(self):
        return kivyFile

if __name__ == "__main__":
    MainApp().run()
