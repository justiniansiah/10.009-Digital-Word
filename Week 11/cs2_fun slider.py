from kivy.app import App
from kivy.uix.label import Label 

class SlideDetectApp(App):
	def build(self):
		main_label = Label(text = 'Slide me', font_size =72)
		main_label.bind(on_touch_move=self.detect)
		self.size = 72
		return main_label


	def detect(self, instance, touch):
		#if not instance.collide_point(touch.x, touch.y):
		#	return False
		print instance.text
		if touch.dx<-40:
			instance.text = 'Slide Left'
			instance.font_size = self.size
			self.size += 5
			
		if touch.dx>40:
			instance.text = 'Slide Right'
			instance.font_size = self.size
			self.size += 5
			
		if touch.dy<-40:
			instance.text = 'Slide Down'
			instance.font_size = self.size
			self.size += 5
			
		if touch.dy>40:
			instance.text = 'Slide Up'
			instance.font_size = self.size
			self.size += 5
			
		return True

if __name__=='__main__':
	SlideDetectApp().run()