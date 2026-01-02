"""Write a program that:
Takes a string input from the user
Prints:
Length of the string
String in uppercase
String in lowercase
Replaces all spaces with _
Prints whether the string is a palindrome (ignore case)"""

str = input("Enter multi-word string: ")

print("Length of the string is ",len(str))

print("In uppercase: ",str.upper())

print("In lowercase: ",str.lower())

print("Replaced all spaces with _:",str.replace(" ","_"))

if (str == str[::-1]) :
    print("Palindrome: True")

else:
    print("Palindrome: False")

