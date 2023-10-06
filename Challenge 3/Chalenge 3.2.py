class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students():
    student_list = []
    num_students = int(input("Enter the number of students: "))
    
    for i in range(num_students):
        name = input(f"Enter the name of student {i+1}: ")
        roll_number = input(f"Enter the roll number of student {i+1}: ")
        cgpa = float(input(f"Enter the CGPA of student {i+1}: "))
        student = Student(name, roll_number, cgpa)
        student_list.append(student)
    
    # Use the sorted function with a lambda function as the key to sort by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
sorted_students = sort_students()

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
