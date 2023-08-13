def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def main():
  print("Welcome to the calculator!")

  # this is a loop (endless loop)
  while True:
    operation = input("Select an operation (+, -, *, /): ")

    if operation == "+":
        print(num1, "+", num2, "=", add(num1, num2))
    # else if
    elif operation == "-":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif operation == "*":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif operation == "/":
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid operation!")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    choice = input("Do you want to continue? (y/n): ")
    if choice == "n":
        break

if __name__ == "__main__":
  main()
