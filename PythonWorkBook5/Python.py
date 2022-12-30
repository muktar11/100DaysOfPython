student_heights = input("INPUT  A LIST OF STUDENT HEIGHTS.").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

#write your code below this row 
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
number_of_students = len(student_heights)
average_height = total_height / number_of_students
print(average_height)