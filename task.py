# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

print("Each person should pay: " + str(round((bill / people) * (1+tip/100), 2)))

# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip/100*bill + bill
bill_per_person = bill_with_tip/people

print("Each person should pay: $" + str(round(bill_per_person, 2)))
