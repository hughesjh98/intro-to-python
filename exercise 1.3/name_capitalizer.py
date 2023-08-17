# first_name = input(" enter your first name: ")
# middle_name = input("enter your middle name: ")
# last_name = input(" enter your last name: ")

# first_name = first_name.capitalize()
# middle_name = middle_name.capitalize()
# last_name = last_name.capitalize()

# print("your full name is", first_name, middle_name, last_name)

# a = int(input("Enter a number: "))
# b = int(input("Enter a number to be added with the first: "))

# print("the sum of these numbers is: " + str(a + b) )

# age = int(input("Enter your age: "))
# print("Age between 18 and 35: " + str(18 < age < 35))

# fruit = input("I have an apple, an orange and a banana! " \
#     + "Which fruit would you like to have? : ")

# if fruit == "apple":
#     print("Here, have an apple!")

# elif fruit == "orange":
#     print("Here, have an orange!")

# elif fruit == "banana":
#     print("Here, have a banana!")

# else:
#     print("Oops, I don't think I have that.")

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# for i in range(0,8): 
#     print(planets[i])

# num = int(input("Enter a number to be multiplied: "))
# start = int(input("Enter a starting point for the problem: "))
# end = int(input("Enter an end point for the problem: "))
# for mul in range(start, end):
#     if mul == 6:
#         print("we're done!")
#         break
#     print(num * mul)
    
    
#     num = [10,20,30,40,50, "we're all done"]
#     for numbers in num:
#         print(numbers)
    
# text = input("Enter a string: ")
# chars = ['Uppercase' if c.isupper() else 'Lowercase' if c.islower() else 'Other' for c in text]

# print(chars)

# The function gets defined here, arguments
# value1 and value2 are set up to accept values.
# def adder(value1, value2):
#     result = value1 + value2
#     print("The added result is " + str(result))

# # The main code starts here. We'll take the user's inputs now.
# a = int(input("Enter the first value: "))
# b = int(input("Enter the second value: "))

# # Calling adder() which prints the result
# adder(a, b)

# Here's a function that takes value1 and value2,
# # divides value1 by value2 and then prints the result
# def divider(value1, value2):
#     print(value1 / value2)

# # Taking the user's inputs:
# a = int(input("Enter the first value: "))
# b = int(input("Enter the second value: "))

# # Calling divider() by passing keyword arguments
# divider(value1 = a, value2 = b)

def my_func(a, b):
    print("Returning 'a'!") 
    print("Returning 'b'!")
    return a, b

val = my_func(3, 5)
print(val)