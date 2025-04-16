

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Task 1: Load and Explore the Dataset
# download iris data and read it into a dataframe
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(url, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Display the first few rows
print("First few rows of the dataset:")

print(df.head())

# Explore the structure of the dataset
print("\nData types and missing values:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# If dropping missing values is preferred:
data = df.dropna()

print("\nDataset after cleaning:")
print(df.info())

# Check for duplicates  
print("\nChecking for duplicates:")
print(df.duplicated().sum())

# Remove duplicates if any  
df.drop_duplicates(inplace=True)


# Task 2: Basic Data Analysis
# Compute basic statistics of numerical columns
print("Basic statistics of numerical columns:")
print(data.describe())

# Group by a categorical column and compute mean of a numerical column
print("\nMean of numerical columns grouped by class:")
sepal_length = df['sepal_length'].mean()
grouped_data = df.groupby('class').mean()

print("\nMean of numerical columns grouped by class:")
print(grouped_data)

# Task 3: Data Visualization
# Visualize the data using different types of plots
# 1. Line Chart
plt.figure(figsize=(10, 6))
plt.plot(data['class'], data['sepal_length'], marker='o', label='Trend')
plt.title("Line Chart: Trends Over Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(data['class'], data['sepal_length'], color='blue')      
plt.title("Bar Chart: Average Value per Category")
plt.xlabel("Category")  
plt.ylabel("Average Value")
plt.xticks(rotation=45)
plt.show()

# 3. histogram
# Histogram: Distribution of a numerical column 
plt.figure(figsize=(10, 6))
plt.hist(data['sepal_length'], bins=20, color='purple', alpha=0.7)
plt.title("Histogram: Distribution of Numerical Column")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 4. scatter plot

plt.figure(figsize=(10, 6))
plt.scatter(data['sepal_length'], data['sepal_width'], color='red') 
plt.title("Scatter Plot: Relationship Between Two Numerical Columns")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()