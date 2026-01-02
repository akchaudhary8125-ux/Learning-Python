import random

"""
1 for snake
-1 for water
0 for gun

"""
# compter's choice
computer = random.choice([0,1,-1])

# Taking user's choice and converting it into 0,1,-1
user_str = input("""Enter 
s for snake 
w for water 
g for gun
Your choice: """)

user_dict = {"s" : 1 , "w" : -1, "g": 0}
clean_user = user_str.strip().lower()
if (clean_user=="s" or clean_user=="w" or clean_user=="g"):
    user = user_dict[clean_user]

else:
    print("Choose a valid option!!!")
    


# Showing user's and computer's choice
reverse_dict = {1: "Snake", -1:"Water", 0:"Gun"}
print(f"Your Choice: {reverse_dict[user]} \nComputer's Choice: {reverse_dict[computer]}\n")

# Result
if (computer == user):
    print("Its a Draw!!!\n")

else:
    if (computer==-1 and user==1):
        print("You Win!!!\n")

    elif(computer==-1 and you==0):
        print("Computer Wins!!!\n")

    elif(computer==1 and user==-1):
        print("Computer Wins!!!\n")

    elif(computer==1 and user==0):
        print("You Win!!!\n")
    
    elif(computer==0 and user==-1):
        print("You Win!!!\n")
        
    elif(computer==0 and user==1):
        print("Computer Wins!!!\n")

    else: 
        print("Something went wrong!\n")
        