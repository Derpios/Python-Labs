# HouseSign.py - This program calculates prices for custom house signs.

# Initialize variables here.
charge = 0.00
num_chars = 8
color = "gold"
wood_type = "oak"
# Charge for this sign.
charge = charge + 35.00
# Number of characters.
if num_chars > 5:
    charge = charge + (num_chars - 5) * 4
# Color of characters.
if color == "gold":
    charge = charge + 15.00
# Type of wood.
if wood_type == "oak":
    charge = charge + 20.00
# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print(f"The charge for this sign is ${charge:.2f}")
