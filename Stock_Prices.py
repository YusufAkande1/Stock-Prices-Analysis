import pandas as pd
import matplotlib.pyplot as plt

#===============================================
# DATA CLEANING AND PREPROCESSING
#===============================================
df = pd.read_csv("Stock_Prices.csv")

# Check missing values
print(df.isnull().sum())

df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Check data types
print(df.dtypes)

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Check columns
print(df.columns)

df.to_csv("Stock_Price_Clean.csv")

print("Data Cleaning Completed")

#===============================================
# EXPLORATORY DATA ANALYSIS
#===============================================

print(df.describe())

# Example: Opening price distribution
df['open'].hist()
plt.title("Distribution of Opening Prices")
plt.show()