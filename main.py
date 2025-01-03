from kivy.app import App
from kivy.uix.button import Button

class AppTest(App):
    def build(self):
        return Button(text="hello world")


AppTest().run()