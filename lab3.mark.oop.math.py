import numpy as np
import math
import curses


class student:
    def __init__(self,name,id,DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
    
    def get_name(self):
       
        return self.__name
   
    def get_id(self):
        
        return self.__id
   
    def get_DoB(self):
       
        return self.__DoB

studentlist =[]

def Student():
    return int(input("Enter number of student: "))

def GetStudentList():
    for i in range(Student()):
        Student_i = Student.GetInfo()   
        StudentList.append([Student_i.Name,ID,DoB,])

    for student in StudentList:
        print("")

class course:
    def __init__(self,name,id,credits):
        self.id = name
        self.name = id
        self.credits = credits

    def get_name(self):
        
        return self.__name
    
    def get_id(self):
        
        return self.__id
    
    def get_credits(self):
       
        return self.__credits


courselist = []


class mark:
    def GetMark():
    n = int(input("how many student you want to input mark: "))

    def roundmark(num):
    if math.floor(mark*10)/10
        return mark

    def testAvg(markslist):
        total = 0 
        for x in markslist:
            total = x
        average = total/len(markslist)
        return avg     
    
    
    for name in stu:
        credit = 0 
        total = 0 

    for x in stu[name]:
        credit += x[0]
        total += x[0]*x[1]
    stu_grade.append([name,total/credit])


markslist = []
def sorting():
n = int(input("tudent input ?")
ls = []
for i in range(0, n):
	x,y = input("Student's name and GPA: ").split()
	ls.append((y,x))
ls = sorted(ls, reverse = True)
print("Sorted list of students:")
for i in ls:
	print(i[1], i[0])
