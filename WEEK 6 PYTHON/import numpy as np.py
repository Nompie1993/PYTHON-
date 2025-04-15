import numpy as np

# Create a NumPy array of numbers from 1 to 10
arr = np.arange(1, 11)

# Calculate the mean of the array
mean = np.mean(arr)

print(f"The mean of the array {arr} is {mean}.")











import matplotlib.pyplot as plt

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Plotting the line graph
plt.plot(numbers)

# Adding title and labels
plt.title('Simple Line Graph')
plt.xlabel('Index')
plt.ylabel('Value')

# Display the plot
plt.show()