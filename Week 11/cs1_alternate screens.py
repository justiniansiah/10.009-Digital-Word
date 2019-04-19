from kivy.app import App 
from kivy.uix.label import Label  

class AlternateApp(App):
	
	def build(self):
		self.main_label = Label(text='Programming is fun.',font_size = 72,on_touch_down = self.alternate)
		self.state = 0
		return self.main_label

	def alternate(self,instance, touch):
		print "clicked"
		if self.state == 0:
			self.main_label.text = 'It is fun to program.'
			self.state = 1
		else:
			self.main_label.text = 'Programming is fun.'
			self.state = 0
		print self.main_label.text
		

myapp=AlternateApp()
myapp.run()