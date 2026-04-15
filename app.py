class Student:
    def __init__(self, name, course, student_id):
        self.name = name
        self.course = course
        self.id = student_id

    def info(self):
        return f"Ім'я: {self.name}, Курс: {self.course}"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.id == student.id:
                print(f"Студент ({student.id}) уже навчається в школі.")
                return
        self.students.append(student)

    def remove_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                self.students.remove(s)
                return
        print(f"Студента ({student_id}) не знайдено.")

    def list_students(self):
        for s in self.students:
            print(f"{s.name} - {s.course}")

    def students_by_course(self, course):
        return [s for s in self.students if s.course == course]

    def total_students(self):
        return len(self.students)


s1 = Student("Анна", "Python", 1)
s2 = Student("Олег", "Design", 2)
s3 = Student("Іван", "Python", 3)

school = School("IT School")

print(s1.info())

school.add_student(s1)
school.add_student(s2)
school.add_student(s3)
school.add_student(Student("Марія", "Java", 1))

print("\nСписок студентів:")
school.list_students()

print("\nСтуденти курсу Python:")
for s in school.students_by_course("Python"):
    print(s.info())

print("\nВсього студентів:", school.total_students())

school.remove_student(2)
school.remove_student(999)

print("\nПісля видалення:")
school.list_students()