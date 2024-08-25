# Function to count even and odd numbers in a list
def count_even_odd(numbers):
    count = {"even": 0, "odd": 0}
    for num in numbers:
        if num % 2 == 0:
            count["even"] += 1
        else:
            count["odd"] += 1
    return count

# List of integers
numbers = []

# Taking input from the user
numbers = input("Enter numbers separated by spaces: ")

# Converting the input string to a list of integers
numbers = list(map(int, numbers.split()))

# Modifying the list by adding the last four digits of the student ID
last_four_digits = 43  # Last four digits of student ID
modified_numbers = [num + last_four_digits for num in numbers]

# For counting even and odd numbers
result = count_even_odd(modified_numbers)

# Displaying the result
print("Modified list:", modified_numbers)
print("Even and Odd count:", result)
