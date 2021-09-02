from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


def on_press(btn):
    btn.text = 'Apertado'


def on_release(btn):
    btn.text = 'Solto'


class MyApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        label = Label(text='Olá Mundo !')
        label.font_size = 50
        btn = Button(
            text='Botão', 
            on_press=on_press,
            on_release=on_release)

        btn.font_size = 50
        box.add_widget(label)
        box.add_widget(btn)
        return box

MyApp().run()
