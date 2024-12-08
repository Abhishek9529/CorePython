# Q1. Write a program to swap the values of two variables without using a third variable.
# a = 10 
# b = 20
# print (f"Before Swaping  Values of a = {a} And b = {b}")
# c = a
# a = b
# b = c
# print (f"After Swaping  Values of a = {a} And b = {b}")


# Q2. Write a program that takes input from the user and checks its data type.
try :
    a = int(input("Enter the Value : "))
    print(f" The type of a is : {type(a)}")
except ValueError as e:
    print("Entered Value is Not a Int")