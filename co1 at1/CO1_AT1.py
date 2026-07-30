#co1_at1_1

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("house_price.csv")
print(data.head())

X = data.drop("Price", axis=1)
y = data["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Predicted House Prices:")
print(y_pred)

score = r2_score(y_test, y_pred)
print("\nR² Score (Accuracy):", score)

#co1_at1_2

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("student_performance.csv")
print(data.head())

X = data[["Study_Hours", "Attendance", "Internal_Marks", "Assignment_Score"]]
y = data["Final_Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Predicted Final Marks:")
print(y_pred)

score = r2_score(y_test, y_pred)
print("\nR² Score (Accuracy):", score)