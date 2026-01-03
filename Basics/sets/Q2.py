"""Write a program that:
Takes two sets of integers from the user
Prints:
Union
Intersection
Difference (set1 - set2)
Removes all duplicate elements from a list using a set
Prints the final unique list"""


set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

lst = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(lst))

print("Unique list:", unique_list)