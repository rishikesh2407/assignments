def addNumber(a, b):
    sum = a + b
    return sum
# Taking input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Calling out user-defined function 
sum = addNumber(num1, num2)
# Display result
print("Sum of two numbers is: ", sum)