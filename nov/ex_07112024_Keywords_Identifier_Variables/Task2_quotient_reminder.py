# Task 2
# Take a 2 input from the user Print the Quotient and Remainder

# taking 2 input
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

# convert the input str to int
num1 = int(num1)
num2 = int(num2)

Quotient = num1 // num2
Remainder = num1 % num2

# printing output
print("The Quotient of number is", Quotient)
print("The Remainder of number is", Remainder)

