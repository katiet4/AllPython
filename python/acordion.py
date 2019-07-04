from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.actionbar import ActionBar
Config.set('graphics','resizable',0)
Config.set('graphics','width',680)
Config.set('graphics','height',440)
class AccordionApp(App):
    def build(self):
        fl = Accordion(orientation='vertical',size = (300,300))
        ab = ActionBar()
        ab.add_widget(Button(text='hello',size_hint=(50,50)))
        return ab


if __name__ == '__main__':
    AccordionApp().run()