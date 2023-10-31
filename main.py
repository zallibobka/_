import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=250, spacing=50)
        self.add_widget(layout)

        label = Label(text='Это главный экран')
        layout.add_widget(label)

        button_tovar = Button(text='Товар', on_press=self.go_to_spisok_tovarov_screen)
        layout.add_widget(button_tovar)

        button_proiz = Button(text='Производитель', on_press=self.go_to_spisok_proiz_screen)
        layout.add_widget(button_proiz)

    def go_to_spisok_tovarov_screen(self, instance):
        self.manager.current = 'spisok_tovarov'

    def go_to_spisok_proiz_screen(self, instance):
        self.manager.current = 'spisok_proiz'

class SecondScreen_tov(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen_tov, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=250, spacing=50)
        self.add_widget(layout)

        label = Label(text='Это экран товаров')
        layout.add_widget(label)

        button = Button(text='Вернуться на главный экран', on_press = self.go_to_main_screen)
        layout.add_widget(button)

        connect = sqlite3.connect('resylk.db')
        cursor = connect.cursor()


    def go_to_main_screen(self, instance):
        self.manager.current = 'main'

class ThirdScreen_proiz(Screen):
    def __init__(self, **kwargs):
        super(ThirdScreen_proiz, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=250, spacing=50)
        self.add_widget(layout)

        label = Label(text='Это экран производителей')
        layout.add_widget(label)

        button = Button(text='Вернуться на главный экран', on_press = self.go_to_main_screen)
        layout.add_widget(button)

        connect = sqlite3.connect('resylk.db')
        cursor = connect.cursor()


    def go_to_main_screen(self, instance):
        self.manager.current = 'main'

class RibaKamApp(App):
    def build(self):
        return sm


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SecondScreen_tov(name='spisok_tovarov'))
sm.add_widget(ThirdScreen_proiz(name='spisok_proiz'))


if __name__ == '__main__':
    RibaKamApp().run()
