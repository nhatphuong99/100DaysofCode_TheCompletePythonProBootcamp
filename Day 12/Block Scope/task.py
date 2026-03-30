# Accessible anywhere
my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2

print(my_global_var)

for _ in range(10):
    # Accessible anywhere
    my_block_var = 3

print(my_block_var)

"""
def is_prime(num):
    if num <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(num*0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    return is_prime
print(is_prime(4))
"""