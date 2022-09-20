 # Calculator

#addition
def add(a, b):

   return a + b

#substraction
def subtract(a, b):

   return a - b

#multiplication
def multiply(a, b):
   return a * b

#division
def divide(a, b):
   return a / b

# input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiplb")
print("4.Divide")

choose = input("Enter choose(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choose == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choose == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choose == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choose == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")