"""Write a program that:
Takes an integer n
Prints numbers from 1 to n
Prints the sum of all even numbers between 1 and n
Stops the loop if the sum exceeds 50"""


n = int(input("Enter an integer:"))
sum =0
for i in range(1,n+1):
    print(i, end=" ")
    if (i % 2 == 0) :
        sum += i
        if (sum>50):
            break

print("Sum of even numbers is: ",sum)    
       
