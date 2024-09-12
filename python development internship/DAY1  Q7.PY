#create a program that prints the multiplication table of a given number using a while loop
number = int(input("enter a number:"))
multiplier = 1
while number <= 10:
    result = number*multiplier
    print(number,'x', multiplier,'=',result)
    multiplier += 1