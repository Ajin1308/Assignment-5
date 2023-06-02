class Student:
    def __init__(self):
        self.__name=""
        self.__rollnumber=""

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

student=Student()
student.setName("Ajin")
student.setRollNumber("10")
name=student.getName()
rollNumber=student.getRollNumber()
print("Name: ",name)
print("RollNumber: ",rollNumber)