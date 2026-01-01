"""
Docstring for OOPs.Student

    The Student Management System is a simple object-oriented application designed to manage student records efficiently. The system allows users to store, view, update, and manage student information such as name, roll number, and academic performance. It is built using Object-Oriented Programming (OOP) principles to ensure clean structure, reusability, and scalability.
    
"""

class Student :
    number_of_student = 0
    def __init__(self,rollno,name,age,gender,percentage):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.gender = gender
        self.percentage = percentage
        Student.number_of_student += 1
        
    
    
s1 = Student(1,"shubham",21,"male",85)
s2 = Student(2,"harsh",25,"male",85)


print(Student.number_of_student)
        
    