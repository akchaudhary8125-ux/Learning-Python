"""Write a program to:
Copy contents of source.txt to backup.txt
Use with statement
"""

with open("source.txt", "r") as src, open("backup.txt", "w") as backup:
    backup.write(src.read())
