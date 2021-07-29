class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def middle_grade(self):
        m = 0
        x = 0
        for i in self.grades.values():
            for n in i:
                x += n
                m += 1
        return x / m

    def __str__(self):
        return f'Имя лектора = {self.name} \nФамилия лектора = {self.surname} \nСредняя оценка за лекции = {round(self.middle_grade(), 2)}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.middle_grade() < other.middle_grade()


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_grade(self):
        m = 0
        x = 0
        for i in self.grades.values():
            for n in i:
                x += n
                m += 1
        return x / m

    def __str__(self):
        res = ', '.join(str(i) for i in self.courses_in_progress)
        return f'Имя студента = {self.name} \nФамилия студента = {self.surname} \nСредняя оценка за домашнее задание = {round(self.middle_grade(), 2)} \nКурсы в процессе изучения: {res} \nЗавершенные курсы:{self.finished_courses}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.middle_grade() < other.middle_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя проверяющего = {self.name} \nФамилия проверяющего = {self.surname}'


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

other_student = Student('Emma', 'Swan', 'your_gender')
other_student.courses_in_progress += ['Python']

some_reviewer = Reviewer('Peter', 'Parker')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 7)

print(f'Оценки студенту выставлены: {some_student.grades}')
print(f'Оценки другому студенту выставлены: {other_student.grades}')
# print(f'Курс проверяющего: {some_reviewer.courses_attached}')

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 9)

other_lecturer = Lecturer('Bobby', 'Marley')
other_lecturer.courses_attached += ['Git']
some_student.rate_hw(other_lecturer, 'Git', 7)
some_student.rate_hw(other_lecturer, 'Git', 9)

print(f'Оценки лектору выставлены: {some_lecturer.grades}')
print(f'Оценки другому лектору выставлены: {other_lecturer.grades}')

print()
print(some_lecturer)
print()
print(other_lecturer)
print()
print(some_reviewer)
print()
print(some_student)
print()
print(other_student)
print()
print(f'Средний балл some студента меньше other студента? {some_student < other_student}')
print(f'Средний балл some лектора меньше other лектора? {some_lecturer < other_lecturer}')
