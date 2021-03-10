#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")
bill = input("What was the total bill! ")
bill_as_float = float(bill)
current_bill = (f"Your current bill is {bill_as_float}")
print(current_bill)

tip = input("What percentage tip would you like to leave? 10, 12 or 15? ")
tip_as_int = int(tip)
tip_percent = tip_as_int / 100

how_many_people = int(input("How many people to split the bill?"))

total_tip_amount = bill_as_float * tip_percent
total_bill = total_tip_amount + bill_as_float
total_bill_as_rounded = round(total_bill, 2)
each_person = bill_as_float / how_many_people * (1 + tip_percent)
print(tip_percent)
each_person_as_rounded = "{:.2f}".format(each_person)
message = f" Total bill is {total_bill_as_rounded}, you are giving {tip_as_int} percent tips, between {how_many_people} people each person will pay {each_person_as_rounded}"
print(message)

