# Course Class
class Course:
    def __init__(self, course_name):
        self.course_name = course_name

    def __str__(self):
        return self.course_name


# Student Class
def show_all_students():
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            print("\n All Enrolled Students:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(" No student data found!")


class Student:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.__password = password  # Private variable (Encapsulation)
        self.courses = []

    # Enroll a course
    def enroll_course(self, course):
        self.courses.append(course)

        # File handling (append mode)
        with open("students.txt", "a", encoding="utf-8") as file:
            file.write(f"Name: {self.name}, Roll: {self.roll}, Course: {course}\n")

    # Getter method for password
    def get_password(self):
        return self.__password


# ------------------ Main Program ------------------

# Create courses
course1 = Course("Python")
course2 = Course("Web Development")

# Create students
student1 = Student("Rahim", 1, "rahim123")
student2 = Student("Karim", 2, "karim456")

# Enroll students
student1.enroll_course(course1)
student1.enroll_course(course2)

student2.enroll_course(course1)

# Show all students from the file
show_all_students()

# Access password using getter
print("\n Rahim Password (using getter):", student1.get_password())
