# Function to calculate birth year
def calculate_birth_year(age, last_four_digits):
    current_year = 2024  # Current year is 2024
    birth_year = current_year - age
    # Birth year based on the last four digits of the student ID
    if last_four_digits % 2 == 0:
        birth_year -= last_four_digits
    else:
        birth_year += last_four_digits
    return birth_year

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
student_id = input("Enter your student ID: ")

# Extracting the last four digits of the student ID
last_four_digits = int(student_id[-4:])

# Calculating birth year
birth_year = calculate_birth_year(age, last_four_digits)

# Displaying the result
print(f"Hello, {name}! Based on your age, you were born in {birth_year}.")
