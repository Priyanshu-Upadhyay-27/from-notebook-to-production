import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Fake training data
# Features: [area, bedrooms]
X = np.array([
    [600,  1],
    [800,  2],
    [1000, 2],
    [1200, 3],
    [1500, 3],
    [1800, 4],
    [2000, 4],
    [2500, 5],
])

# Target: price in lakhs
y = np.array([25, 35, 45, 55, 70, 85, 95, 120])

# Train model
model = LinearRegression()
model.fit(X, y)

