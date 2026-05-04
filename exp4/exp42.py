# Store student marks and calculate average and topper.
"""
Created on Fri Apr 02 15:10:00 2026

@author: prajwal gogawale35

"""

# Take number of students
n = int(input("Enter number of students: "))
marks = []

# Input marks
for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

# Calculate average and topper
average = sum(marks) / n if n > 0 else 0
topper = max(marks) if n > 0 else 0

# Output
print("Marks:", marks)
print("Average marks:", average)
print("Topper marks:", topper)
