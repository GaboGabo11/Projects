print("Welcome User to calculator!")
math = input('What operator do you want to calculate?(+, -, /, //, *, **):  ')
if math == "+":
    num1 = int(input("enter first number:  "))
    num2 = int(input("enter second number:  "))
    print("Answer is" + " " + str(num1 + num2))

if math == "-":
    num1 = int(input("enter first number:  "))
    num2 = int(input("enter second number:  "))
    print("Answer is" + " " + str(num1 - num2))

if math == "/":
    num1 = int(input("enter first number:  "))
    num2 = int(input("enter second number:  "))
    print("Answer is" + " " + str(num1 / num2))
 
if math == "//":
    num1 = int(input("enter first number:  "))
    num2 = int(input("enter second number:  "))
    print("Answer is" + " " + str(num1 // num2))

if math == "*":
    num1 = int(input("enter first number:  "))
    num2 = int(input("enter second number:  "))
    print("Answer is" + " " + str(num1 * num2))

if math == "**":
    num1 = int(input("enter first number:  "))
    num2 = int(input("enter second number:  "))
    print("Answer is" + " " + str(num1 ** num2))

else:
    print("Please type correctly!")
