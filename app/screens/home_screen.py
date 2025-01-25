from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 

class HomeScreen(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="INICIAR", background_color = 'blue',pos_hint={"center_x":0.5,"center_y":0.5},size_hint=(0.3,0.1),on_press = self.Home))

    # def Home(self,instance):
    #     self.add_widget(Label(text="Sejam bem-vindos",color="black"))