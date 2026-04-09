import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Stock_Prices.csv")

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Check data types
print(df.dtypes)

# Exploratory Data Analysis (EDA)

print(df.describe())

# Example: Opening price distribution
df['open'].hist()
plt.title("Distribution of Opening Prices")
plt.show()

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Check columns
print(df.columns)

# Filter data
apple = df[df['symbol'] == 'AAPL']
apple = apple.sort_values('date')

print(apple)

plt.plot(apple['date'], apple['close'])
plt.title("AAPL Stock Price Over Time")
plt.show()

apple['MA_30'] = apple['close'].rolling(window=30).mean()

plt.plot(apple['date'], apple['close'], label='Close')
plt.plot(apple['date'], apple['MA_30'], label='30-day MA')
plt.title('Stock Price vs 30-Day Moving Average')
plt.legend()
plt.show()