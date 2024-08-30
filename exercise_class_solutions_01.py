num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
total = num1 + num2
print("The total sum of first and second number is:",total)
animal = (input("What's your favorite animal? "))
print("My favorite animal is also", animal+"!")
temperature = int(input("Enter the temperature in Fahrenheit: "))
degree_celsius = (temperature - 32)* 5.0/9.0
print(f"When we convert the temperature {temperature} F into celsius, it becomes {degree_celsius} C")
side1 = int(input("The first side of length of triangle is:"))
side2 = int(input("The second side of length of triangle is:"))
side3 = int(input("The third side of length of triangle is:"))
total = side1 + side2 + side3
print("The length of three sides of a triangle is:", total)
number = float(input("Enter a number: "))
square = number ** 2
print("The square of given number is", square)
digits = [1,2,3,4,5]
digits.remove(3)
print(digits)
list1 = [10, 9, 8, 7, 6]
list2 = [5, 4, 3, 2, 1]
list1.extend(list2)
print(list1)
total_items = [10, 20, 30, 40]
print(total_items)
removed_items = total_items.pop()
print(removed_items)
colors = ['red', 'blue', 'green', 'yellow']
green_index = colors.index('green')
print(green_index)