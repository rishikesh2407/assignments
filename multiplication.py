# Python program to multiply two number using function

def product_num(num1, num2):  #user-defind function
    num = (num1 * num2)   #calculate product
    return num   #return value

# take inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# function call
product = product_num(num1, num2)

# print multiplication value
print("The Product is: ", product)