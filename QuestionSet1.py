# Q1. Write a program to swap the values of two variables without using a third variable.
# a = 10 
# b = 20
# print (f"Before Swaping  Values of a = {a} And b = {b}")
# a, b = b, a
# print (f"After Swaping  Values of a = {a} And b = {b}")


# Q2. Write a program that takes input from the user and checks its data type.
# a = input("Enter the Value : ")
# if a.isdigit():
#     print(f"The value is int")
# elif a.replace(".", "", 1).isdigit():
#     print("The value is float ")
# else :
#     print("The value is string")



# Q3. Write a program to convert Celsius to Fahrenheit. Take the temperature in Celsius as input.
# Formula: F = (C * 9/5) + 32
# Example:
# Input: C = 37
# Output: F = 98.6

# Input
# celsius = float(input("Enter temperature in Celsius: "))

# Conversion
# fahrenheit = (celsius * 9 / 5) + 32

# Output
# print(f"{celsius}°C is equal to {fahrenheit}°F")


#Q4. Take two numbers as input and perform all basic arithmetic operations: addition, subtraction, multiplication, division, and modulus.
# a , b = 10 , 5
# print(f"Value of a : {a}  \nValue of b : {b}")
# print(f"Addition : {a+b}")
# print(f"Subtraction : {a-b}")
# print(f"Multiplaction : {a*b}")
# print(f"Division : {a/b}")
# print(f"Modulus : {a%b}")


# Q5. Take a string input and check if it is a palindrome.
# string = input("Enter Any String : ")
# if string == string[::-1]:
#     print(f"{string} is palindrome string.")
# else :
#     print(f"{string} is not palindrome string.")


# Q6. Take two strings as input and concatenate them without using the + operator.
# str1 = "Hello"
# str2 = "World"
# print(str1+str2)   # HelloWorld


# Q7. Take a list of strings as input and join them into a single string separated by spaces.
# worlds = input("Enter a list of words separated by spaces : ").split()
# print(type(worlds), worlds)
# result = " ".join(worlds)
# print("Joined String : ", result)


# Q8. Take an input as a string, convert it into an integer and a float, and display all three values.
# data = input("Enter String ")
# str_val = data
# int_val = int(data)
# float_val = float(data)
# print(f"String : {str_val}, Integer : {int_val}, Float : {float_val}")



# Q9. Take a string input containing digits and letters and extract only the digits.
# Example:
# Input: abc123xyz
# Output: 123

# step 1
# digits = []
# data = input("Enter value combination of string and digit : ")
# print(data)
# for i in data:
#     if i.isdigit():
#         digits.append(i)
# print("".join(digits))

# step 2 
# data = input("Enter value combination of string and digit : ")
# digits = ''.join(filter(str.isdigit, data))
# print("Digits : ", digits)


# Q10. Take a number as input and print its reverse.
# num = input("Enter The Number")
# reversed_num = num[::-1]
# print(reversed_num)


# Q11. Check Leap Year
# year = int(input("Enter the year : "))
# if (year % 4 == 0 and year % 100 !=  0) or (year % 400 == 0):
#     print(f"{year} is leap year")
# else :
#     print(f"{year} is not leap year")

