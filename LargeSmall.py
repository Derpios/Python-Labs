# LargeSmall.py - This program calculates the largest and smallest of three integer values.

# initialize variables here.
firstNumber = -50
secondNumber = 53
thirdNumber = 78

# Write assignment, if, or if else statements here as appropriate.
if firstNumber >= secondNumber and firstNumber >= thirdNumber:
    largest = firstNumber
elif secondNumber >= firstNumber and secondNumber >= thirdNumber:
    largest = secondNumber
else: 
    largest = thirdNumber

if firstNumber <= secondNumber and firstNumber <= thirdNumber:
        smallest = firstNumber
elif secondNumber <= firstNumber and secondNumber <= thirdNumber:
        smallest = secondNumber
else: 
    smallest = thirdNumber
# Output largest and smallest number.
print("The largest value is", largest)
print("The smallest value is", smallest)
