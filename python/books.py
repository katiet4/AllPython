from kivy.app import App

from kivy.config import Config

from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.boxlayout import BoxLayout

import os

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#from kivy.uix.widget import Widget

Config.set('graphics','resizable',0)
Config.set('graphics','width',680)
Config.set('graphics','height',440)
class booksApp(App):
	def build(self):
		fl = FloatLayout(size = (680,440))
		self.tr=TextInput(size_hint=(None,None),pos=(0,40),size=(680,400),allow_copy = False,background_color = [0,0,0,0],foreground_color=[1,1,1,1] )
		self.tr.bind(focus=self.on_focus)
		self.to=TextInput(size_hint=(None,None),
							pos=(0,0),
							size=(410,40),
							font_size=24,
							multiline=False,
							allow_copy = False,
							background_color = [.4,.4,.4,.4],
							foreground_color=[1,1,1,1] )
		self.to.bind(focus=self.on_focus)

		fl.add_widget(self.tr)
		fl.add_widget(self.to)
		fl.add_widget(Button(text='Open',on_press=self.Open,size_hint=(None,None),pos=(500,0),size=(90,40)))
		fl.add_widget(Button(text='Save',on_press=self.Save,size_hint=(None,None),pos=(590,0),size=(90,40)))
		fl.add_widget(Button(text='Dir',on_press=self.Dir,size_hint=(None,None),pos=(410,0),size=(90,40)))
		return fl
	def Open(self,instance):
		self.alltext = ''
		try:
			with open(self.to.text,'a') as append:
				pass
			with open(self.to.text,'r') as read:
				for i in read:
					self.alltext += i
		except Exception as e:
			print("Error:",e)
		else:
			pass
		finally:
			pass
		self.tr.text = self.alltext
	def Save(self,instance):
		try:
			with open(self.to.text,'w') as write:
				print(self.tr.text,file = write)
		except Exception as e:
			print("Error:",e)
		finally:
			pass
	def Dir(self,instance):
		als=''
		try:
			if self.to.text == '':
				dirs = os.listdir()
				for d in dirs:
					als+=d+'\n'
			else:
				dirs = os.listdir(self.to.text)
				for d in dirs:
					als+=d+'\n'
		except Exception as e:
			print("Error:",e)
		else:
			pass
		finally:
			pass
		self.tr.text = als
	def on_focus(self,instance, value):
		print(value)