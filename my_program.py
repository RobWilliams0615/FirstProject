# general Python practice on datay types

student_grades = ['A', 'B', 'C']


print(student_grades)


number_of_slopes = list(range(1, 9, 3))

print(number_of_slopes)

rainfall = [3.4, 10, 'Light', [1, 2, 3]]

print(rainfall)

class_grades = [77.5, 89, 95, 64, 89, 90, 93, 65, 70, 64, 89, 67, 89]

mysum = sum(class_grades)
length = len(class_grades)
mean = mysum / length
print(mean)
winner = max(class_grades)
print(winner)

print(class_grades.count(89))
