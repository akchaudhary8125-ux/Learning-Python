"""Write a program that:
Takes an integer input
Prints:
"Positive" if number > 0
"Negative" if number < 0
"Zero" if number == 0
If the number is positive, also print:
"Even" or "Odd" """

num = int(input("Enter a number: "))

# checks positive, neagtive or zero
if (num>0):
    print("Positive")
    
    # checks even or odd if positive
    if (num%2 == 0):
        print("Even")
    else:
        print("Odd")

elif(num<0):
    print("Negative")
else:
    print("Zero")
