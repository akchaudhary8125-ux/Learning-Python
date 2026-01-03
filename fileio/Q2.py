"""Write a program that:
Writes "File I/O started" to log.txt
Appends "Learning Python" on the next line"""


with open("log.txt", "w") as f:
    f.write("File I/O started")
    
    
with open("log.txt", "a") as f:
    f.write("\nLearning Python")