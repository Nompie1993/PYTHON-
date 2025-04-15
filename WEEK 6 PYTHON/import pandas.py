import pandas as pd

# Create a small dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Salary': [50000, 54000, 58000, 60000, 52000]
}

# Load the dataset into a pandas DataFrame
df = pd.DataFrame(data)

# Display summary statistics
summary_statistics = df.describe()