# Stock Portfolio Tracker
# Developer: Hema
# Task 2 - CodeAlpha Internship Project

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}

print("💼 Welcome to the Stock Portfolio Tracker!")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Taking user input
while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("⚠️ Stock not found. Please enter a valid symbol from the list.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("⚠️ Please enter a valid number for quantity.")

# Calculate total investment
total_investment = 0
print("\n📊 Your Portfolio Summary:")
print("-" * 40)
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_investment += value
    print(f"{stock} - {qty} shares × ${stock_prices[stock]} = ${value}")

print("-" * 40)
print(f"💰 Total Investment Value: ${total_investment}")

# Save results to file
save = input("\nWould you like to save the results to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-" * 30 + "\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total Investment: ${total_investment}\n")
    print("✅ Results saved to 'portfolio_summary.txt' successfully!")

print("\n🎯 Thank you for using the Stock Portfolio Tracker!")
