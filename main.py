import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.factory import Factory
from kivy.utils import boundary
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.audio import SoundLoader

from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Button(text='Record your catch')
    
    def recordCatch(catchList):
        """
        Go to screen with Collection points for Weight, photo, name of fish etc
        input the output of them to a Dictionary
        """
        
    def out2Database(catchList, serverNo):
        '''
        Change data from databases to outputtable form
        send data to database
        '''
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):  #touch.pos will e wherever the buttom is -RM
           recordCatch()
            pass
    
class TestApp(App):
    def build(self):
        return Button(text='Weather Forecast')

class TestApp(App):
    def build(self):
        return Button(text='Local Fishing Locations')


TestApp().run()
