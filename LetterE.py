# LetterE.py - This program prints the letter E with 3 asterisks
# across and 5 asterisks down.
# Input:  None.
# Output: Prints the letter E.

num_across = 3  # Number of asterisks to print across.
num_down = 5  # Number of asterisks to print down.

# Write a loop to control the number of rows.
for r in range(num_down):
    for c in range(num_across):
        if (r % 2 == 0):
            print("*", end="")
        elif (c == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
