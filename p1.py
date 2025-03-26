def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Input a number
num = int(input("Enter a number: "))

# Calculate and display the factorial
print(f"The factorial of {num} is {factorial(num)}")
