import random

# random_integer = random.randint(1,100)
# print(random_integer)
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
# random_float = random.uniform(0, 10)
# print(random_float)

random_flip = random.choice([True, False])
print(random_flip)
if random_flip == True:
    print("You have flipped Heads.")
else:
    print("You have flipped Tails.")


