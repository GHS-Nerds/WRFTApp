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

class homeScreen(Screen):
	pass

class settingsScreen(Screen):
	pass

class recordCatchScreen(Screen):
	def on_touch_down(self, touch):
		if self.collide_point(*touch.pos):
			parser = ArgumentParser(description="""\Send the contents of a directory as a MIME message.
Unless the -o option is given, the email is sent by forwarding to your local
SMTP server, which then does the normal delivery process.  Your local machine
must be running an SMTP server.""")
			#parser.add_argument('-d', '--directory',
                        #help="""Mail the contents of the specified directory,
                        #otherwise use the current directory.  Only the regular
                        #files in the directory are sent, and we don't recurse to
                        #subdirectories.""")
			parser.add_argument('-o', '--output',metavar='FILE',
                        help="""Print the composed message to FILE instead of
                        sending the message to the SMTP server.""")
			parser.add_argument('-s', '--sender', required=True,
                        help='The value of the From: header (required)')
			#parser.add_argument('-r', '--recipient', required=True,
                        #action='append', metavar='RECIPIENT',
                        #default=[], dest='recipients',
                        #help='A To: header value (at least one required)')
			args = parser.parse_args()
			directory = '/etc/WRFT'
			if not directory:
				directory = '.'
				# Create the enclosing (outer) message
				outer = MIMEMultipart()
				outer['Subject'] = 'Contents of directory %s' % os.path.abspath(directory)
				outer['To'] = COMMASPACE.join('GHSNerds@gmail.com')
				outer['From'] = args.sender
				outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
				
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
												if args.output:
													with open(args.output, 'w') as fp:
														fp.write(composed)
														else:
															with smtplib.SMTP('localhost') as s
															s.sendmail(args.sender, 'GHSNerds@gmail.com', composed)
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
