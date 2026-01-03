"""Write a program that:
Takes 5 student names and their marks from the user
Stores them in a dictionary
Prints:
All students and marks
Student with highest marks
Student with lowest marks
Calculates and prints the average marks
Updates marks of a given student (input name)"""


dict = {}
for i in range(5):
    name= input("Enter your name: ")
    marks = int(input("Enter your marks of Science: "))
    dict[name]=marks

print("Students & marks:",dict)

max_value = max(dict.values())
min_value = min(dict.values())
print(max_value)
print(min_value)
# print(dict[max_value])

# Average marks
avg = sum(dict.values()) / len(dict)
print("Average marks:",avg)

# Update marks
name = input("Enter the name to update the marks: ")
new_marks = int(input("Enter marks: "))

if name in dict:
    dict[name]=new_marks
    print("Updated dictionary:", dict)

else:
    print("Student not found")

