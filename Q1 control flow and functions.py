def large_power(base, exponent):
    # Calculate base raised to the power of exponent
    result = base ** exponent
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Example usage
print(large_power(5, 4))  # Output: false (5^4 = 625, which is less than 5000)
print(large_power(10, 6)) # Output: True (10^6 = 1000, which is greater than 5000)
