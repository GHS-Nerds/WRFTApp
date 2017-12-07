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
    pass
class RecordCatchScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

kivyFile = Builder.load_file("main.kv")

class MainApp(App):

    def build(self):
        return kivyFile

if __name__ == "__main__":
    MainApp().run()
