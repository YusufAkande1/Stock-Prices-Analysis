import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ===============================================
# CLASSIFICATION
# ===============================================

# Load cleaned dataset
df = pd.read_csv("Stock_Price_Clean.csv")

df['movement'] = (df['close'] > df['open']).astype(int)

# Select Features
X = df[['open', 'high', 'low', 'volume']]
y = df['movement']

#Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make Prediction
y_pred = model.predict(X_test)

# Evaluate Model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))