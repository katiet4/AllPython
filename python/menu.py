from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.base import stopTouchApp
from updateFiles import updateFilesApp
from XandO import XandOApp
from calcul import colculatorApp
from books import booksApp
from pictures import picturesApp
from code import codeApp

from kivy.config import Config

Config.set('graphics','resizable',0)
Config.set('graphics','width',680)
Config.set('graphics','height',440)

class menuApp(App):
	def build(self):
		self.title = "Menu"
		self.al = AnchorLayout(anchor_x='right', anchor_y='bottom',padding=[160,85,0,0])
		self.gl = GridLayout(cols = 2)
		self.b1 = Button(text = 'Редактор \n файлов',size_hint = (None,None),size = (180,90), on_press = self.update)
		self.b2 = Button(text = 'Калькулятор',size_hint = (None,None),size = (180,90), on_press = self.calculator)
		self.b3 = Button(text = 'X и O',size_hint = (None,None),size = (180,90), on_press = self.XandO)
		self.b4 = Button(text = 'Книги',size_hint = (None,None),size = (180,90), on_press = self.books)
		self.b5 = Button(text = 'Картинки',size_hint = (None,None),size = (180,90), on_press = self.pictures)
		self.b6 = Button(text = 'Кодировки',size_hint = (None,None),size = (180,90), on_press = self.code)
		self.gl.add_widget(self.b1)
		self.gl.add_widget(self.b2)
		self.gl.add_widget(self.b3)
		self.gl.add_widget(self.b4)
		self.gl.add_widget(self.b5)
		self.gl.add_widget(self.b6)
		self.al.add_widget(self.gl)
		return self.al
	def remove(self):
		self.gl.remove_widget(self.b1)
		self.gl.remove_widget(self.b2)
		self.gl.remove_widget(self.b3)
		self.gl.remove_widget(self.b4)
		self.gl.remove_widget(self.b5)
		self.gl.remove_widget(self.b6) 
	def update(self,instance):
		self.remove()
		menuApp().stop()
		updateFilesApp().run()
	def calculator(self,instance):
		self.remove()
		menuApp().stop()
		colculatorApp().run()
	def XandO(self,instance):
		self.remove()
		menuApp().stop()
		XandOApp().run()
	def books(self,instance):
		self.remove()
		menuApp().stop()
		booksApp().run()
	def pictures(self,instance):
		self.remove()
		menuApp().stop()
		picturesApp().run()
	def code(self,instance):
		self.remove()
		menuApp().stop()
		codeApp().run()
if __name__ == "__main__":
	menuApp().run()