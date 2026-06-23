# Pandas Data Analysis Project
# California Housing Dataset
# 

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing


# Load Dataset
california_dataset = fetch_california_housing()

print(type(california_dataset))
print(california_dataset)

# Create DataFrame
california_df = pd.DataFrame(
    california_dataset.data,
    columns=california_dataset.feature_names
)

print(california_df.head())
print(california_df.tail())
print(california_df.shape)
california_df.info()

# Add Target Column
california_df["Target"] = california_dataset.target

# Missing Values
print(california_df.isnull().sum())

# Statistics
print(california_df.describe())

# Additional Column
california_df["Price"] = california_dataset.target

# Drop Column (temporary example)

california_df.drop(columns="Price")

# Data Selection
print(california_df.iloc[:, 0])
print(california_df.iloc[:, -1])

# Correlation
print(california_df.corr())

# Save Data
california_df.to_csv("california.csv", index=False)
california_df.to_excel("california.xlsx", index=False)