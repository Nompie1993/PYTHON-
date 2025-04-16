import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)  # Now 'df' is defined

plt.plot(df['Name'], df['Age'])  # Ensure 'Name' and 'Age' are columns in your DataFrame
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age vs Name Plot')
plt.show()