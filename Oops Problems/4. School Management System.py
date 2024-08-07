# school_management.py

class Person:
    """
    Base class to represent a person.
    """

    def __init__(self, name, age):
        """
        Initialize the person with name and age.
        
        :param name: The name of the person.
        :param age: The age of the person.
        """
        self.__name = name # private attribute
        self.__age = age # private attribute

    def get_name(self):
        """
        Get the name of the person.
        
        :return: The name of the person.
        """
        return self.__name

    def get_age(self):
        """
        Get the age of the person.
        
        :return: The age of the person.
        """
        return self.__age

class Student(Person):
    """
    Class to represent a student, inheriting from Person.
    """

    def __init__(self, name, age, student_id):
        """
        Initialize the student with name, age, and student ID.
        
        :param name: The name of the student.
        :param age: The age of the student.
        :param student_id: The student ID.
        """
        super().__init__(name, age)
        self.__student_id = student_id # private attribute

    def get_student_id(self):
        """
        Get the student ID.
        
        :return: The student ID.
        """
        return self.__student_id

class Teacher(Person):
    """
    Class to represent a teacher, inheriting from Person.
    """

    def __init__(self, name, age, employee_id):
        """
        Initialize the teacher with name, age, and employee ID.
        
        :param name: The name of the teacher.
        :param age: The age of the teacher.
        :param employee_id: The employee ID.
        """
        super().__init__(name, age)
        self.__employee_id = employee_id # private attribute

    def get_employee_id(self):
        """
        Get the employee ID.
        
        :return: The employee ID.
        """
        return self.__employee_id

class Course:
    """
    Class to represent a course.
    """

    def __init__(self, course_name, course_code):
        """
        Initialize the course with course name and course code.
        
        :param course_name: The name of the course.
        :param course_code: The course code.
        """
        self.__course_name = course_name # private attribute
        self.__course_code = course_code # private attribute
        self.__students = [] # private attribute

    def add_student(self, student):
        """
        Add a student to the course.
        
        :param student: The student to add.
        """
        self.__students.append(student)

    def remove_student(self, student_id):
        """
        Remove a student from the course by student ID.
        
        :param student_id: The ID of the student to remove.
        """
        self.__students = [student for student in self.__students if student.get_student_id() != student_id]

    def list_students(self):
        """
        List all students in the course.
        
        :return: A list of student names.
        """
        return [student.get_name() for student in self.__students]

# Example usage
if __name__ == "__main__":
    # Create students
    student1 = Student("Alice", 20, "S1001")
    student2 = Student("Bob", 21, "S1002")

    # Create a teacher
    teacher = Teacher("Mr. Smith", 45, "T2001")

    # Create a course
    course = Course("Mathematics", "MATH101")

    # Add students to the course
    course.add_student(student1)
    course.add_student(student2)

    # List students in the course
    print("Students in the course:")
    print(course.list_students())

    # Remove a student from the course
    course.remove_student("S1001")

    # List students in the course after removal
    print("Students in the course after removal:")
    print(course.list_students())
