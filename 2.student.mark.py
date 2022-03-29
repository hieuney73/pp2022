import Class

class Course:
  def_init_(self,id,name):
    self.id = id
    self.name = name

  def set_id(self,id):
    self._id = id
  def set_name(self,name):
    self._name = name
    
  def get_id(self):
    return self._id
  def get_name(self):
    return self._name

  def show_courseinfo(self):
      print(f"\n course's ID {self.get_id()}")
      print(f"\n course's name {self.get.name()}")

class Student:
  def__init__(self, student_id, student_name, student_DoB):
    self.id = student id
    self.name = student name
    self.DoB = student DoB

  def set_id(self,id):
    self._id = id
  def set_name(self,name):
    self._name = name
  def set_dob(self,DoB):
    self._DoB = DoB
    
  def get_id(self):
    return self._id
  def get_name(self):
    return self._name
  def get_DoB(self):
    return self._DoB

  def show_studentinfo(self):
      print(f"\n student's ID {self.get_id()}")
      print(f"\n student's name {self.get.name()}")
      print(f"\n student's DoB {self.get.Dob()}")

studentlist = []  
courselist = []
marks = []
run = True
while(True):
    print("\n 1.Return")
    print("\n 2.Add Student")
    print("\n 3.View Student List")
    print("\n 4.Add Course")
    print("\n 5.View Course List")
    print("\n 6.Add Mark")
    Select = input("Please select")
    if select == 1:
        print("\n Goodbye!")
        return
    if select == 2:
        print("\n Enter student's Info:")
        id = input("ID"); name = input("Name"); DoB = input("DoB")
        studentlist = Student()
    if select == 3:
        print("\n Student List:")
        for i in studentlist:
            i = i+1
    if select == 4:
        print("\n Enter course's Info:")
        id = input("ID"); name = input("Name")
        courselist = Course()
    if select == 5:
        print("\n The Course List:")
        for i in courselist:
            i = i+1
    if select == 6:
        print("\n Choose the course:")
        studentlist[].get_mark(mark)
        mark = input("Mark")
    else:
        print("\n Invalid Option!")

