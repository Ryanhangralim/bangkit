file = open("example_file.txt", "r")
for line in file.readlines():
    print(line, end="")
file.close()

print("\n")

with open("example_file.txt") as file:
    for line in file.readlines():
        print(line, end="")