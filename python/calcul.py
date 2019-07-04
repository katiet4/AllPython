from kivy.app import App

from kivy.config import Config

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.boxlayout import BoxLayout

#import os

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#from kivy.uix.widget import Widget

Config.set('graphics','resizable',0)
Config.set('graphics','width',680)
Config.set('graphics','height',440)

class colculatorApp(App):
	def build(self):
		self.t = TextInput(text = '0',size_hint=(None,None),pos=(0,300),size = (680,140))
		fl = FloatLayout(size = (300,300))
		fl.add_widget(self.t)
		gl = GridLayout(cols = 4,pos=(0,0),padding=[0,180,0,0],size_hint=(1.3,1.09))
		fl.add_widget(gl)
		gl.add_widget(Button(text = str(1),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = str(2),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = str(3),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = '+',on_press=self.plus,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = str(4),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = str(5),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = str(6),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = '-',on_press=self.minus,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = str(7),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = str(8),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = str(9),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = '=',on_press=self.result,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = '*',on_press=self.proisv,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = str(0),on_press=self.hellos,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = '/',on_press=self.dilen,size_hint=(None,None),size=(170,75)))
		gl.add_widget(Button(text = 'Clear',on_press=self.clear,size_hint=(None,None),size=(85,75)))
		fl.add_widget(Button(text = '.',on_press=self.hellos,size_hint=(None,None),size=(85,75),pos = (595,0)))
		self.make = '+'
		self.do = 0
		self.number_one = 0
		self.number_two = 0
		return fl
	def result(self,instance):
		try:
			if self.t.text == "":
				self.t.text = '0'
			num = float(self.t.text)
			self.t.text = '0'
			self.number_two = num
			res = 0
			resstr = '0'
			if self.make == "*":
				res = self.number_two * self.number_one
				resstr=str(res)
			elif self.make == "/":
				res = int(self.number_one / self.number_two)
				resstr=str(res)
			elif self.make == "-":
				res = self.number_one - self.number_two
				resstr=str(res)
			elif self.make == "+":
				res = self.number_one + self.number_two
				resstr=str(res)
			elif self.make == "clear":
				resstr='0'
			self.number_two = 0
			self.number_one = 0
			self.t.text=resstr
			self.do = 0
		except Exception as e :
			print('Error',e)
	def proisv(self,instance):
		try:
			if self.do == 1:
				pass
			else:
				num = float(self.t.text)
				self.t.text = '0'
				self.number_one = num
				self.make = '*'
			self.do = 1
		except Exception as e :
			print('Error',e)
	def clear(self,instance):
		try:
			self.t.text = '0'
			num = float(self.t.text)
			self.number_one = num
			self.make = 'clear'
			self.do = 0
		except Exception as e :
			print('Error',e)
	def dilen(self,instance):
		try:
			if self.do == 1:
				pass
			else:
				num = float(self.t.text)
				self.t.text = '0'
				self.number_one = num
				self.make = '/'
			self.do = 1
		except Exception as e :
			print('Error',e)
	def minus(self,instance):
		try:
			if self.do == 1:
				pass
			else:
				num = float(self.t.text)
				self.t.text = '0'
				self.number_one = num
				self.make = '-'
			self.do = 1
		except Exception as e :
			print('Error',e)
	def plus(self,instance):
		try:
			if self.do == 1:
				pass
			else:
				num = float(self.t.text)
				self.t.text = '0'
				self.number_one = num
				self.make = '+'
			self.do = 1
		except Exception as e :
			print('Error',e)
	def hellos(self,instance):
		try:
			if instance.text=='.':
				i = '.'
				string = self.t.text
				if i in string:
					pass
				else:
					self.t.text+=instance.text
			else:
				self.t.text+=instance.text
		except Exception as e :
			print('Error',e)