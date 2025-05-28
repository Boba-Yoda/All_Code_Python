from course import Course

class Student:
    
    student_id = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1
    
    def __str__(self):
        getInput = self.last_name + ", " + self.first_name
        temp = ""
        temp += getInput + "\n"
        for eachCourse in self.courses: 
            temp += str(eachCourse)
            temp += "\n"
            
    
        return(temp)
        
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name
        
    def get_student_id(self):
        return self.student_id
    
    def add_course(self, new_course):
        self.courses.append(new_course)
        print ("Complete this based on what the program is doing here.")

#Only Name Code

"""
from course import Course

class Student:
    
    student_id = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1
    
    def get_name(self):
        
        getInput = self.first_name + " " + self.last_name
        
        return(getInput)
        
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name
        
    def get_student_id(self):
        return self.student_id
    
    def add_course(self, new_course):
        self.courses.append(new_course)
"""
