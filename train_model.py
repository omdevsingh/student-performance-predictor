
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import pickle

# Example training dataset
data = {
    "study_hours": [
        1, 2, 3, 4, 5, 6, 7, 8,
        1, 3, 5, 7, 2, 4, 6, 8,
        2, 4, 6, 8
    ],
    "attendance": [
        50, 55, 60, 65, 70, 75, 80, 85,
        60, 70, 80, 90, 65, 75, 85, 95,
        55, 65, 75, 90
    ],
    "previous_marks": [
        40, 45, 50, 55, 60, 65, 70, 80,
        45, 55, 65, 75, 50, 60, 70, 85,
        48, 58, 68, 82
    ],
    "final_marks": [
        42, 46, 52, 58, 63, 68, 74, 85,
        47, 57, 67, 78, 52, 62, 73, 88,
        50, 60, 71, 86
    ]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance", "previous_marks"]]
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Model training completed!")
print("Mean Absolute Error:", round(mean_absolute_error(y_test, predictions), 2))
print("R2 Score:", round(r2_score(y_test, predictions), 2))

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as model.pkl")
