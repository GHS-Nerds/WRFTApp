#!/usr/bin/python

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty, BooleanProperty

from plyer import email


class EmailInterface(BoxLayout):
    pass


class IntentButton(Button):
    email_recipient = StringProperty()
    email_subject = StringProperty()
    email_text = StringProperty()
    create_chooser = BooleanProperty()

    def send_email(self, *args):
        email.send(recipient=self.email_recipient,
                   subject=self.email_subject,
                   text=self.email_text,
                   create_chooser=self.create_chooser)


class EmailApp(App):
    def build(self):
        return EmailInterface()

    def on_pause(self):
        return True

if __name__ == "__main__":
	EmailApp().run()
