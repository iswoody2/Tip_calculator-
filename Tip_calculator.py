print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10 12 15 "))

people = int(input("How many people to split the bill? "))

percentagetip = tip / 100 + 1.0

result = bill / float(people) * float(percentagetip)

print(f"Each person should pay {round(result, 2)}")

