from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager , Screen

class MenuScreen(Screen) :
    def __init__(self,**kwargs) :
        super(MenuScreen,self).__init__(**kwargs)
        self.fl = BoxLayout(orientation = "vertical")
        #Кнопка на которую нужно нажать
        self.but_open = Button (text = "нажми на меня",size_hint = (None,None) ,size = (600,40),pos = (20,50),on_press = self.ButtonOpen)
        self.fl.add_widget(self.but_open)

     def ButtonOpen(self):
         self.but_open1 = Button (text = "кнопка1",size_hint = (None,None) ,size = (600,40),pos = (20,100))
         self.but_open2 = Button (text = "Не жми на меня",size_hint = (None,None) ,size = (600,40),pos = (20,150))
         self.fl.add_widget(self.but_open1)
         #Аналогично пишем сюда и другие кнопки

class MyApp() :
    def build(self):
        manager = ScreenManager()
    	manager.add_widget(MenuScreen(name = 'menu'))
    	return manager

if __name__ == '__main__' :
    MyApp().run()
