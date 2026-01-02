"""Write a Python program that:
Takes two inputs from the user
Stores one as int and the other as float
Prints:
Their sum
Their type using type()
Converts both to string and concatenates them
Prints the final result"""

a = int(input("Enter a valid integer: "))
b = float(input("Enter a valid float: "))

sum = a + b
print("Sum is:",sum)

print("Types:",type(a), type(b))

concat = str(a) + str(b)
print(concat)
