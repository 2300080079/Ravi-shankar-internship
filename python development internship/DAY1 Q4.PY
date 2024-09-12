#write a python program that takes an integer input from the user and prints whether the number is positive, negative or zero
number = int(input("enter the number:"))
if number>0:
    print(number,"is positive")
elif number<0:
    print(number,"is negative")
else:
    print(number, "is zero")
          