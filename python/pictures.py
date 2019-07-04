
from kivy.app import App

from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

from kivy.config import Config

from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.boxlayout import BoxLayout

#import os

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#from kivy.uix.widget import Widget

Config.set('graphics','resizable',0)
Config.set('graphics','width',680)
Config.set('graphics','height',440)

class picturesApp(App):
	def build(self):
		self.s = Scatter()
		self.fl = FloatLayout(size = (680,440))
		self.img = 'i4koX1r288g.jpg' 
		self.wimg = Image(source=self.img,pos = ((680/2-85),440/2))
		self.to=TextInput(size_hint=(None,None),
							pos=(0,0),
							size=(545,40),
							font_size=24,
							multiline=False,
							allow_copy = False)
		self.to.bind(focus=self.on_focus)
		self.s.add_widget(self.wimg)
		self.fl.add_widget(self.s)
		self.fl.add_widget(self.to)
		self.b1 = Button(text='Open',on_press=self.Open,size_hint=(None,None),pos=(545,0),size=(135,40))
		self.fl.add_widget(self.b1)
		return self.fl
	def remove(self):
		self.fl.remove_widget(self.b1)
		self.fl.remove_widget(self.b2)
		self.fl.remove_widget(self.s)
		self.fl.remove_widget(self.to)
	def Open(self,instance):
		self.alltext = ''
		try:
			self.img=self.to.text
			self.wimg.source=self.img
		except Exception as e:
			print("Error:",e)
		else:
			pass
		finally:
			pass
	def on_focus(self,instance, value):
		print(value)