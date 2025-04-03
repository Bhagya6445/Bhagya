# Calculate average grade
def avg(grades):
    return sum(grades) / len(grades)

# Create dictionary of students
def stu_dict(students):
    return {name: grades for name, grades in students}

# Find top student
def top_stu(students):
    top, high = "", 0
    for name, grades in students.items():
        a = avg(grades)
        if a > high:
            top, high = name, a
    return top, high

# Count passed students
def count_pass(students):
    return sum(1 for grades in students.values() if avg(grades) >= 50)

# Example Data
students = [
    ("Alice", [80, 90, 70]),
    ("Bob", [40, 50, 60]),
    ("Charlie", [30, 20, 40])
]

# Using functions
students_dict = stu_dict(students)
top, high = top_stu(students_dict)
passed = count_pass(students_dict)

# Output
print(f"Top Student: {top}, Highest Avg Grade: {high}")
print(f"Students Passed: {passed}")
