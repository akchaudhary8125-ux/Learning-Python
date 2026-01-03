"""Write a program that:
Takes 5 integers from the user
Stores them in a tuple
Prints:
The tuple
Sum, maximum, and minimum values
Converts the tuple into a list
Removes all duplicate elements
Converts it back to a tuple and prints it"""

# empty tuple
nums = ()

# Taking input from user
for i in range(5):
    num = int(input("Enter integer: "))
    nums = nums + (num,)

# prints the tuple
print("Tuples:", nums)

print("Sum is:", sum(nums))
print("Max number is:", max(nums))
print("Min number is:", min(nums))

# converts the tuple into list and removes the duplicate items
lst = list(set(nums))
print(lst)

# Again converts into tuple from list
num_tup = tuple(lst)
print("New tuple is:", num_tup)