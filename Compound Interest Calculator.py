# This program will request how much money will be in your savings account and then calculate
# based on the interest rate how many years it will take to pay off your given debt from interest
# alone. The program prints out how much money you will have after each year.

account = float(input("Insert amount of money you have deposited: "))
interest_rate = float(input("Insert the interest rate of your savings account: "))
years = float(input("Insert the amount of years you plan on holding your savings: "))
debt_total = float(input("Insert your current amount of debt: "))


print(f"initial_amount: {account}")

year_counter = 1
while year_counter <= years:
    accrued_interest = account * interest_rate
    account += accrued_interest
    print(f"year {round(year_counter, 2)}: {round(account, 2)}")
    year_counter += 1

if account < debt_total:
    print("\nSorry, but you're still in debt")
else:
    print("\nCongrats! You are debt-free!")

years_to_freedom = 1
while account < debt_total:
    accrued_interest = account * interest_rate
    account += accrued_interest
    years_to_freedom += 1
if account > debt_total:
    print(f"\nIt will take {years_to_freedom} years to overcome your debt on interest alone. \
        \n...Let's hope the world still exists by then.")
