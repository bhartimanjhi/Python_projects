# PYTHON CALCULATOR PROJECT:-

print("Welcome to the python calculator...")

num1 = int(input("please enter the first number or value:- "))
num2 = int(input("please enter the second number or value:- "))
opr = input("please select the operation(+, -, *, /):- ")
if opr == '+':
    result = (num1 + num2)
    print("The result of addition is:- ", result)

elif opr == '-':
    result = (num1 - num2)
    print("The result of subtraction is:- ", result)

elif opr == '*':
    result = (num1*num2)
    print("The result of multiplication is:- ", result)

elif opr == '/':
    result = (num1/num2)
    print("The result of division is:- ", result)

else:
    print("Invalid input!, please try again...")

print("Thank you for using python calculator...")
input()
