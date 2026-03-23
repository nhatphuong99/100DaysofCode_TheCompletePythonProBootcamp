import random
import test
'''
rand_num = random.randint(1, 10)
#This will produce a random whole number between 1 and 10 (inclusive).
print(rand_num)
print(test.test_num)
print(test.test_str)

rand_num_0_to_1 = random.random() * 10
# (0.0 <= random.random() < 1.0) * 10
random_float = random.uniform(1, 10)
# a <= random.uniform(a,b) <= b
#This will generate a random floating point number between 1 and 10.
print(rand_num_0_to_1)
print(random_float)
'''
rand_heads_or_tails = random.randint(0, 1)
if rand_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")