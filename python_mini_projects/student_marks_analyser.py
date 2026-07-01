# Student Marks Analyser
# A beginner Python mini-project to analyse student marks.

students = {
    "Aman": [80, 90, 75],
    "Riya": [95, 88, 92],
    "Dev": [60, 70, 65],
    "Neha": [85, 85, 85],
    "Kabir": [50, 60, 55],
    "Isha": [92, 94, 90],
    "Arjun": [45, 55, 50],
    "Meera": [78, 82, 80],
    "Rahul": [30, 40, 35],
    "Sneha": [88, 91, 89],
    "Karan": [65, 68, 70],
    "Pooja": [100, 95, 98],
    "Vikram": [58, 62, 59],
    "Tanya": [72, 75, 70],
    "Yash": [20, 25, 30]
}

below_average = 70
passing_marks = 40

def average_of_students(students):
    """Calculate the average marks of each student."""
    average_marks = {}
    for name, marks in students.items():
        average_marks[name] = round(sum(marks) / len(marks), 2)
    return average_marks

def identify_topper(average_marks):
    """Return the student or students with the highest average marks."""
    highest_average = max(average_marks.values())
    toppers = [name for name, average in average_marks.items() if average == highest_average]
    return toppers

def identify_below_average(average_marks, below_average):
    """Return the student or students with average marks below the set average marks."""
    below_average_students = [name for name, average in average_marks.items() if average < below_average]
    return below_average_students

def identify_failed_students(average_marks, passing_marks):
    """Return students whose average marks are below the passing marks."""
    failed_students = [name for name, average in average_marks.items() if average < passing_marks]
    return failed_students

def generate_report(average_marks, toppers, below_average_students, failed_students):
    """This creates a dictionary of all the important attributes to be included in the final report."""
    report = {
        "average_marks": average_marks,
        "toppers": toppers,
        "below_average": below_average_students,
        "failed_students": failed_students
    }
    return report

def print_report(report):
    """This function displays final report in a more presentable way."""
    print("Student Marks Report")
    print("--------------------")

    print("Average Marks:")
    for name, average in report["average_marks"].items():
        print(name + ": " + str(average))

    print()

    print("Toppers:")
    print(", ".join(report["toppers"]))

    print()

    print("Below Average Students:")
    if report["below_average"]:
        print(", ".join(report["below_average"]))
    else:
        print("None")

    print()

    print("Failed Students:")
    if report["failed_students"]:
        print(", ".join(report["failed_students"]))
    else:
        print("None")

average_marks = average_of_students(students)
toppers = identify_topper(average_marks)
below_average_students = identify_below_average(average_marks, below_average)
failed_students = identify_failed_students(average_marks, passing_marks)
report = generate_report(average_marks, toppers, below_average_students, failed_students)
print_report(report)
