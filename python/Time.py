
from kivy.app import App

from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

from kivy.config import Config

#from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock 
#import os
import datetime

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#from kivy.uix.widget import Widget

Config.set('graphics','resizable',0)
Config.set('graphics','width',680)
Config.set('graphics','height',440)

class TimeApp(App):
	def build(self):
		self.hours1=0
		self.minutes1=0
		self.seconds1=0
		fl = FloatLayout(size = (680,440))
		self.hours = TextInput(multiline=False,size_hint = (None,None),size=(100,60),font_size=40,pos=(170,300),text='0h')
		self.hours.bind(focus=self.on_focus)
		self.minutes = TextInput(multiline=False,size_hint = (None,None),size=(100,60),font_size=40,pos=(290,300),text='0m')
		self.minutes.bind(focus=self.on_focus)
		self.seconds = TextInput(multiline=False,size_hint = (None,None),size=(100,60),font_size=40,pos=(410,300),text='0s')
		self.seconds.bind(focus=self.on_focus)
		self.Go = Button(size_hint = (None,None),size=(100,60),pos=(290,180),text='Update',on_press=self.go_timer)
		fl.add_widget(self.hours)
		fl.add_widget(self.minutes)
		fl.add_widget(self.seconds)
		fl.add_widget(self.Go)
		return fl
			
	def go_timer(self,instance):
		self.hours.text = str(datetime.datetime.today().hour)+'h'
		self.seconds.text = str(datetime.datetime.today().second)+'s'
		self.minutes.text = str(datetime.datetime.today().minute)+'m'
	def on_focus(self,instance,value):
		if value:
			print(value)
		else:
			print(value)
if __name__ == '__main__':
	TimeApp().run()