# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 135
}

total_investment = 0
portfolio = {}

print("Enter your stocks. Type 'done' to finish.\n")

while True:
    stock = input("Stock symbol: ").upper().strip()

    if stock == "":
        print("Invalid input. Type a stock symbol or 'done'.")
        continue

    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue
    
    try:
        qty = int(input("Quantity: ").strip())
    except ValueError:
        print("Invalid quantity. Try again.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + qty
    total_investment += stock_prices[stock] * qty
    
    print(f"Added: {qty} shares of {stock}. Current total: ${total_investment}\n")


print("\n--- Portfolio Summary ---")
for s, q in portfolio.items():
    print(f"{s}: {q} shares @ ${stock_prices[s]}")

print(f"\nTotal Investment Value: ${total_investment}")

