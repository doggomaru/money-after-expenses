name = input("What is your name? ")
hours_worked_str = input(f"Hello, {name}! I'm here to help you calculate your earnings after monthly expenses! How many hours do you work per week? ")
hourly_pay_str = input("In USD, how much do you earn per hour at work? Please omit the dollar sign, as it is implied. ")
hours_worked = round(float(hours_worked_str),2)
hourly_pay = round(float(hourly_pay_str),2)
monthly_pay = hourly_pay * hours_worked * 4
rent = round(float(input("In USD, how much do you pay in rent or mortgage each month? ")),2)
print(f"This project is currently unfinished. For now, let's lay out the information provided. Your monthly pay is ${monthly_pay} and your rent/mortgage per month is ${rent}.")
