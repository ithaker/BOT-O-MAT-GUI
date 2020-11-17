import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenManagement(ScreenManager):
    pass

class SecondWindow(Screen):
    pass

class MyGrid(Widget):
    name = ObjectProperty()
    rtype = ObjectProperty()

    robot_name = StringProperty('')
    robot_type = StringProperty('')


    def submit_name(self):
        self.robot_name = self.name.text

    def btn(self):
        self.name.text = ""
        self.rtype.text = ""

class MyApp(App):
    title = "Bot-O-Mat"
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()