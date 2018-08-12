from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

import random

class FlipACoinApp(App):
    image = Image(source = 'CanadianToonieTails.png', size = (50, 50))

    def build(self):
        self.image.bind(on_touch_down = self.callback)
        boxLayout = BoxLayout(orientation = 'vertical')
        boxLayout.add_widget(self.image)
        return boxLayout
 
    def callback(self, value, a):
        head = random.choice([True, False])
        if (head):
            self.image.source = 'CanadianToonieHead.png'
        else:
            self.image.source = 'CanadianToonieTails.png'

if __name__ == '__main__':
    FlipACoinApp().run()