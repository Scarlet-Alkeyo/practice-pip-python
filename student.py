# class Student:
#       name="Agnes"
#       school="Akirachix"
#       code=79
#       age=20



class Student:
    school="Akiarchix"

    def __init__(self,first_name,last_name,age,country,code):
         self.first_name=first_name
         self.last_name=last_name
         self.age=age
         self.country=country
         self.code=code

    def greet_student(self):
         greeting=f"Hello{self.first_name}, welcome to {self.school}.Your code is {self.code}"
         return greeting
    
    def year_birth(self):
         return f"Hello {self.first_name},you were born  in {2024-self.age}"
    
    def full_name(self):
         return f"Hello my fullname is {self.first_name} {self.last_name}"
    



student = Student("John", "Doe", 20, "USA", "JD123")


print(student.greet_student())

print(student.year_birth())

print(student.full_name())