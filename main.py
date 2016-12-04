import stmplib
from email.mime.text import MIMEText 
#https://docs.python.org/3/library/email-examples.html
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
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class homeScreen(Screen):
	pass

class settingsScreen(Screen):
	pass

class recordCatchScreen(Screen):
	pass

class screenManagement(screenManagement):
	pass
	
class rootWidget(BoxLayout):
    fishName = ObjectProperty()   
    pass 


class WRFTApp(App):
    def build(self):
        return rootWidget()       

if __name__=="__main__":
    WRFTApp().run()




















