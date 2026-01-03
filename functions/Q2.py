"""Write a function student_report() that:
Takes a student name as a positional argument
Accepts any number of marks using *args
Accepts optional details like grade, school using **kwargs
Returns the average marks
Prints all additional details neatly"""


def student_report(name, *marks, **details):
    """Prints student details and returns average marks."""

    print("Name: ",name)

    if marks:
        avg = sum(marks)/len(marks)

    else:
        avg = 0

    for key,value in details.items():
        print(f"{key.capitalize()} :{value}")

    return avg

a = student_report("Amit", 
                   70,76,89 ,
                   grade = "A",
                   college = "BMC")
print("Average marks:", round(a,2))

