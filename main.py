import os
import sys
import stmplib
import mimetypes

from argparse import ArgumentParser

from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
''' this is from https://docs.python.org/3/library/email-examples.html,
it imports stuff we need to send the test and image contents of a folder by email.
The code I added below, hopefully, if the button is tapped will email something, 
but we need to set variables for a WRFT server email, and a variable for the user and the folder on their system.
It also needs some sort of script while installing to make the folder, 
and for this script to place the fish types, photos etc. in the folder. 
I mentioned GPG in readme.md - this will improve security once it's implemented.
Useful info on that particular subject may be found at http://pythonhosted.org/gnupg/ and https://pypi.python.org/pypi/gnupg - J'''
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

COMMASPACE=', '

Builder.load_string("""
<homeScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'

<settingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")#not done yet - needs looking at

class homeScreen(Screen):
	pass

class settingsScreen(Screen):
	pass

class recordCatchScreen(Screen):
	def on_touch_down(self, touch):
		if self.collide_point(*touch.pos):			
			directory = '/etc/WRFT'
			# Create the enclosing (outer) message
			outer = MIMEMultipart()
			outer['Subject'] = 'Contents of directory %s' % os.path.abspath(directory)
			outer['To'] = 'GHSNerds@gmail.com'
			outer['From'] = args.sender				
				for filename in os.listdir(directory):
					path = os.path.join(directory, filename)
					if not os.path.isfile(path):
						continue
        					# Guess the content type based on the file's extension.  Encoding
        					# will be ignored, although we should check for simple things like
        					#gzip'd or compressed files.
						ctype, encoding = mimetypes.guess_type(path)
						if ctype is None or encoding is not None:
            						# No guess could be made, or the file is encoded (compressed), so
           						# use a generic bag-of-bits type.
							ctype = 'application/octet-stream'
							maintype, subtype = ctype.split('/', 1)
							if maintype == 'text':
								with open(path) as fp:
                						# Note: we should handle calculating the charset
								msg = MIMEText(fp.read(), _subtype=subtype)
								elif maintype == 'image':
									with open(path, 'rb') as fp:
										msg = MIMEImage(fp.read(), _subtype=subtype)
										else:
											with open(path, 'rb') as fp:
												msg = MIMEBase(maintype, subtype)
												msg.set_payload(fp.read())
            											# Encode the payload using Base64
												encoders.encode_base64(msg)
        											# Set the filename parameter
												msg.add_header('Content-Disposition', 'attachment', filename=filename)
												outer.attach(msg)
    												# Now send or store the message
												composed = outer.as_string()
												with smtplib.SMTP('localhost') as s
													s.sendmail(msg)
													s.quit()
													pass

class screenManagement(screenManagement):
	pass
	
class rootWidget(BoxLayout):
    	fishName = ObjectProperty()   
    	pass 


sm=ScreenManager()
sm.add_widget(Screen(name='homeScreen'))
sm.add_widget(Screen(name='settingsScreen'))
sm.add_widget(Screen(name='recordCatchScreen'))

class WRFTApp(App):
    	def build(self):
        return rootWidget()
	return sm

if __name__=="__main__":
	WRFTApp().run()
