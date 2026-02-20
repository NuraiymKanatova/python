class Student:
    school = "NIS"            # class variable (общая)
    count = 0                 # class variable (общая)

    def __init__(self, name):
        self.name = name      # instance variable (личная)
        Student.count += 1    # change class variable to instance variable

s1 = Student("Aruzhan")
s2 = Student("Daniyar")

print(s1.name, s2.name)       # different values
print(s1.school, s2.school)   # same values (NIS)
print(Student.count)          # 2



# если присвоить s1.school = ..., то переменная класса не поменяется 
# а создастся экземпляр переменной с тем же именем, которая "перекроет" общую

class Student:
    school = "NIS"

s1 = Student()
s2 = Student()

s1.school = "KTL"             # created instance variable only for s1

print(s1.school)              # KTL (took from object)
print(s2.school)              # NIS (took from class)
print(Student.school)         # NIS (class didn't change)

# как поменять для всех - поменять через класс

Student.school = "RFMSH"

print(s1.school)              # KTL (it has it's own instance school)
print(s2.school)              # RFMSH