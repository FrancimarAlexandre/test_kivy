# import screens
from app.screens.home_screen import HomeScreen

if __name__ == "__main__":
    from kivy.app import App
    from kivy.core.window import Window
    class AppKivy(App):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            # configurações da janela
            Window.size = (400,600)
            Window.clearcolor = ("white")
            Window.title = "App kivy python gg do g"
        def build(self):
           return HomeScreen()


    AppKivy().run()