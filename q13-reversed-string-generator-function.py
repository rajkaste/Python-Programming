# generator function
def reverse_string(my_str):
    length = len(my_str)
    # print(length)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# print(reverse_string("C4E Python Lab!"))

# for loop to print the whole reversed string
for char in reverse_string("C4E Python Lab!"):
    print(char, end="")
