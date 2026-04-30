import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ===============================================
# TIME SERIES ANALYSIS
# ===============================================

df = pd.read_csv("Stock_Prices.csv")

# Check missing values
print(df.isnull().sum())

# Drop Missing Values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Check columns
print(df.columns)

# Filter One Column
apple = df[df['symbol'] == 'AAPL']
apple = apple.sort_values('date')

print(apple)

# Plot trend
plt.plot(apple['date'], apple['close'])
plt.title("AAPL Stock Price Over Time")
plt.show()

# Moving average
apple['MA_30'] = apple['close'].rolling(window=30).mean()

plt.plot(apple['date'], apple['close'], label='Close')
plt.plot(apple['date'], apple['MA_30'], label='30-day MA')
plt.title('Stock Price vs 30-Day Moving Average')
plt.legend()
plt.show()

# ===============================================
# REGRESSION ANALYSIS
# ===============================================

# Select Features
X = df[['open']]
y = df['close']

# Split data into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make Prediction
y_pred = model.predict(X_test)

# Evaluate Model

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)