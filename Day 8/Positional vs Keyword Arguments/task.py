# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet(name, greeting):
    print(f"{greeting}, {name}")

greet( "Angela", "Hello")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(name ="Angela", location =  "London")


def my_function(a, b):
    print(a)
    print(b)


my_function(2, 1)