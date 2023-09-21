#CLASSES

class Student():
    # data members
    # Name, phone, address
     
    # member functions
     #initialize the value of the variable,, init is called a constructor#
    def __init__(self): #underscores are important there are two underscores around _ _init_ _
        self.name = "asd"
        self.address = "la vasa"
        self.phone= 1234567890
    
    def printStudent(self):
        print("Name: {},\nAddress: {},\nPhone: {} ".format(self.name,self.address,self.phone))

    def _str_(self):
        pass

asd = Student()
asd.printStudent()


class Student1:
    def __init__(self,a,b):
        self.name = a
        self.stu_class = b 
#creating an object xyz
xyz = Student("Anthony", "MCA")
print(xyz.name, xyz.stu_class)
print(xyz)
print(type(xyz))


