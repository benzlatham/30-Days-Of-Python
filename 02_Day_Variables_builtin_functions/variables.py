# Day 2: 30 Days of Python Programming
# Exercise 1 
first_name = 'Benjamin'
last_name = 'Latham'
full_name = first_name + ' ' + last_name
country = 'United States'
city = 'Orange Park'
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = 'yes'
favorite_food, sport, mother = 'pasta', 'volleyball', 'Katherine'

# Exercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(favorite_food))
print(type(sport))
print(type(mother))
print(len(first_name))
if len(first_name) > len(last_name):
    print('First name is longer than last name')
elif len(first_name) < len(last_name):
    print('Last name is longer than first name')
else:
    print('The names have equal length')
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_two / num_one
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)
# Problem 12
import math
radius = 30
area_of_circle = math.pi * radius ** 2
print("Area:", area_of_circle)
circum_of_circle = 2 * math.pi * radius
print("Circumference:", circum_of_circle)
user_radius = int(input("What is the radius?:"))
user_area_of_circle = math.pi * user_radius ** 2
print("Area of circle:", user_area_of_circle)
#problem 13
user_first_name = input("First name:")
user_last_name = input("Last name:")
user_country = input("Country:")
user_age = input("Age:")

help('keywords')