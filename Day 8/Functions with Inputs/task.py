# def greet():
#     print("Hello!")
#     print("How do you do?")
#     print("Isn't the weather nice?")
#
# greet()
from pickle import PROTO


# Function that allows for inputs
#
# def greet_with_name(name):
#
#     print(f"Hello {name}")
#     print(f"How do you do, {name}?")
#
# greet_with_name(input ("What's your name? "))

# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with(input("What is your name? "), input("What is your location? ")

