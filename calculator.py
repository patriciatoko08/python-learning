try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product: {a * b}")
except ValueError:
    print("Please enter numbers only.")