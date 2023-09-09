# LifeSpan Time Remaining
# Inspired from Wait but Why - Tim Urban
import math

while True:
    programname = "Life Clock"
    print (f"\nWelcome to {programname}!\nLets calculate the time you have remaining in your career and your lifetime.\n")
    print (f"Disclaimer: These numbers are estimates based on a 365 day year and general statistics in Western Countries, 2023.\n")
    age = input("Enter your current age:\n")
    currentage = float(age)
    estimatedlifespan = input("How long do you think you'll live for?\nLife expectancy in Western Countries is approximately 80 for Men and 84 for Women.\n")
    lifespan = float(estimatedlifespan)
    # Retirement Age 
    retirement = input("When would you like to retire?\nAverage retirement age is approximately 66.\nYou may also use this section to calculate time remaining for a different goal.\n")
    estimatedretire = float(retirement)

    # Time in a Year
    days = 365.0
    weeks = 52.0
    months = 12.0

    # Life Time Remaining
    yearsleft = round(lifespan-currentage,1)
    monthsleft = round(yearsleft*12,1)
    weeksleft = round(yearsleft*52,1)
    daysleft = round(yearsleft*365,1)
    # Career Time Remaining
    cyearsleft = round(estimatedretire-currentage,1)
    cmonthsleft = round(cyearsleft*12,1)
    cweeksleft = round(cyearsleft*52,1)
    cdaysleft = round(cyearsleft*365,1)

    print(f"\n      LIFE CLOCK RESULTS GENERATED        \n")
    print(f"CAREER CLOCK\n There are:\n    Days: {cdaysleft}\n    Weeks: {cweeksleft}\n    Months: {cmonthsleft}\n    Years: {cyearsleft}\n remaining until you reach the age of {estimatedretire}.")
    print(f"\nYOUR LIFE CLOCK\n You have:\n    {daysleft} days, {weeksleft} weeks, {monthsleft} months and {yearsleft} left in total,\n assuming you live until {estimatedlifespan} (sorry I'm grim lol).\n")
    print(f"\n How would you like to use your time?...")
    
    restart = input(f"\n       Run {programname} again: (Yes/No)\n").lower()
    if restart != "yes":
        print(f"\n      Exited {programname}")
        break
    print (f"\n      Restarting {programname}...")