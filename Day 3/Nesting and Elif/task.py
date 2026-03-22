print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age "))
    ticket = 0
    if age > 18:
        ticket = 12
    elif age >= 12:
        ticket = 7
    else:
        ticket = 5
    print(f"Your ticket is {ticket}$")
else:
    print("Sorry you have to grow taller before you can ride.")
