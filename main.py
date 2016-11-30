import kivy
from kivy.uix.button import Button
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput

class rootWidget(BoxLayout):
    fishName = ObjectProperty()   
    pass 


class WRFTApp(App):
    def build(self):
        return rootWidget()       

if __name__=="__main__":
    WRFTApp().run()




















