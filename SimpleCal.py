import math

def add(x, y):
    """Function to perform addition"""
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y): 
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def exponentiate(x, y):
    return x ** y

def calculator():
    """Function to run the calculator program"""
    print("Welcome to Simple Calculator with Advanced Features!")
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Quit")
        
        choice = input("Enter choice (1/2/3/4/5/6): ")
        
        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", exponentiate(num1, num2))
        elif choice == '6':
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    calculator()
