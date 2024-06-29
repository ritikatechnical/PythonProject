import math

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


def compare(num1, num2):
 if num1 > num2:
    print(f"{num1} is greater than {num2}")
 elif num1 < num2:
    print(f"{num2} is greater than {num1}")
 else:
   print("The numbers are equal")
 pass


result = compare(num1, num2)


