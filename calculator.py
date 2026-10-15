def calculator():

    print("==========================")
    print("      CALCULATOR")
    print("==========================")

    while True:

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "5":
            print("Thank you for using Calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice!")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                print("Result =", result)

            elif choice == "2":
                result = num1 - num2
                print("Result =", result)

            elif choice == "3":
                result = num1 * num2
                print("Result =", result)

            elif choice == "4":

                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print("Result =", result)

        except ValueError:
            print("Please enter valid numbers.")


calculator()
