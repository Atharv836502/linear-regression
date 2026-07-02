import joblib

model = joblib.load("linear_regression_model.pkl")

price = model.predict([[3300]])
print(price)