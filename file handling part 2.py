# Open file in write mode
f = open("data.txt", "w")
f.write("Hello Python\nFile Handling")
f.close()

# Read file
f = open("data.txt", "r")
print(f.read())
f.close()

# Append to file
f = open("data.txt", "a")
f.write("\nAppended line")
f.close()
