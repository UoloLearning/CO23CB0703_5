def max_of_three(num1, num2, num3):
    """This function returns the maximum of three numbers."""
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Call the max_of_three function with 3 numbers
result = max_of_three(10, 5, 20)

# Print the result
print("Maximum of three numbers:", result)
