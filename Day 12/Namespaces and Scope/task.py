enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside increase_enemies: {enemies}")
    def create_enemies():
        enemies = 5
        print(f"enemies insicde create_enemies: {enemies}")
    create_enemies() # cannot call outside increase_enemies()
    print(f"enemies outsicde create_enemies: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
