def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x/y

def calculator():
    while True:
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter operation choice (1/2/3/4): ")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1,num2)
        elif choice == "2":
            result = subtract(num1,num2)
        elif choice == "3":
            result = multiply(num1,num2)
        else:
            try:
                result = divide(num1,num2)
            except ValueError as error:
                print(error)
                return

        print("Result:",result)

if __name__ == "__main__":
    calculator()
