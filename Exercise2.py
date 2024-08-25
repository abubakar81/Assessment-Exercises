# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Taking Input from user
number = int(input("Enter an integer: "))

# Determining if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Checking prime numbers in the specific range
last_four_digits = 43  # Last four digits of student ID
print(f"Prime numbers between 1 and {last_four_digits}:")
for i in range(1, last_four_digits + 1):
    if is_prime(i):
        print(i, end=" ")
