class student:
    def __init__(self,IEP,gender,learningSpeed,name):
        self.IEP = IEP
        self.learningSpeed = learningSpeed
        self.gender = gender
        self.name = name
        self.noGroups = []

class group:
    def __init__(self):
        self.sum = 0

class sort:
    def __init__(self,quantity,filters,type):
        self.listOfStudents = []
        self.quantity = quantity
        self.filters = []
        self.type = "heterogenous"

    def addStudent(self,student):
        self.listOfStudents.add(student)

    def makeGroups(self,attribute,quant):
        allGroups = []
        for x in quant:
            allGroups.append(group())
        for student in self.listOfStudents:
            for x in range(0,len(allGroups)):
                if (sum(allGroups[x].sum)>=all(sum(allGroups).sum)):
                    allGroups[x].append(student)
                    break



