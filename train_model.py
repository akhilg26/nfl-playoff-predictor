import pandas as pd
from data_collection import *
from feature_engineering import *
from training_data import *
import sklearn
from testing_data import *


# print(training_df.head())
X = training_df.drop(columns=['home_team_won'])
y = training_df['home_team_won']

print(f"All games: {len(training_df)}")
X_train, X_validation, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.2, train_size=0.8, shuffle=True)
X_test = testing_df
scaler = sklearn.preprocessing.StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_validation_scaled = scaler.transform(X_validation)
X_test_scaled = scaler.transform(X_test)
model = sklearn.linear_model.LogisticRegression(max_iter=1000)
print(f"Training games: {len(X_train_scaled)}")
print(f"Validation games: {len(X_validation_scaled)}")
model.fit(X_train_scaled, y_train)
print(f"Training score {model.score(X_train_scaled, y_train)}")
print(f"Validation score: {model.score(X_validation_scaled, y_test)}")
feature_names = X_train.columns
coefficients = model.coef_[0]
print(model.predict_proba(X_test))

for name, coef in zip(feature_names, coefficients):
    print(f"{name}: {coef:.3f}")

