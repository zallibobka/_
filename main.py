import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

data_product = []

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

        layout = BoxLayout(orientation='vertical', spacing=10)
        self.add_widget(layout)

        label = Label(text='Это экран товаров')
        layout.add_widget(label)

        connect = sqlite3.connect('resylk.db')
        cursor = connect.cursor()
        spisok = set()
        for i in cursor.execute('SELECT * FROM tovar').fetchall():
            #data_product.append(i[1])
            spisok.add(i[1])
        for elem in spisok:
            bt = Button(text=elem, on_press=self.go_to_product_screen)
            layout.add_widget(bt)

        button = Button(text='Вернуться на главный экран', on_press=self.go_to_main_screen)
        layout.add_widget(button)

    def go_to_product_screen(self, instance):
        self.manager.current = 'product'
    def go_to_main_screen(self, instance):
        self.manager.current = 'main'

class ResProductScreen(Screen):
    def __init__(self, **kwargs):
        super(ResProductScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=100, spacing=50)
        self.add_widget(layout)



        button = Button(text='Вернуться на главный экран', on_press=self.go_to_spisok_tovarov_screen)
        layout.add_widget(button)
    def go_to_spisok_tovarov_screen(self, instance):
        self.manager.current = 'spisok_tovarov'



class ThirdScreen_proiz(Screen):
    def __init__(self, **kwargs):
        super(ThirdScreen_proiz, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=50)
        self.add_widget(layout)

        label = Label(text='Это экран производителей')
        layout.add_widget(label)

        connect = sqlite3.connect('resylk.db')
        cursor = connect.cursor()

        for i in cursor.execute('SELECT * FROM proizv').fetchall():
            bt = Button(text=i[1], on_press=self.go_to_proizv_screen)
            layout.add_widget(bt)
        print(data_product)

        button = Button(text='Вернуться на главный экран', on_press=self.go_to_main_screen)
        layout.add_widget(button)

    def go_to_proizv_screen(self, instance):
        self.manager.current = 'proizv'

    def go_to_main_screen(self, instance):
        self.manager.current = 'main'

class ResProizvScreen(Screen):
    def __init__(self, **kwargs):
        super(ResProizvScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10)
        self.add_widget(layout)



        button = Button(text='Вернуться назад', on_press=self.go_to_spisok_proiz_screen)
        layout.add_widget(button)
    def go_to_spisok_proiz_screen(self, instance):
        self.manager.current = 'spisok_proiz'





class RibaKamApp(App):
    def build(self):
        return sm


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SecondScreen_tov(name='spisok_tovarov'))
sm.add_widget(ThirdScreen_proiz(name='spisok_proiz'))
sm.add_widget((ResProductScreen(name='product')))
sm.add_widget(ResProizvScreen(name='proizv'))



if __name__ == '__main__':
    RibaKamApp().run()
