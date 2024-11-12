stock_prices = [298,305,144,245,123]

monthly_expenses = [2200, 2350, 2600, 2130,2190]


if __name__ == "__main__":
    print(stock_prices[0])
    print("February spent {} extra money than January".format(monthly_expenses[1]-monthly_expenses[0]))
    print("Total expens in frist quarter is {}".format(monthly_expenses[0]+monthly_expenses[1]+monthly_expenses[2]))
    print("Did I spent Rs. 2350 in any month - {}".format(2350 in monthly_expenses))
    monthly_expenses.append(1980)
    print(monthly_expenses)
    monthly_expenses[3] = monthly_expenses[3] - 200
    print(monthly_expenses)