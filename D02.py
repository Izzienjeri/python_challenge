num1 = float(input("Enter the first number: "))  
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter your choice (1/2/3/4): ")

if operation == '1':  
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '2':  
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '3': 
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == '4':  # Division
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid input! Please select a valid operation.")












# # Perform the chosen operation
# if operation == '1':  # Addition
#     result = num1 + num2
#     print(f"{num1} + {num2} = {result}")

# elif operation == '2':  # Subtraction
#     result = num1 - num2
#     print(f"{num1} - {num2} = {result}")

# elif operation == '3':  # Multiplication
#     result = num1 * num2
#     print(f"{num1} * {num2} = {result}")

# elif operation == '4':  # Division
#     if num2 != 0:
#         result = num1 / num2
#         print(f"{num1} / {num2} = {result}")
#     else:
#         print("Error! Division by zero is not allowed.")

# else:
#     print("Invalid input! Please select a valid operation.")


