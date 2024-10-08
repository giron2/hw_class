class Student:
    def __init__(self, name, surname,):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}
        self.grad = []

    def teacher_rate(self, lecturer, course, grade: int):
        self.lecturer = lecturer
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.course and grade > 0 and grade <= 10:
            lecturer.grad.append(grade)
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]

            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {sum(self.grad) / len(self.grad)} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        a = sum(self.grad) / len(self.grad)
        b = sum(other.grad) / len(other.grad)
        return a < b

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course = []
        self.grades = {}
        self.grad = []
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum(self.grad) / len(self.grad)}"
    def __lt__(self, other):
        a = sum(self.grad) / len(self.grad)
        b = sum(other.grad) / len(other.grad)
        return a < b
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade:int):
        self.student = student
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            student.grad.append(grade)
            if course in student.grades:
                student.grades[course] += [grade]

            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"





stud1 = Student("Ruoy", "Eman")
stud2 = Student("Joseph", "Biden")

stud1.courses_in_progress = ("Python" , "C++" , "Java")
stud2.courses_in_progress = ("Python" , "JavaScript" , "Html")

stud1.finished_courses = ("JavaScript" , "Html")
stud2.finished_courses = ("C++" , "Java")

lec1 = Lecturer("Eva", "Scott")
lec2 = Lecturer("Olga", "Evans")

rew1 = Reviewer("jh", "Foster")

rew2 = Reviewer("joh", "Coleman")

rew1.courses_attached = ("Python" , "JavaScript", "Java" , "Html")
rew2.courses_attached = ("Python" , "C++" , "Html")

lec1.course = ("Python" , "JavaScript" , "Html" , "C++")
lec2.course = ("Python" , "JavaScript" , "Html" , "Java")


rew1.rate_hw(stud1, "JavaScript", 4)
rew1.rate_hw(stud1, "JavaScript", 9)
rew2.rate_hw(stud1, "Html" , 8)
rew2.rate_hw(stud2, "C++" , 8)


stud1.teacher_rate(lec1, "Python", 8)
stud2.teacher_rate(lec1, "Python", 7)

stud1.teacher_rate(lec2, "Python", 8)
stud2.teacher_rate(lec2, "Python", 7)

def avg_stud(stud:list, cour):
    stud_lst = list(stud)
    cours = cour
    rat = []
    rats = []

    for st in stud_lst:
        rat.append(st.grades[cours])

    for r in rat:
        for x in r:
            rats.append(x)

    return f"Курс: {cours} Ср. оценка студентам: {sum(rats)/len(rats)}"


def avg_lect(lec:list, cour):
    lec_lst = list(lec)
    cours = cour
    rat = []
    rats = []

    for st in lec_lst:
        rat.append(st.grades[cours])

    for r in rat:
        for x in r:
            rats.append(x)

    return f"Курс: {cours} Ср. оценка лекторам: {sum(rats)/len(rats)}"

test_1 = avg_stud([stud2], "C++")
test_2 = avg_stud([stud1], "JavaScript")
test_3 = avg_lect([lec1], "Python")
test_4 = avg_lect([lec2], "Python")
print(test_3)
print(test_2)
print(test_1)
print(test_4)

print(stud1)
print(stud2)

print(lec1)
print(lec2)

print(rew1)
print(rew2)


print(stud2 < stud1)
print(stud1 < stud2)

print(lec2 < lec1)
print(lec1 < lec2)