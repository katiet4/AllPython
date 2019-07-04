from kivy.app import App

from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

from re import *

from math import pow

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

class codeApp(App):
	def build(self):
		fl = FloatLayout(size=(680,440))
		self._2 = TextInput(size_hint = (None,None),size=(325,150),pos=(10,280))
		self._2.bind(focus=self.on_focus)
		self._8 = TextInput(size_hint = (None,None),size=(325,150),pos=(345,280))
		self._8.bind(focus=self.on_focus)
		self._10 = TextInput(size_hint = (None,None),size=(325,160),pos=(10,60))
		self._10.bind(focus=self.on_focus)
		self._16 = TextInput(size_hint = (None,None),size=(325,160),pos=(345,60))
		self._16.bind(focus=self.on_focus)
		B2 = Button(text="2",size_hint = (None,None),size=(80,40),pos=((325/2/1.4+10),230),on_press=self.But2)
		B8 = Button(text="8",size_hint = (None,None),size=(80,40),pos=((325/2/1.4+10+325),230),on_press=self.But8)
		B10 = Button(text="10",size_hint = (None,None),size=(80,40),pos=((325/2/1.4+10),10),on_press=self.But10)
		B16 = Button(text="16",size_hint = (None,None),size=(80,40),pos=((325/2/1.4+10+325),10),on_press=self.But16)
		fl.add_widget(self._2)
		fl.add_widget(self._8)
		fl.add_widget(self._10)
		fl.add_widget(self._16)
		fl.add_widget(B2)
		fl.add_widget(B8)
		fl.add_widget(B10)
		fl.add_widget(B16)
		self.stat_2 = compile('(^|\s)[0-1.]{1,1000}(\s|$)') 
		self.stat_8 = compile('(^|\s)[0-7.]{0,1000}(\s|$)') 
		self.stat_10 = compile('(^|\s)[0-9.]{0,1000}(\s|$)') 
		self.stat_16 = compile('(^|\s)[ABCDEFGabcdefg0-9.]{0,1000}(\s|$)') 
		self.charac = {
						'A':10,
						'B':11,
						'C':12,
						'D':13,
						'E':14,
						'F':15,
		}
		return fl

	def But2(self,instance):
		try:
			textpol = self._2.text.split('.')
			text = self._2.text
			val = self.stat_2.match(text)
			if val:
				arrsu = len(textpol[0])
				r=arrsu-1
				summ=0
				for i in text:
					if i == '.':
						pass
					else:
						t = int(i)
						po = pow(2,r)
						summ+=float(t)*po
						r=r-1
				self._10.text=str(summ)
				self.allcode()
			else:
				print("Error")
		except Exception as e:
			print("Error",e)

	def But8(self,instance):
		try:
			textpol = self._8.text.split('.')
			text = self._8.text
			val = self.stat_8.match(text)
			if val:
				arrsu = len(textpol[0])
				r=arrsu-1
				summ=0
				for i in text:
					if i == '.':
						pass
					else:
						t = int(i)
						po = pow(8,r)
						summ+=float(t)*po
						r=r-1
				self._10.text=str(summ)
				self.allcode()
			else:
				print("Error")
		except Exception as e:
			print("Error",e)

	def But10(self,instance):
		self.allcode()

	def But16(self,instance):
		try:
			textpol = self._16.text.split('.')
			text = self._16.text
			val = self.stat_16.match(text)
			if val:
				arrsu = len(textpol[0])
				r=arrsu-1
				summ=0
				for i in text:
					if i == '.':
						pass
					else:
						if (i != '0' and
							i != '1' and
							i != '2' and
							i != '3' and
							i != '4' and
							i != '5' and
							i != '6' and
							i != '7' and
							i != '8' and
							i != '9'):
							i=i.upper()
							t = self.charac[i]
						else:
							t = int(i)
						po = pow(16,r)
						summ+=float(t)*po
						r=r-1
				self._10.text=str(summ)
				self.allcode()
			else:
				print("Error")
		except Exception as e:
			print("Error",e)

	def on_focus(self,instance,value):
		print(value)
		
	def allcode(self):
		try:
			text = self._10.text
			val = self.stat_10.match(text)
			if val:
				inpu = self._10.text
				_2 = ''
				t = inpu.split('.')
				num = int(t[0])
				while (num>=2):
					if ((num%2)==1):
						_2+='1'
						num-=1
					else:
						_2+='0'
					num/=2
					num=int(num)
				if(num == 0):
					pass
				else:
					_2+='1'
				_2end = ''
				back = -1	
				for i in _2:
					_2end+=_2[back]
					back-=1
				endtwo = ''
				two = ''
				lengtharr = len(t)
				if lengtharr==1:
					t.append('0')
				if t[1]=='':
					t[1]='0'
				length = len(t[1])
				numstr=int(t[1])
				numster = '1'+('0'*length)
				numsterint= int(numster)
				test = str(numstr/numsterint)
				num2=float(test)
				for i in range(length):
					integet = round(num2)
					if (integet == 1):
						two+='1'
					else:
						two+='0'
					num2 = float(num2*2)
					if _2end == '':
						_2end='0'
					TheEnd = _2end+'.'+two
				self._2.text=TheEnd

				_2 = ''
				t = inpu.split('.')
				num = int(t[0])
				while (num>=8):
					_2+=str((num%8))
					num/=8
					num=int(num)
				_2+=str(num)
				_8end = ''
				back = -1	
				for i in _2:
					_8end+=_2[back]
					back-=1
				lengtharr = len(t)
				if lengtharr==1:
					t.append('0')
				if t[1]=='':
					t[1]='0'
				theend = ''
				length = len(t[1])
				numstr=int(t[1])
				numster = '1'+('0'*length)
				numsterint= int(numster)
				test = numstr/numsterint
				endint = test
				for i in range(length):
					summ=(endint*8)
					end = int(summ)
					if end != 0:
						theend+=str(end)
						endint = summ-end
					else:
						theend+=str(end)
						endint = summ
				if theend == '':
					theend = '0'
				Theend = _8end+'.'+theend
				self._8.text=Theend

				_2 = ''
				t = inpu.split('.')
				code = {
					'10':'A',
					'11':'B',
					'12':'C',
					'13':'D',
					'14':'E',
					'15':'F'
					}
				num = int(t[0])
				while (num>=16):
					one = (num%16)
					if one > 9:
						string = str(one)
						_2+=code[string]
					else:
						_2+=str(one)
					num/=16
					num=int(num)
				if num > 9:
					string = str(num)
					_2+=code[string]
				else:
					_2+=str(num)
				_16end = ''
				back = -1	
				for i in _2:
					_16end+=_2[back]
					back-=1

				lengtharr = len(t)
				if lengtharr==1:
					t.append('0')
				if t[1]=='':
					t[1]='0'
				theend = ''
				length = len(t[1])
				numstr=int(t[1])
				numster = '1'+('0'*length)
				numsterint= int(numster)
				test = numstr/numsterint
				endint = test
				for i in range(length):
					summ=(endint*16)
					end = int(summ)
					if end != 0:
						if end >=10:
							number = str(end)
							r = code[number]
							theend+=str(r)
						else:
							theend+=str(end)
						endint = summ-end
					else:
						theend+=str(end)
						endint = summ
				if theend == '':
					theend = '0'
				Theend = _16end+'.'+theend
				self._16.text=Theend
			else:
				print('Error')
		except Exception as e:
			print('Error:',e)