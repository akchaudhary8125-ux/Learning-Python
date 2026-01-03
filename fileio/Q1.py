"""Write code to:
Open a file notes.txt
Read all lines
Print only lines containing the word "Python" """

# with open("note.txt", "w") as f:
#     f.write("hello")


with open("notes.txt", "r") as f:
    content = f.readlines()

    for line in content:
        if "Python" in line:
            print(line.strip())
