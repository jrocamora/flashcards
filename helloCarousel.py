import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage


class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right')
        
        src = "https://farm8.staticflickr.com/7404/10772400223_244bb727c6_z_d.jpg"
        image = AsyncImage(source=src, allow_stretch=True)
        carousel.add_widget(image)

        src = "https://farm6.staticflickr.com/5139/5519598097_e91d45b195_z_d.jpg"
        image = AsyncImage(source=src, allow_stretch=True)
        carousel.add_widget(image)

        src = "https://farm3.staticflickr.com/2920/33021716475_4fffb8f11a_z_d.jpg"
        image = AsyncImage(source=src, allow_stretch=True)
        carousel.add_widget(image)
        
        src = "https://farm1.staticflickr.com/271/20147143552_28affd24e7_z_d.jpg"
        image = AsyncImage(source=src, allow_stretch=True)
        carousel.add_widget(image)
        
        return carousel


CarouselApp().run()