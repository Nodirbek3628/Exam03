class Student:
    
    def __init__(self,name,age,kurs):
        self.name = name
        self.age = age
        self.kurs = kurs 

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, studying in {self.kurs}nd course."
    
student = Student("Ali",20,2)
print(student.introduce())