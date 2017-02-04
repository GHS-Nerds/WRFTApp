#!/usr/bin/kivy

import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, BooleanProperty

from plyer import email


class EmailInterface(GridLayout):
    
    def __init__(self, **kwargs):
        super(EmailInterface, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Recipient'))
        self.email_recipient = TextInput(multiline=False)
        self.add_widget(self.email_recipient)
        self.add_widget(Label(text='Subject'))
        self.email_subject = TextInput(multiline=False)
        self.add_widget(self.email_subject)
        self.add_widget(Label(text='Text'))
        self.email_text = TextInput(multiline=True)
        self.add_widget(self.email_text)
        self.sendbutton = Button(text='Send', font_size=14)
        self.sendbutton.bind(on_press=send_email)
        self.add_widget(self.sendbutton)


'''class IntentButton(Button):
    email_recipient = StringProperty()
    email_subject = StringProperty()
    email_text = StringProperty()
    create_chooser = BooleanProperty()'''

def send_email(self, **kwargs):
    email.send(recipient=self.email_recipient, subject=self.email_subject, text=self.email_text, create_chooser=self.sendbutton)


class EmailApp(App):
    def build(self):
        return EmailInterface()

    def on_pause(self):  
        return True

if __name__ == "__main__":
    EmailApp().run()
