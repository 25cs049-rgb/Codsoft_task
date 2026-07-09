print("===================================")
print("      SIMPLE CALCULATOR")
print("===================================")

while True:
    print("\nChoose an Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the Calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid Choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "1":
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")

        elif choice == "4":
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")

    except ValueError:
        print("Invalid Input! Please enter numbers only.")