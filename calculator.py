def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("=== Command-Line Calculator ===")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)")
    print("Type 'q' at any time to quit.\n")

    while True:
        choice = input("Choose operation (+, -, *, /) or 'q' to quit: ").strip()

        if choice.lower() == 'q':
            print("Goodbye!")
            break

        if choice not in ('+', '-', '*', '/'):
            print(f"'{choice}' is not a valid operation. Please try again.\n")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)

            print(f"Result: {num1} {choice} {num2} = {result:.4f}\n")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


if __name__ == "__main__":
    main()