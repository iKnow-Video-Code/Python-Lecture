# Grade Percentage Program - Program that grades based on the percentage a student has by the end of the year

percentageStudent = int(input("Enter the percentage of the student: "))
if percentageStudent >= 90:
    print("The student has a grade of A")
elif percentageStudent >= 80:
    print("The student has a grade of B")
elif percentageStudent >= 70:
    print("The student has a grade of C")
elif percentageStudent >= 60:
    print("The student has a grade of D")
else:
    print("The student has a grade of F")