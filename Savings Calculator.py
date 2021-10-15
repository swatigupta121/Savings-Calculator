print("Your Saving Calculator")

hr=input("How much do you earn per hour? ")

hr_per_day=8
daily_savings = int(hr)*hr_per_day
print("This is your daily savings: ",daily_savings)

days_per_week=5
weekly_savings = daily_savings*days_per_week
print("This is your weekly savings: ",weekly_savings)

weeks_per_month=4
monthly_savings = weekly_savings*weeks_per_month 
print("This is your monthly savings: ",monthly_savings)
