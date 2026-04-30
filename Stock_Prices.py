import pandas as pd
import matplotlib.pyplot as plt

#===============================================
# DATA CLEANING AND PREPROCESSING
#===============================================
df = pd.read_csv("Stock_Prices.csv")

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Check missing values
print(df.isnull().sum())

df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Check data types
print(df.dtypes)

#===============================================
# EXPLORATORY DATA ANALYSIS
#===============================================

print(df.describe())

# Example: Opening price distribution
df['open'].hist()
plt.title("Distribution of Opening Prices")
plt.show()


