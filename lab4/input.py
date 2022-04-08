import numpy as np
import math
import curses
from curses import wrapper

def Student():

    return int(input("Enter number of student: "))

def GetStudentList():

    for i in range(Student()):

        Student_i = Student.GetInfo() 
  
        StudentList.append([Student_i.Name,ID,DoB,])

    for student in StudentList:

        print("")


def GetMark():

    n = int(input("how many student you want to input mark: "))

    def roundmark(num):

    if math.floor(mark*10)/10

        return mark


def sorting():

n = int(input("tudent input ?")

ls = []

for i in range(0, n):

	x,y = input("Student's name and GPA: ").split()

	ls.append((y,x))

ls = sorted(ls, reverse = True)

print("Sorted list of students:")

