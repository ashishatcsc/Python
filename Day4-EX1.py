# Create a program that:
#
# 1. Prompts the user to input a (dollar) amount.
#
# 2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.
#
# 3. Prints out the amount in euros, as shown in the screenshot below.

DollarAmount = float(input("How Many Dollars you have? "))
EuroAmount = DollarAmount*0.95
print("Amount in Euros is:",EuroAmount)