# Modifying Global Scope

enemies = 1


def increase_enemies1():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

"""increase_enemies2() will give an error
cannot access local variable 'enemies' where it is not associated with a value"""
def increase_enemies2():
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies1()
print(f"enemies outside function: {enemies}")

increase_enemies2()
print(f"enemies outside function: {enemies}")


