# Hardcoded stock prices
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300,
    "AMZN": 120
}

portfolio = {}      # To store user entries: {stock: quantity}
total_investment = 0

print(" Stock Portfolio Tracker")
print("Available stocks:", ", ".join(prices.keys()))
print("Type 'done' to finish input.\n")

# Step 1: User Input Loop
while True:
    stock = input("Enter stock symbol (AAPL/TSLA/GOOG/MSFT/AMZN): ").upper()

    if stock == "DONE":
        break

    if stock not in prices:
        print(" Stock not found in price list. Try again.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print(" Please enter a valid number.\n")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print("Added!\n")

# Step 2: Calculate Total Investment
print("\n------ Portfolio Summary ------")
for stock, qty in portfolio.items():
    value = qty * prices[stock]
    total_investment += value
    print(f"{stock}: {qty} shares x ${prices[stock]} = ${value}")

print("----------------------------------")
print(f"Total Investment = ${total_investment}")
print("----------------------------------\n")

# Step 3: Optional File Saving
save = input("Do you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    filename = "portfolio.txt"

    with open(filename, "w") as file:
        file.write("------ Portfolio Summary ------\n")
        for stock, qty in portfolio.items():
            value = qty * prices[stock]
            file.write(f"{stock}: {qty} shares × ${prices[stock]} = ${value}\n")
        file.write(f"Total Investment = ${total_investment}\n")

    print(f" Report saved as {filename}")
else:
    print("Report not saved.")