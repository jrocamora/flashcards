import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyGridApp(App):

    def build(self):
        
        layout = GridLayout(cols=2)
        layout.add_widget(Button(text='Granja'))
        layout.add_widget(Button(text='Anadir categoria'))


        return layout


if __name__ == '__main__':
    MyGridApp().run()