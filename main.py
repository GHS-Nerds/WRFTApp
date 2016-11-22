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
from kivy.uix.screenmanager import ScreenManager, Screen, slideTransition

sm = ScreenManager(transition=SlideTransition())
kivySm = kivy.uix.screenmanager

catchRecord_screen = Screen(name='catchRecord')
sm.add_widget(catchRecord_screen)

class home_screen(Screen):
    '''
    This is where the setting up for buttons for the home screen goes
    '''
    pass

class catchRecord_screen(Screen):
    '''
    This is where the setting up for buttons for the home screen goes
    '''
    pass

class kivySm.TransitionBase()
    duration = .1
    isActive = True

class kivySm.SlideTransition()
    def right():
        direction = right
    def left():
        direction = left

sm.add_widget(home_screen(name='home'))
sm.add_widget(catchRecord_screen(name='home'))

class WRFT(App):
    def build(self):
        return Button(text='Record your catch')
    
    def recordCatch_process(catchList):
        """
        Clear screen
        Go to screen with Collection points for Weight, photo, name of fish etc [Populate screen]
        Input the output of them to a Dictionary
        """
        
    def out2Database(catchList, serverNo):
        '''
        Change data from databases to outputtable form
        Send data to database
        '''
    
    def weatherForcast_Detect(self, touch):
        if self.collide_point(*touch.pos):  #touch.pos will e wherever the buttom is -RM
           recordCatch()
            pass
    
    
class WRFT(App):
    def build(self):
        return Button(text='Weather Forecast')

class WRFT(App):
    def build(self):
        return Button(text='Local Fishing Locations')

sm.add_widget(home_screen(name='home'))
sm.add_widget(catchRecord_screen(name='home'))
WRFT().run()

