from kivy.app import App

from kivy.config import Config

#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.boxlayout import BoxLayout

import os

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#from kivy.uix.widget import Widget
Config.set('graphics','resizable',0)
Config.set('graphics','width',680)
Config.set('graphics','height',440)
class XandOApp(App):
	def build(self):
		self.title = "X and O"
		self.game = 'X'
		gl = GridLayout(cols = 3,padding =[145,25,0,0],spacing = -3)
		self.button1=Button(text= "?",size_hint=(None,None),size =(130,130),on_press=self.but)
		self.button2=Button(text= "?",size_hint=(None,None),size =(130,130),on_press=self.but)
		self.button3=Button(text= "?",size_hint=(None,None),size =(130,130),on_press=self.but)
		self.button4=Button(text= "?",size_hint=(None,None),size =(130,130),on_press=self.but)
		self.button5=Button(text= "?",size_hint=(None,None),size =(130,130),on_press=self.but)
		self.button6=Button(text= "?",size_hint=(None,None),size =(130,130),on_press=self.but)
		self.button7=Button(text= "?",size_hint=(None,None),size =(130,130),on_press=self.but)
		self.button8=Button(text= "?",size_hint=(None,None),size =(130,130),on_press=self.but)
		self.button9=Button(text= "?",size_hint=(None,None),size =(130,130),on_press=self.but)
		gl.add_widget(self.button1)
		gl.add_widget(self.button2)
		gl.add_widget(self.button3)
		gl.add_widget(self.button4)
		gl.add_widget(self.button5)
		gl.add_widget(self.button6)
		gl.add_widget(self.button7)
		gl.add_widget(self.button8)
		gl.add_widget(self.button9)
		return gl
	def re(self):
		self.button1.text='?'
		self.button2.text='?'
		self.button3.text='?'
		self.button4.text='?'
		self.button5.text='?'
		self.button6.text='?'
		self.button7.text='?'
		self.button8.text='?'
		self.button9.text='?'
	def but(self,instance):
		if instance.text == '?':
			instance.text = self.game
			if self.game == 'X':
				self.game='O'
			else:
				self.game='X'
			if(self.button1.text == "X" and self.button5.text == "X" and self.button9.text == "X"):
				print('X won!')
				self.re()
			elif(self.button1.text == "O" and self.button5.text == "O" and self.button9.text == "O"):
				print("O won!")
				self.re()
			elif(self.button1.text == "X" and self.button2.text == "X" and self.button3.text == "X"):
				print("X won!")
				self.re()
			elif(self.button1.text == "O" and self.button2.text == "O" and self.button3.text == "O"):
				print("O won!")
				self.re()
			elif(self.button1.text == "X" and self.button4.text == "X" and self.button7.text == "X"):
				print("X won!")
				self.re()
			elif(self.button1.text == "O" and self.button4.text == "O" and self.button7.text == "O"):
				print("O won!")
				self.re()
			elif(self.button7.text == "X" and self.button8.text == "X" and self.button9.text == "X"):
				print("X won!")
				self.re()
			elif(self.button7.text == "O" and self.button8.text == "O" and self.button9.text == "O"):
				print("O won!")
				self.re()
			elif(self.button3.text == "X" and self.button6.text == "X" and self.button9.text == "X"):
				print("X won!")
				self.re()
			elif(self.button3.text == "O" and self.button6.text == "O" and self.button9.text == "O"):
				print("O won!")
				self.re()
			elif(self.button3.text == "X" and self.button5.text == "X" and self.button7.text == "X"):
				print("X won!")
				self.re()
			elif(self.button3.text == "O" and self.button5.text == "O" and self.button9.text == "O"):
				print("O won!")
				self.re()
			elif(self.button2.text == "X" and self.button5.text == "X" and self.button8.text == "X"):
				print("X won!")
				self.re()
			elif(self.button2.text == "O" and self.button5.text == "O" and self.button8.text == "O"):
				print("O won!")
				self.re()
			elif(self.button4.text == "X" and self.button5.text == "X" and self.button6.text == "X"):
				print("X won!")
				self.re()
			elif(self.button4.text == "O" and self.button5.text == "O" and self.button6.text == "O"):
				print("O won!")
				self.re()
			else:
				print("-------")
			if (self.button1.text != "?" and
				self.button2.text != "?" and 
				self.button3.text != "?" and
				self.button4.text != "?" and
				self.button5.text != "?" and 
				self.button6.text != "?" and
				self.button7.text != "?" and
				self.button8.text != "?" and 
				self.button9.text != "?"):
				self.re()
				print("Nicic!")
		else:
			print('Error')