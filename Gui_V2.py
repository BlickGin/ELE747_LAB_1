import kivy
kivy.require('1.0.2') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (400, 130)


class LblTxt(BoxLayout):
    from kivy.properties import ObjectProperty
    theTxt = ObjectProperty(None)


class MyApp(App):

    def build(self):
        self.root = Builder.load_file('simpleForm.kv')
        return self.root


if __name__ == '__main__':
    MyApp().run()
