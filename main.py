#close - closes a file and saves
#read - Reads the contents of the file. You can assign the result t a variable 
#truncate - Empties the file. 
# seek(0)  moves location of reader to the beginning


from sys import argv
script, filename = argv

print(f"We're going to erase { filename}")
print(f"You don't want that, hit CTRL -C (^C)")
print(f"if you do want that hit RETURN")

input('?')

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file GOODBYE!")
target.truncate

print("now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line2)
target.write("\n")

print("and finally we close it")
target.close