import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the data
df = pd.read_csv('vehicle_rental_data.csv')

# Prepare features and target
X = df[['year', 'mileage', 'seating_capacity', 'transmission', 'air_conditioning', 
        'fuel_efficiency', 'model_year', 'num_features', 'fuel_type', 'vehicle_type', 'brand_tier']]
y = df['rental_rate']

# Encode categorical variables
X = pd.get_dummies(X, columns=['transmission', 'fuel_type', 'vehicle_type', 'brand_tier'], drop_first=True)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

# Save the model
joblib.dump(model, 'trained_rental_price_model.joblib')

print("Model trained and saved as 'trained_rental_price_model.joblib'")
