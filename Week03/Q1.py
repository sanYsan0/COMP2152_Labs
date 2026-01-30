grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()
print(f"Sorted grades: {grades}")
#Sorted grades: [78, 85, 88, 90, 92, 95]
print(f"Highest grades: {grades[-1]}")#last item of the list
print(f"Lowest grades: {grades[0]}")#first item of the list
print(f"Total number of grades: {len(grades)}")