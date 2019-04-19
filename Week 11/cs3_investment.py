from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 

class MyLabel(Label):
	def __init__(self,**kwargs):
		Label.__init__(self,**kwargs)
		self.bind(size=self.setter('text_size'))
		self.padding=(20,20)
		self.font_size=24
		self.halign='center'
		self.valign='middle'


class Investment(App):

	def build(self):
		layout= GridLayout(cols=2,row_force_default=True, row_default_height=40)
		
		l1=MyLabel(text="Investment Amount")
		layout.add_widget(l1)
		
		self.t1 = TextInput(text = "0", multiline = False,width=150)
		layout.add_widget(self.t1)
		
		l2=MyLabel(text="Monthly Interest Rate")
		layout.add_widget(l2)
		
		self.t2 = TextInput(text = "0", multiline = False,width=150)
		layout.add_widget(self.t2)
		
		l3=MyLabel(text="Years")
		layout.add_widget(l3)
		
		self.t3 = TextInput(text = "0", multiline = False,width=150)
		layout.add_widget(self.t3)

		pass 
		
		
		l4=MyLabel(text="Future Value")
		layout.add_widget(l4)
		
		self.l5=MyLabel(text="$0.00",width=150)
		layout.add_widget(self.l5)
		
		pass
		
		btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
		layout.add_widget(btn)
		
		exit = Button(text="Exit", on_press=self.quit_app, font_size=24)
		layout.add_widget(exit)
		
		
		return layout 

	def calculate(self, instance):
		inv_amt = float(self.t1.text)
		years = float(self.t3.text)
		mth_int_rate = float(self.t2.text)
		self.txt_future_val=inv_amt*(1+mth_int_rate)**(12*years)
		self.l5.text = "$%.2f" %(self.txt_future_val)
		
	def quit_app(self, value):
		App.get_running_app().stop()
		exit()



Investment().run()