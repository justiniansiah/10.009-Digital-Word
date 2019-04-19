
class Celsius(object): #must put xxxx(object)
    
    def __init__(self,temperature=0):
        self.temperature = temperature
    
    def to_fahrenheit(self):
        C = (self.temperature * 1.8) + 32
        return C
    
    #getters and setters    
    def get_temperature(self):
        return self._temperature
        
    def set_temperature(self, value):
        if value < -273:
            self._temperature = -273
        else:
            self._temperature = value
    
    
    temperature = property(get_temperature,set_temperature)  
    
    # # above line is same as the following 
    # temperature = property() # make empty property 
    # temperature = temperature.getter(get_temperature) # assign fget
    # temperature = temperature.setter(set_temperature) # assign fset    
    

c = Celsius()
print c.temperature

c.temperature = 32
print c.to_fahrenheit()

c.temperature = -300
print c.temperature
        

