from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App


class MyLabel(Label):
    def __init__(self,**kwargs):
        Label.__init__(self,**kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding=(20,20)

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=BoxLayout()
        self.add_widget(self.layout)
        # Add your code below to add the two Buttons
        pass
        
        settings = Button(text="Settings", on_press=self.change_to_setting, font_size=24)
        self.layout.add_widget(settings)
        
        quit = Button(text="Quit", on_press=self.quit_app, font_size=24)
        self.layout.add_widget(quit)
    
    def change_to_setting(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
        self.manager.current= 'settings'

    def quit_app(self, value):
        App.get_running_app().stop()
        exit()



class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout=BoxLayout()
        self.add_widget(self.layout)
        # Add your code below to add the label and the button
        pass
        
        l1=MyLabel(text="Settings Screen",font_size=24,halign='center',valign='middle')
        self.layout.add_widget(l1)
        
        Menu = Button(text="Back to Menu", on_press=self.change_to_menu, font_size=24)
        self.layout.add_widget(Menu)
    

    def change_to_menu(self,value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
        self.manager.current= 'menu'



class SwitchScreenApp(App):
    def build(self):
            sm=ScreenManager()
            ms=MenuScreen(name='menu')
            st=SettingsScreen(name='settings')
            sm.add_widget(ms)
            sm.add_widget(st)
            sm.current='menu'
            return sm

if __name__=='__main__':
    SwitchScreenApp().run()
