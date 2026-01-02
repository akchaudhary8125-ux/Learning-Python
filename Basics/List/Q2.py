"""Write a program that:
Takes 5 integers from the user and stores them in a list
Prints:
The original list
Sum of all elements
Maximum and minimum element
Sorts the list in descending order
Removes all even numbers from the list
Prints the final list"""

# lst = []

# a,b,c,d,e = int(input("Enter 5 integers: "))
# print(a,b,c,d,e)

lst = []

# Taking 5 integers
for i in range(5):
    num = int(input("Enter integer: "))
    lst.append(num)

print("Original list:", lst)
print("Sum:", sum(lst))
print("Max:", max(lst))
print("Min:", min(lst))

# Sorting in descending order
lst.sort(reverse=True)
print("Sorted (desc):", lst)

# Removing even numbers
lst = [x for x in lst if x % 2 != 0]
print("Final list:", lst)
