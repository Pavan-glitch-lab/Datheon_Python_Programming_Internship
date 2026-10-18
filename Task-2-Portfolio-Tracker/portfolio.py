import csv

portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    ticker = input("\nEnter stock ticker (or 'done' to finish): ").upper()

    if ticker == "DONE":
        break

    try:
        buy_price = float(input("Enter buying price: "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            continue

        portfolio[ticker] = {
            "buy_price": buy_price,
            "quantity": quantity
        }

    except ValueError:
        print("Please enter valid numbers.")
        continue

if not portfolio:
    print("No stocks entered.")
    raise SystemExit

prices = {}

with open("sample_prices.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        prices[row["Ticker"].upper()] = float(row["Price"])

total_invested = 0
total_value = 0

print("\n========== PORTFOLIO SUMMARY ==========")
print(f"{'Ticker':<10}{'Quantity':<12}{'Invested':<15}{'Market Value':<15}{'Gain/Loss %'}")

summary = []

for ticker, details in portfolio.items():
    buy_price = details["buy_price"]
    quantity = details["quantity"]

    if ticker not in prices:
        print(f"{ticker}: Price not found in sample_prices.csv")
        continue

    current_price = prices[ticker]
    invested = buy_price * quantity
    market_value = current_price * quantity
    gain_loss = ((current_price - buy_price) / buy_price) * 100

    total_invested += invested
    total_value += market_value

    print(
        f"{ticker:<10}{quantity:<12}"
        f"{invested:<15.2f}{market_value:<15.2f}"
        f"{gain_loss:.2f}%"
    )

    summary.append({
        "Ticker": ticker,
        "Buy Price": buy_price,
        "Current Price": current_price,
        "Quantity": quantity,
        "Invested": invested,
        "Market Value": market_value,
        "Gain/Loss %": round(gain_loss, 2)
    })

profit_loss = total_value - total_invested

print("\nTotal Invested: ₹", round(total_invested, 2))
print("Current Portfolio Value: ₹", round(total_value, 2))
print("Total Profit/Loss: ₹", round(profit_loss, 2))

if total_invested > 0:
    print("Overall Return: ", round((profit_loss / total_invested) * 100, 2), "%")

with open("portfolio_summary.csv", "w", newline="") as file:
    fields = [
        "Ticker", "Buy Price", "Current Price", "Quantity",
        "Invested", "Market Value", "Gain/Loss %"
    ]

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(summary)

print("\nSummary saved to portfolio_summary.csv")