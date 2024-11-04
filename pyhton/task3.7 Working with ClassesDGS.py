##Class Person
class Person:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f"(id={self.id} name={self.name} age={self.age})"

##Class Student
class Student:
    def __init__(self,id,person,degree):
        self.id=id

        if(type(person)!=Person):
            raise Exception("The Student needs to be of the Person class")
        else:
            self.person = person

        self.degree = degree

    def __str__(self):
        return f"\t[id={self.id} info={self.person} degree={self.degree}]\n"

##Class StudentGroup
class StudentGroup:
    def __init__(self,id,groupName,students):
        self.id = id
        self.groupName = groupName

        if(isinstance(students,list)):
            self.students = students
        else:
            raise Exception("The Students atribute needs to be a list of students")

    def __str__(self):
        toString = f'StudenGroup (\nid = {self.id} \ngroupName ="{self.groupName}" \nStudents:\n'
        for student in self.students:
            toString+=str(student)
        return toString+")"

##CÓDIGO
student1 = Student(1,Person(3,"Jorge",23),"ciencias")
student2 = Student(2,Person(2,"Victor",24),"biología")
student3 = Student(3,Person(1,"Héctor",18),"economía")

print(student1.person.id)
print(student1.person.age)
print(student1.person.name)

Group1 = StudentGroup(1,"GROUP ONE",[student1,student2,student3])

print("*** IMPRIMIMOS EL GRUPO POR PRIMERA VEZ ***")
print(Group1)

Group1.students.pop(0)

print("*** ELIMINAMOS UN ESTUDIANTE ***")
print(Group1)

Group1.students.append(Student(4,Person(4,"Manuel",20),"DAW"))


print("*** AÑADIMOS UN ESTUDIANTE ***")
print(Group1)

try:
    student5 = Student(5,"Prueba","economía")
except Exception as erro:
    print(erro)

try:
    Group1 = StudentGroup(2,"GROUP TWO",student1)
except Exception as erro:
    print(erro)