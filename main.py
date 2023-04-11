from kivymd.app import MDApp
from specialbuttons import LabelButton, ImageButton
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition, ScreenManager
#from kivy.uix.label import Label

from homemapview import HomeMapView
from homegpshelper import HomeGpsHelper
from final_preds import final_call

#from kivy.core.window import Window
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()



class HomeScreen(Screen):
    pass


class PredScreen(Screen):
    pass


class MainApp(MDApp):
    search_menu = None

    current_lat = 41.887620
    current_lon = -87.621230

    list1 = final_call(current_lat, current_lon)
    flat_list = [item for sublist in list1 for item in sublist]

    def on_start(self):
        # https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        # Initialize GPS
        HomeGpsHelper().run()

    #def navigation_draw(self, args):
        #print("Navigation")

    def change_screen(self, screen_name, direction='forward', mode=""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager

        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name

        #if screen_name == "home_screen":
        #    self.root.ids.titlename.title = "Urgent"


MainApp().run()