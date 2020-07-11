class Student:
     
#__init__() 是类的初始化方法；它在类的实例化操作后 会自动调用，不需要手动调用； 
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
         

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        
   