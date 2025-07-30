number_output = 1

#This is a simple class definition in Python
#The class is named Student and it has an __init__ method to initialize the attributes
#It also has a display method to return a formatted string with the student's details
#We can create a null constructor 
#but it is not necessary in this case since Python provides a default constructor
#def __init__(self):
#  pass

class Student:
    def __init__ (self, name=None, age=None):
        self.name = name
        self.age = age

    #Setters and getters for name and age attributes
    #These methods allow us to set and get the values of the attributes
    #This is a common practice in object-oriented programming to encapsulate the attributes
    #and provide controlled access to them.
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def display(self):
        return f"This student's name is {self.name}, {self.age} years old."
    
    @classmethod
    def default_student(cls):
        return cls("Default Name", 18)

class GoodStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age) #Call the parent class constructor, init name and age
        self.grade = grade

    def display(self): #Override the display method to include grade information
        return f"This good student is named {self.name}, {self.age} years old. His grade is {self.grade}."
    
#Creating instances of the Student class
student_a = Student("Cuong", 21)
print(student_a.display())

student_b = Student.default_student()
print(student_b.display())

student_c = Student()
student_c.set_name("John")
student_c.set_age(20)
print(student_c.display())


#Creating an instance of the GoodStudent class
#This class inherits from Student and adds a grade attribute
#It also overrides the display method to include the grade information
cuong = GoodStudent("Cuong", 21, "A")
print(cuong.display())



