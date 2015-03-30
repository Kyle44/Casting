# File         lab3.py
# Written by:  Kyle Fritz
# Date:        9/17/13
# Section:     10
# Email:       fritzk1@umbc.edu
# Description: Lab 3, i/o and Math operators
############### USE WITH PYTHON 3 ###########
### scl enable python33 bash


def main():
    
    # Prompt for 3 input values
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num3 = input("Enter third number: ")
    # Casting each input values as integers
    a = int(num1)
    b = int(num2)
    c = int(num3)
    # Perform mathematical operations
    squ1 = a ** 2
    sum23 = b + c 
    # Print the totals
    print("When you square", a, ", you get", squ1)
    print("When you add", b, "and", c, ", you get", sum23) 
main()
