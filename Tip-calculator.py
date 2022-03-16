print("Welcome to the Tip Calculator!\n")
print("Paying tips is very essential so therefore YOU MUST PAY!!!\n")
total_bill = input("What was the total bill? $")

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

new_total = (float(total_bill) * int(tip) / 100) + float(total_bill) 

people = input("How many people to split the bill? ")

each_person = round(new_total / int(people), 2)
each_person = "{:.2f}".format(each_person)

print(f"Each person should pay: ${each_person}")