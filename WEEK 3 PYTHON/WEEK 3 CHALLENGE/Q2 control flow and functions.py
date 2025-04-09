def divisible_by_ten(num):
    # Check if the number is divisible by 10
    if num % 10 == 0:
        return True
    else:
        return False

# Example usage
print(divisible_by_ten(50))  # Output: True (50 is divisible by 10)
print(divisible_by_ten(47))  # Output: False (47 is not divisible by 10)