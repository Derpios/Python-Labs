# This program calculates an employee's take home pay.
salary = 1250.00
numDependents = 2

# Calculate state tax here.
stateTax = (0.065 * salary)
print(f"State Tax: ${stateTax:.2f}")

# Calculate federal tax here.
federalTax = (0.28 * salary)
print(f"Federal Tax: ${federalTax:.2f}")

# Calculate dependant deduction here.
dependentDeduction = (0.025 * salary) * numDependents
print(f"Dependents: ${dependentDeduction:.2f}")

# Calculate total withholding here.
totalWithholding = (stateTax + federalTax)
print(f"Total withholding ${totalWithholding:.2f}")

# Calculate take home pay here.
takeHomePay = (salary - totalWithholding + dependentDeduction)
print(f"Salary: ${salary:.2f}")
print(f"Take-Home Pay: ${takeHomePay:.2f}")
