sh: 1: :wq: not found
for char in range(26):
    if char != 4 and char != 16:
        print("{:s}".format(chr(char + ord("a"))), end="")
