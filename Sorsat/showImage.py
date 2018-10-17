### KIVY example to show image

from kivy.app import App
from kivy.uix.image import Image

class TutorialApp(App):
	def build(self):
		return Image(source='testiJuoma.png')
		
if __name__ == "__main__":
	TutorialApp().run()