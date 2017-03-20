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
    pass

class ScreenManagement(ScreenManager):
    pass


kivyFile = Builder.load_file("main.kv")

class MainApp(App):
    
    def build(self):
        return kivyFile

if __name__ == "__main__":
    MainApp().run()
