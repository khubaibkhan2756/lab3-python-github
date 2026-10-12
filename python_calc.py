def get_two_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def addition():
    x, y = get_two_numbers()
    result = x + y
    print("The result of addition is:", result)

def subtraction():
    x, y = get_two_numbers()
    result = x - y
    print("The result of subtraction is:", result)

def multiplication():
    x, y = get_two_numbers()
    result = x * y
    print("The result of multiplication is:", result)

def division():
    x, y = get_two_numbers()
    if y == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = x / y
        print("The result of division is:", result)

def percentage():
    x, y = get_two_numbers()
    if y == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = (x / y) * 100
        print("The result of percentage is:", result)

def even_odd():
    while True:
        try:
            x = int(input("Enter a number to check if it's even or odd: "))
            if x % 2 == 0:
                print(x, "is an even number.")
            else:
                print(x,  "is an odd number.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    while True:
        print("\n Welcome to Python Calculator\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Even or Odd")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        if choice == '1':
            addition()
        elif choice == '2':
            subtraction()
        elif choice == '3':
            multiplication()
        elif choice == '4':
            division()
        elif choice == '5':
            percentage()
        elif choice == '6':
            even_odd()
        elif choice == '0':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
main()