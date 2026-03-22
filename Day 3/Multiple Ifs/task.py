print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    bill = 0
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    photo = input("Do you want to take photos? (y/n)")
    if photo == "y":
        bill += 3
    print(f"The total bill is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
